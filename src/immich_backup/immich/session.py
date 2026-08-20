from typing import overload

import httpx
from pydantic import BaseModel, TypeAdapter

from immich_backup.immich.exceptions import ImmichApiError, ImmichConnectionError


class ImmichSession:
    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout: float = 30.0,
    ) -> None:
        self._client = httpx.Client(
            base_url=base_url.rstrip("/") + "/",
            headers={
                "Accept": "application/json",
                "x-api-key": api_key,
            },
            timeout=timeout,
        )

    @overload
    def request[T](
        self,
        method: str,
        path: str,
        *,
        params: BaseModel | None = None,
        body: BaseModel | None = None,
        response_type: type[T],
    ) -> T: ...

    @overload
    def request(
        self,
        method: str,
        path: str,
        *,
        params: BaseModel | None = None,
        body: BaseModel | None = None,
        response_type: None = None,
    ) -> None: ...

    def request[T](
        self,
        method: str,
        path: str,
        *,
        params: BaseModel | None = None,
        body: BaseModel | None = None,
        response_type: type[T] | None = None,
    ) -> T | None:
        query = (
            params.model_dump(
                mode="json",
                by_alias=True,
                exclude_none=True,
            )
            if params
            else None
        )

        payload = (
            body.model_dump(
                mode="json",
                by_alias=True,
                exclude_none=True,
            )
            if body
            else None
        )
        try:
            response = self._client.request(
                method,
                path,
                params=query,
                json=payload,
            )
        except httpx.RequestError as exc:
            raise ImmichConnectionError(
                f"Failed to communicate with Immich: {exc}"
            ) from exc

        if response.is_error:
            raise ImmichApiError.from_response(response)

        if response.status_code == 204:
            return None

        if response_type is None:
            return None

        return TypeAdapter(response_type).validate_python(response.json())

    def close(self) -> None:
        self._client.close()
