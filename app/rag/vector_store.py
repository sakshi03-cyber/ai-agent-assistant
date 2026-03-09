import chromadb
from app.utils.logger import logger
from app.rag.embedding import embed_documents 

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="knowledge_base"
) 

def store_documents(chunks):

    logger.info("Storing documents in vector database")

    try:

        texts = [chunk.page_content for chunk in chunks]

        embeddings = embed_documents(chunks)

        ids = [str(i) for i in range(len(texts))]

        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )

        logger.info(f"Stored {len(texts)} documents")

    except Exception as e:

        logger.error(f"Vector store error: {e}") 

def search_documents(query, n_results=3):

    logger.info(f"Searching for: {query}")

    try:

        from app.rag.embedding import embed_text

        query_embedding = embed_text(query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return results["documents"][0]

    except Exception as e:

        logger.error(f"Search error: {e}")

        return []       

if __name__ == "__main__":

    from app.rag.document_loader import load_pdf
    from app.rag.chunking import chunk_documents

    docs = load_pdf("data/sample-report.pdf")

    chunks = chunk_documents(docs)

    store_documents(chunks)

    results = search_documents("What is artificial intelligence?")

    print("Search Results:\n")

    for r in results:
        print(r)
        print("\n---\n")     