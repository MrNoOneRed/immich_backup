from immich_backup.immich.enums.album_user_role_enum import AlbumUserRoleEnum
from immich_backup.immich.responses.responses import Responses
from immich_backup.immich.responses.user_response import UserResponse


class AlbumUserResponse(Responses):
    role: AlbumUserRoleEnum
    user: UserResponse
