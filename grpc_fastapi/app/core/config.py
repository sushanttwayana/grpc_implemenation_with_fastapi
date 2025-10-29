from dotenv import load_dotenv
import os
import logging

class Settings:
    logging_level = logging.getLevelName(os.environ.get("LOGGING_LEVEL", "INFO"))
    log_format = os.environ.get("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    grpc_bar = os.environ.get("GRPC_BAR", "localhost")
    grpc_bakery = os.environ.get("GRPC_BAKERY", "localhost")
    grpc_kitchen = os.environ.get("GRPC_KITCHEN", "localhost")
    
    
settings = Settings()