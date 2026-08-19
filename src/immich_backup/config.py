import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.IMMICH_API_KEY = os.getenv("IMMICH_API_KEY")
        self.IMMICH_API_URL = os.getenv("IMMICH_API_URL")
        self.IMMICH_API_TIMEOUT = int(os.getenv("IMMICH_API_TIMEOUT") or "60")


config = Config()
