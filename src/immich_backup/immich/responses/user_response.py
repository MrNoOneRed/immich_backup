from datetime import datetime
from uuid import UUID

from pydantic import EmailStr

from immich_backup.immich.enums.user_avatar_color_enum import UserAvatarColorEnum
from immich_backup.immich.responses.responses import Responses


class UserResponse(Responses):
    avatar_color: UserAvatarColorEnum
    email: EmailStr
    id: UUID
    name: str
    profile_changed_at: datetime
    profile_image_path: str
