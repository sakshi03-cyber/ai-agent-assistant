from tavily import TavilyClient
from app.config import TAVILY_API_KEY 
from app.utils.logger import logger
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=api_key)

def web_search(query: str):

    logger.info(f"Web search tool called with query: {query}")

    try:

        response = client.search(
            query=query,
            search_depth="basic",
            max_results=3
        )

        results = []

        for r in response["results"]:
            results.append(
                f"{r['title']}\n{r['content']}\nSource: {r['url']}\n"
            )

        return "\n".join(results)

    except Exception as e:

        logger.error(f"Web search error: {e}")

        return f"Error during web search: {str(e)}"


if __name__ == "__main__":

    result = web_search("latest AI news")

    print(result)