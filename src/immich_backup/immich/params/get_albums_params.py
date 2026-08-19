from uuid import UUID

from immich_backup.immich.params.params import Params


class GetAlbumsParams(Params):
    asset_id: UUID | None = None
    id: UUID | None = None
    is_owned: bool | None = None
    is_shared: bool | None = None
    name: str | None = None
