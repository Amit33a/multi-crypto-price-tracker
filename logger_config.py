import logging

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Attach handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
