from typing import Self

from immich_backup.config import config
from immich_backup.immich.endpoints.albums import Albums
from immich_backup.immich.endpoints.search import Search
from immich_backup.immich.session import ImmichSession


class Immich:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.session = ImmichSession(base_url, api_key)
        self.albums = Albums(self.session)
        self.search = Search(self.session)

    def close(self) -> None:
        self.session.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args) -> None:
        self.close()


immich = Immich(config.IMMICH_API_BASE_URL, config.IMMICH_API_KEY)
