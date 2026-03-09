from app.tools.calculator import calculate
from app.tools.search  import web_search
from app.tools.vector_search import search_knowledge_base 
from app.utils.logger import logger


TOOLS = {
    "calculator": calculate,
    "search": web_search,
    "vector_search": search_knowledge_base
}

def execute_tool(tool_name, input_data):

    if tool_name not in TOOLS:
        logger.error(f"Tool {tool_name} not found")
        return "Tool not available."

    try:

        tool_function = TOOLS[tool_name]

        result = tool_function(input_data)

        return result

    except Exception as e:

        logger.error(f"Tool execution error: {e}")

        return f"Error executing tool: {str(e)}"
    

if __name__ == "__main__":

    print("Calculator Test:")
    print(execute_tool("calculator", "5 * 8"))

    print("\nWeb Search Test:")
    print(execute_tool("search", "latest AI news"))

    print("\nVector Search Test:")
    print(execute_tool("vector_search", "What is artificial intelligence?"))