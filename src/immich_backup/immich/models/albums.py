from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import Field

from immich_backup.immich.models.assets import AssetOrderEnum
from immich_backup.immich.models.base import ImmichQuery, ImmichResponse
from immich_backup.immich.models.common import ContributorCountResponse
from immich_backup.immich.models.users import UserResponse


class GetAllAlbumsQuery(ImmichQuery):
    asset_id: UUID | None = None
    id: UUID | None = None
    is_owned: bool | None = None
    is_shared: bool | None = None
    name: str | None = None


class AlbumResponse(ImmichResponse):
    album_name: str
    album_thumbnail_asset_id: UUID | None
    album_users: list[AlbumUserResponse]
    asset_count: int
    contributor_counts: list[ContributorCountResponse] = Field(default_factory=list)
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


class AlbumUserResponse(ImmichResponse):
    role: AlbumUserRoleEnum
    user: UserResponse


class AlbumUserRoleEnum(Enum):
    editor = "editor"
    owner = "owner"
    viewer = "viewer"
