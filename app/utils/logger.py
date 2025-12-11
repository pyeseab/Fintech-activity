import logging
from config import LOG_LEVEL

# Create a logger object
logger = logging.getLogger("portfolio_app")
logger.setLevel(LOG_LEVEL)  # e.g., "INFO" from config.py

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)

# Optional: create a file handler
file_handler = logging.FileHandler("portfolio_app.log")
file_handler.setLevel(LOG_LEVEL)

# Define log format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Example usage:
# logger.info("This is an info message")
# logger.error("This is an error message")
