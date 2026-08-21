from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import Field

from immich_backup.immich.models.base import ImmichResponse
from immich_backup.immich.models.common import ExifResponse
from immich_backup.immich.models.people import PersonResponse
from immich_backup.immich.models.tags import TagResponse
from immich_backup.immich.models.users import UserResponse


class AssetOrderEnum(Enum):
    asc = "asc"
    desc = "desc"


class AssetVisibilityEnum(Enum):
    archive = "archive"
    timeline = "timeline"
    hidden = "hidden"
    locked = "locked"


class AssetTypeEnum(Enum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    OTHER = "OTHER"


class AssetResponse(ImmichResponse):
    checksum: str
    created_at: datetime
    duplicate_id: UUID | None = None
    duration: int | None = None
    exif_info: ExifResponse | None = None
    file_created_at: datetime
    file_modified_at: datetime
    has_metadata: bool
    height: int | None = None
    id: UUID
    is_archived: bool
    is_edited: bool
    is_favorite: bool
    is_offline: bool
    is_trashed: bool
    library_id: UUID | None = None
    live_photo_video_id: str | None = None
    local_date_time: datetime
    original_file_name: str | None = None
    original_mime_type: str | None = None
    original_path: str | None = None
    owner: UserResponse | None = None
    owner_id: UUID
    people: list[PersonResponse] = Field(default_factory=list)
    resized: bool
    stack: AssetStackResponse | None = None
    tags: list[TagResponse] = Field(default_factory=list)
    thumbhash: str | None = None
    type: AssetTypeEnum
    updated_at: datetime
    visibility: AssetVisibilityEnum
    width: int | None = None


class AssetStackResponse(ImmichResponse):
    asset_count: int
    id: UUID
    primary_asset_id: UUID
