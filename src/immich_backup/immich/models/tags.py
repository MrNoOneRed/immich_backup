from datetime import datetime
from uuid import UUID

from immich_backup.immich.models.base import ImmichResponse


class TagResponse(ImmichResponse):
    color: str
    created_at: datetime
    id: UUID
    name: str
    parent_id: str
    updated_at: datetime
    value: str
