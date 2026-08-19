from datetime import datetime
from uuid import UUID

from immich_backup.immich.enums.asset_order_enum import AssetOrderEnum
from immich_backup.immich.responses.album_user_response import AlbumUserResponse
from immich_backup.immich.responses.contributor_count_response import (
    ContributorCountResponse,
)
from immich_backup.immich.responses.responses import Responses


class AlbumResponse(Responses):
    album_name: str
    album_thumbnail_asset_id: UUID | None
    album_users: list[AlbumUserResponse]
    asset_count: int
    contributor_counts: list[ContributorCountResponse] = []
    created_at: datetime
    description: str
    end_date: datetime
    has_shared_link: bool
    id: UUID
    is_activity_enabled: bool
    last_modified_asset_timestamp: datetime
    order: AssetOrderEnum
    shared: bool
    start_date: datetime
    updated_at: datetime
