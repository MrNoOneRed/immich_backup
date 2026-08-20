from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import EmailStr

from immich_backup.immich.models.base import ImmichResponse


class UserResponse(ImmichResponse):
    avatar_color: UserAvatarColorEnum
    email: EmailStr
    id: UUID
    name: str
    profile_changed_at: datetime
    profile_image_path: str


class UserAvatarColorEnum(Enum):
    primary = "primary"
    pink = "pink"
    red = "red"
    yellow = "yellow"
    blue = "blue"
    green = "green"
    purple = "purple"
    orange = "orange"
    gray = "gray"
    amber = "amber"
