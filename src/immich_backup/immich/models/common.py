from datetime import datetime
from uuid import UUID

from immich_backup.immich.models.base import ImmichResponse


class ContributorCountResponse(ImmichResponse):
    asset_count: int
    user_id: UUID


class ExifResponse(ImmichResponse):
    city: str | None = None
    country: str | None = None
    date_time_original: datetime | None = None
    description: str | None = None
    exif_image_height: int | None = None
    exif_image_width: int | None = None
    exposure_time: str | None = None
    f_number: int | None = None
    file_size_in_byte: int | None = None
    focal_length: int | None = None
    iso: int | None = None
    latitude: int | None = None
    lens_model: str | None = None
    longitude: int | None = None
    make: str | None = None
    model: str | None = None
    modify_date: datetime | None = None
    orientation: str | None = None
    projection_type: str | None = None
    rating: int | None = None
    state: str | None = None
    time_zone: str | None = None
