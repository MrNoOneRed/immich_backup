import requests
from pydantic import TypeAdapter

from immich_backup.immich.params.get_albums_params import GetAlbumsParams
from immich_backup.immich.responses.album_response import AlbumResponse


class Albums:
    def __init__(self, session: requests.Session, baseurl: str, timeout: int = 60):
        self.session = session
        self.baseurl = baseurl
        self.timeout = timeout

    def get_albums(self, params: GetAlbumsParams | None = None) -> list[AlbumResponse]:
        url = self.baseurl + "/albums"
        response = self.session.get(
            url,
            timeout=self.timeout,
            params=params.to_query_params() if params else None,
        )
        response.raise_for_status()
        json = response.json()

        adapter = TypeAdapter(list[AlbumResponse])

        return adapter.validate_python(json)
