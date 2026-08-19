from uuid import UUID

from immich_backup.immich.responses.responses import Responses


class ContributorCountResponse(Responses):
    asset_count: int
    user_id: UUID
