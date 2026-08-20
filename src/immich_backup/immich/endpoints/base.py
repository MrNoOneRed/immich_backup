from immich_backup.immich.session import ImmichSession


class BaseEndpoints:
    def __init__(self, session: ImmichSession) -> None:
        self._session = session