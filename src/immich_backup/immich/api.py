import requests

from immich_backup.config import config
from immich_backup.immich.endpoints.albums import Albums


class Api:
    def __init__(self, api_key: str, api_url: str):
        self.api_key = api_key
        self.api_url = api_url
        self.session = requests.Session()
        self.__init_session()

    def __init_session(self) -> None:
        self.session.headers.update(
            {
                "X-Api-Key": self.api_key,
                "Accept": "application/json",
            }
        )

    def albums(self) -> Albums:
        return Albums(self.session, self.api_url, config.IMMICH_API_TIMEOUT)


api = Api(
    config.IMMICH_API_KEY,
    config.IMMICH_API_URL,
)

albums = api.albums()
