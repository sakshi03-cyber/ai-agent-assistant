from app.services.tool_router import TOOLS
from loguru import logger
import re 

def is_math_query(query: str) -> bool:
    """
    Detect if the query contains a math expression
    """
    pattern = r"[0-9]+\s*[\+\-\*\/]\s*[0-9]+"
    return bool(re.search(pattern, query)) 


def is_pdf_query(query: str) -> bool:
    keywords = ["document", "pdf", "file", "knowledge", "according"]
    
    for word in keywords:
        if word in query.lower():
            return True
            
    return False 


def run_agent(query: str):

    logger.info(f"Agent received query: {query}")

    try:

        if is_math_query(query):

            logger.info("Using calculator tool")

            tool = TOOLS["calculator"]

            result = tool(query)

            return result


        elif is_pdf_query(query):

            logger.info("Using vector search tool")

            tool = TOOLS["vector_search"]

            result = tool(query)

            return result


        else:

            logger.info("Using web search tool")

            tool = TOOLS["search"]

            result = tool(query)

            return result


    except Exception as e:

        logger.error(f"Agent error: {e}")

        return "Something went wrong while processing the query."