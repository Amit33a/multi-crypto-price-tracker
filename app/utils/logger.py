import logging
from pathlib import Path

# Create logs directory if it doesn't exist
Path("logs").mkdir(parents=True, exist_ok=True)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False

# Prevent duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
