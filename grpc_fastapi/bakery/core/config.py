from dotenv import load_dotenv
import os
import logging

class Settings:
    logging_level = logging.getLevelName(os.environ.get("LOGGING_LEVEL", "INFO"))
    log_format = os.environ.get("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
settings = Settings()