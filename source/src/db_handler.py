from qdrant_client import QdrantClient
from ollama import Client as OllamaClient
from src.log_setup import log
import os
import time

class QdrantRetriever:
    def __init__(self):
        self.q_client = QdrantClient(url=os.getenv("QDRANT_URL", "http://localhost:6333"))
        self.o_client = OllamaClient(host=os.getenv("OLLAMA_HOST", "http://localhost:11434"))
        self.o_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "mxbai-embed-large")
        self.q_collection = os.getenv("QDRANT_COLLECTION_NAME", "viewsonic_software_docs")
        self.q_limit = int(os.getenv("QDRANT_SEARCH_LIMIT", "4"))

    def get_context(self, query: str):
        log.info(f"Starting retrieval for: '{query}'")
        
        start_embed = time.perf_counter()
        emb_res = self.o_client.embeddings(model=self.o_model, prompt=query)
        emb = emb_res["embedding"]
        embed_duration = time.perf_counter() - start_embed
        log.debug(f"Embedding generated in {embed_duration:.4f}s using {self.o_model}")
        
        try:
            hits = self.q_client.query_points(
                collection_name=self.q_collection,
                query=emb,
                limit=self.q_limit,
                with_payload=True
            ).points
        except Exception as e:
            log.error(f"Qdrant search failed: {str(e)}")
            return ""

        log.info(f"Found {len(hits)} relevant chunks")
        
        context_parts = []
        total_chars = 0
        
        for i, h in enumerate(hits):
            p = h.payload
            content = p.get('text', '')
            source = p.get('source', 'Unknown')
            section = p.get('section', 'N/A')
            
            chunk_len = len(content)
            total_chars += chunk_len
            
            log.debug(
                f"Hit [{i+1}] | Length: {chunk_len} chars | "
                f"Source: {source.split('/')[-1]} | Section: {section}"
            )
            log.debug(f"Content: {content}")
            
            if chunk_len < 80:
                log.warning(f"Small chunk detected at Hit [{i+1}]. Possible noise or poor split.")

            context_parts.append(
                f"Source: {source} (Section: {section})\nContent: {content}"
            )
        
        final_context = "\n\n".join(context_parts)
        
        log.info(
            f"Context Assembly Complete | Total Size: {total_chars} characters | "
            f"Avg Chunk Size: {total_chars/len(hits) if hits else 0:.1f} chars"
        )
        
        return final_context