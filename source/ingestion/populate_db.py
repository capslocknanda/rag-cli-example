import re

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_core.documents import Document

# --- CONFIGURATION ---
DOCS_DIRECTORY = "../../rag-docs/pages-raw"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "viewsonic_software_docs"

# Native Ollama Provider (Fixes the 400 BadRequest Error)
embeddings_provider = OllamaEmbeddings(
    model="mxbai-embed-large",
    base_url="http://localhost:11434"
)

def extract_source_and_trim(doc: Document) -> Document:
    """
    Extracts the first-line URL and trims all content before the first '#' tag.
    """
    content = doc.page_content
    
    # 1. Extract Source URL from the first line
    source_match = re.search(r'^Source:\s*(https?://[^\s]+)', content, re.MULTILINE)
    doc.metadata = {"url": source_match.group(1) if source_match else "Unknown Source"}
    
    # 2. Drop everything before the first '#' (Navigation/Menu noise)
    first_header_idx = content.find('#')
    if first_header_idx != -1:
        content = content[first_header_idx:]
    else:
        # If no # tag exists, clear content to avoid ingesting purely nav links
        doc.page_content = ""
        return doc

    # 3. Basic Sanitization: clean trailing whitespace and redundant newlines
    lines = [line.rstrip() for line in content.splitlines()]
    content = "\n".join(lines)
    doc.page_content = re.sub(r'\n{3,}', '\n\n', content).strip()
    
    return doc

def run_ingestion_pipeline():
    """
    Simplified pipeline using only RecursiveCharacterTextSplitter and URL metadata.
    """
    print(f"Loading files from {DOCS_DIRECTORY}...")
    
    loader = DirectoryLoader(
        DOCS_DIRECTORY, 
        glob="**/*.md", 
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'}
    )
    
    raw_documents = loader.load()
    if not raw_documents:
        print("No documents found.")
        return

    # 1. Trim noise and extract URL
    processed_docs = [extract_source_and_trim(doc) for doc in raw_documents]

    # 2. Simplified Recursive Chunking
    # chunk_size is large to keep context, min length check happens after
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=150,
        add_start_index=True,
        strip_whitespace=True
    )

    final_chunks = []
    for doc in processed_docs:
        if not doc.page_content:
            continue
            
        # Perform simple recursive splitting
        chunks = text_splitter.split_documents([doc])
        
        # 3. Filter: Only include chunks with at least 200 characters
        # This prevents tiny footers/fragments from cluttering the DB
        for chunk in chunks:
            if len(chunk.page_content) >= 200:
                final_chunks.append(chunk)

    # 4. Ingest into Qdrant
    print(f"Ingesting {len(final_chunks)} chunks into Qdrant...")
    QdrantVectorStore.from_documents(
        final_chunks,
        embeddings_provider,
        url=QDRANT_URL,
        collection_name=COLLECTION_NAME,
        force_recreate=True 
    )
    print("Database population complete.")

if __name__ == "__main__":
    run_ingestion_pipeline()