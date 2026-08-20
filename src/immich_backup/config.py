import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.IMMICH_API_KEY = os.getenv("IMMICH_API_KEY")
        self.IMMICH_API_BASE_URL = os.getenv("IMMICH_API_BASE_URL")
        self.IMMICH_API_TIMEOUT = int(os.getenv("IMMICH_API_TIMEOUT") or "60")

        if not self.IMMICH_API_KEY:
            raise ValueError("IMMICH_API_KEY is not set")

        if not self.IMMICH_API_BASE_URL:
            raise ValueError("IMMICH_API_BASE_URL is not set")


config = Config()
