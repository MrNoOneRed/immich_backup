from immich_backup.immich.endpoints.base import BaseEndpoints
from immich_backup.immich.models.albums import AlbumResponse, GetAllAlbumsQuery


class Albums(BaseEndpoints):
    def get_all_albums(
        self, query: GetAllAlbumsQuery | None = None
    ) -> list[AlbumResponse]:
        return self._session.request(
            method="GET",
            path="albums",
            params=query,
            response_type=list[AlbumResponse],
        )
