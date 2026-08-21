from immich_backup.immich.endpoints.base import BaseEndpoints
from immich_backup.immich.models.search import (
    SearchAssetsQuery,
    SearchAssetsRequest,
    SearchAssetsResponse,
)


class Search(BaseEndpoints):
    def search_assets(
        self,
        query: SearchAssetsQuery | None = None,
        request: SearchAssetsRequest | None = None,
    ) -> SearchAssetsResponse:
        return self._session.request(
            method="POST",
            path="search/metadata",
            params=query,
            body=request,
            response_type=SearchAssetsResponse,
        )
