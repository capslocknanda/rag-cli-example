import os
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from src.log_setup import log

class QdrantRetriever:
    def __init__(self):
        # Configuration from environment variables
        self.q_url = os.getenv("QDRANT_URL", "http://localhost:6333")
        self.o_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        self.o_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "mxbai-embed-large")
        self.collection_name = os.getenv("QDRANT_COLLECTION_NAME", "viewsonic_software_docs")
        self.search_limit = int(os.getenv("QDRANT_SEARCH_LIMIT", "5"))

        # Initialize Native Ollama Embeddings
        self.embeddings = OllamaEmbeddings(
            model=self.o_model,
            base_url=self.o_host
        )

        # Initialize Qdrant Client and Vector Store
        self.client = QdrantClient(url=self.q_url)
        self.vector_store = QdrantVectorStore(
            client=self.client,
            collection_name=self.collection_name,
            embedding=self.embeddings
        )

    def get_context(self, query: str) -> str:
        """
        Retrieves relevant documents from Qdrant and formats them into a 
        context string with source URLs for the LLM.
        """
        log.info(f"Retrieving context for query: '{query}'")

        try:
            # Perform similarity search with metadata
            docs = self.vector_store.similarity_search(
                query, 
                k=self.search_limit
            )
        except Exception as e:
            log.error(f"LangChain Qdrant search failed: {str(e)}")
            return ""

        if not docs:
            log.warning("No relevant documents found in Qdrant.")
            return ""

        context_parts = []
        for i, doc in enumerate(docs):
            # Extract metadata from the new ingestion structure
            source_url = doc.metadata.get("url", "Unknown Source")
            content = doc.page_content.strip()

            log.debug(f"Hit [{i+1}] | Source: {source_url} | Length: {len(content)} chars")

            # Format the chunk for the LLM prompt
            context_parts.append(
                f"--- DOCUMENT CHUNK {i+1} ---\n"
                f"Source URL: {source_url}\n"
                f"Content: {content}"
            )

        final_context = "\n\n".join(context_parts)
        
        log.info(f"Context retrieval complete. Total characters: {len(final_context)}")
        return final_context