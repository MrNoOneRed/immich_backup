from uuid import UUID

from immich_backup.immich.models.base import ImmichResponse


class ContributorCountResponse(ImmichResponse):
    asset_count: int
    user_id: UUID