from datetime import datetime
from uuid import UUID

from immich_backup.immich.models.base import ImmichResponse


class PersonResponse(ImmichResponse):
    birth_date: datetime | None = None
    color: str
    id: UUID
    is_favorite: bool
    is_hidden: bool
    name: str
    thumbnail_path: str
    updated_at: datetime
