import os
import re
import dspy
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from ollama import Client as OllamaClient

# --- CONFIGURATION ---
DOCS_DIR = "../../rag-docs/pages-raw"
QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "viewsonic_software_docs"
EMBED_MODEL = "mxbai-embed-large"
VECTOR_SIZE = 1024 # mxbai-embed-large dimension

# Initialize Clients
q_client = QdrantClient(url=QDRANT_URL)
o_client = OllamaClient(host="http://localhost:11434")

def create_collection():
    """Initializes the Qdrant collection if it doesn't exist."""
    if not q_client.collection_exists(COLLECTION_NAME):
        q_client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE),
        )
        print(f"Created collection: {COLLECTION_NAME}")

def semantic_header_chunking(text):
    """
    Splits markdown by headers while maintaining hierarchy.
    Returns a list of dicts with content and section info.
    """
    # Split by headers (h1, h2, h3)
    segments = re.split(r'(^#+\s.*)', text, flags=re.MULTILINE)
    
    chunks = []
    current_section = "General"
    current_sub_section = ""
    
    for i in range(len(segments)):
        part = segments[i].strip()
        if not part: 
            continue
        
        # If it's a header, update current context
        if part.startswith('#'):
            if part.startswith('###'): 
                current_sub_section = part.replace('#', '').strip()
            else: 
                current_section = part.replace('#', '').strip()
                current_sub_section = "" # Reset sub-section on new main section
        else:
            # This is the content following a header
            chunks.append({
                "content": part,
                "section": current_section,
                "sub_section": current_sub_section
            })
    return chunks

def populate_db():
    create_collection()
    idx = 0
    
    for filename in os.listdir(DOCS_DIR):
        if not filename.endswith(".md"): 
            continue
        
        file_path = os.path.join(DOCS_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            raw_text = f.read()
        
        # Extract Source Link (from the header we added in the scraper)
        source_match = re.search(r'Source: (https?://[^\s]+)', raw_text)
        source_url = source_match.group(1) if source_match else filename
        
        # Clean the text (remove the Source line for embedding)
        clean_text = re.sub(r'Source: https?://[^\s]+', '', raw_text).strip()
        
        # Chunking based on Markdown Hierarchy
        chunks = semantic_header_chunking(clean_text)
        
        print(f"Processing {filename}: {len(chunks)} chunks found.")
        
        for chunk in chunks:
            # Generate Embedding via Ollama
            response = o_client.embeddings(model=EMBED_MODEL, prompt=chunk["content"])
            embedding = response["embedding"]
            
            # Prepare Payload for Qdrant
            payload = {
                "source": source_url,
                "section": chunk["section"],
                "sub_section": chunk["sub_section"],
                "text": chunk["content"]
            }
            
            # Upsert to Qdrant
            q_client.upsert(
                collection_name=COLLECTION_NAME,
                points=[
                    PointStruct(
                        id=idx,
                        vector=embedding,
                        payload=payload
                    )
                ]
            )
            idx += 1

if __name__ == "__main__":
    populate_db()
    print("Database population complete!")