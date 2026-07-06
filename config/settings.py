import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

class Settings:
    """
    Centralized configuration class that reads from environment variables.
    This ensures credentials are never hardcoded in tests.
    """
    BASE_URL = os.getenv("COMPANY_BASE_URL", "")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")
    REGULAR_USERNAME = os.getenv("REGULAR_USERNAME", "")
    REGULAR_PASSWORD = os.getenv("REGULAR_PASSWORD", "")
    BROWSER = os.getenv("BROWSER", "edge").lower()
