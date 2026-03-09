from loguru import logger
import sys

logger.remove()  # remove default logger

# Console logging
logger.add(
    sys.stdout,
    level="INFO",
    format="{time} | {level} | {message}"
)

# File logging
logger.add(
    "logs/agent.log",
    rotation="5 MB",
    retention="10 days",
    level="INFO"
)