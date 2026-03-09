from sentence_transformers import SentenceTransformer
from app.utils.logger import logger 

model = SentenceTransformer("all-MiniLM-L6-v2") 

def embed_text(text: str):

    logger.info("Generating embedding")

    try:

        embedding = model.encode(text)

        return embedding.tolist()

    except Exception as e:

        logger.error(f"Embedding error: {e}")

        return None 
    
def embed_documents(chunks):

    logger.info("Generating embeddings for documents")

    texts = [chunk.page_content for chunk in chunks]

    embedding = model.encode(texts)

    return embedding

if __name__ == "__main__":

    text = "Artificial intelligence is transforming industries."

    vector = embed_text(text)

    print("Vector length:", len(vector))

    print("First 10 values:", vector[:10])
    