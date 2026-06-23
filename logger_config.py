import logging

# Configure application logging
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create reusable logger object
logger = logging.getLogger(__name__)