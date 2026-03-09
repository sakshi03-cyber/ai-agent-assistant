from app.rag.vector_store import search_documents
from app.utils.logger import logger 

def search_knowledge_base(query: str):

    logger.info(f"Knowledge base search called with query: {query}")

    try:

        results = search_documents(query)

        if not results:
            return "No relevant documents found."

        combined_results = "\n\n".join(results)

        return combined_results

    except Exception as e:

        logger.error(f"Vector search tool error: {e}")

        return f"Error searching knowledge base: {str(e)}" 
    
if __name__ == "__main__":

    query = "What is artificial intelligence?"

    result = search_knowledge_base(query)

    print("\nRetrieved Knowledge:\n")

    print(result)    