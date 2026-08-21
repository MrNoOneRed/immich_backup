from datetime import datetime
from uuid import UUID

from pydantic import Field

from immich_backup.immich.models.albums import AlbumResponse
from immich_backup.immich.models.assets import (
    AssetOrderEnum,
    AssetResponse,
    AssetTypeEnum,
    AssetVisibilityEnum,
)
from immich_backup.immich.models.base import ImmichQuery, ImmichRequest, ImmichResponse


class SearchAssetsQuery(ImmichQuery):
    key: str | None = None
    slug: str | None = None


class SearchAssetsRequest(ImmichRequest):
    album_ids: list[UUID] = Field(default_factory=list)
    checksum: str | None = None
    city: str | None = None
    country: str | None = None
    created_after: datetime | None = None
    created_before: datetime | None = None
    description: str | None = None
    encoded_video_path: str | None = None
    id: UUID | None = None
    is_encoded: bool | None = None
    is_favorite: bool | None = None
    is_motion: bool | None = None
    is_not_in_album: bool | None = None
    is_offline: bool | None = None
    lens_model: str | None = None
    library_id: UUID | None = None
    make: str | None = None
    model: str | None = None
    ocr: str | None = None
    order: AssetOrderEnum | None = None
    original_file_name: str | None = None
    original_path: str | None = None
    page: int | None = None
    person_ids: list[UUID] = Field(default_factory=list)
    preview_path: str | None = None
    rating: int | None = None
    size: int | None = None
    state: str | None = None
    tag_ids: list[UUID] | None = None
    taken_after: datetime | None = None
    taken_before: datetime | None = None
    thumbnail_path: str | None = None
    trashed_after: datetime | None = None
    trashed_before: datetime | None = None
    type: AssetTypeEnum | None = None
    updated_after: datetime | None = None
    updated_before: datetime | None = None
    visibility: AssetVisibilityEnum | None = None
    with_deleted: bool | None = None
    with_exif: bool | None = None
    with_people: bool | None = None
    with_stacked: bool | None = None


class SearchAssetsResponse(ImmichResponse):
    albums: SearchAlbumResponse | None = None
    assets: SearchAssetResponse | None = None


class SearchAlbumResponse(ImmichResponse):
    count: int
    facets: list[SearchFacetResponse] = Field(default_factory=list)
    items: list[AlbumResponse] = Field(default_factory=list)
    total: int


class SearchFacetResponse(ImmichResponse):
    counts: SearchFacetCountResponse
    field_name: str


class SearchFacetCountResponse(ImmichResponse):
    count: int
    value: str


class SearchAssetResponse(ImmichResponse):
    count: int
    facets: list[SearchFacetResponse] = Field(default_factory=list)
    items: list[AssetResponse] = Field(default_factory=list)
    next_page: str | None = None
    total: int
