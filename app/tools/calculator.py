from sympy import sympify
from app.utils.logger import logger
def calculate(expression: str):

    logger.info(f"Calculator tool called with: {expression}")

    try:
        result = sympify(expression)
        return str(result)

    except Exception as e:
        return f"Error in calculation: {str(e)}"

if __name__ == "__main__":
    print(calculate("2+2"))
    print(calculate("10*5"))
    print(calculate("sqrt(16)"))
