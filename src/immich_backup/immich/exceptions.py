from typing import Any

import httpx


class ImmichError(Exception):
    """Base exception for all Immich client errors."""


class ImmichConnectionError(ImmichError):
    """Network/connection error."""


class ImmichApiError(ImmichError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error: str | None = None,
        response: httpx.Response | None = None,
    ) -> None:
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.error = error
        self.response = response

    @classmethod
    def from_response(
        cls,
        response: httpx.Response,
    ) -> ImmichApiError:
        message: str | None = None
        error: str | None = None

        try:
            data: Any = response.json()
        except ValueError:
            data = None

        if isinstance(data, dict):
            value = data.get("message")
            if isinstance(value, str):
                message = value

            value = data.get("error")
            if isinstance(value, str):
                error = value

        if message is None:
            message = response.reason_phrase or "Immich API request failed"

        exception_type: type[ImmichApiError] = cls

        match response.status_code:
            case 401 | 403:
                exception_type = ImmichAuthenticationError

            case 404:
                exception_type = ImmichNotFoundError

            case 400 | 422:
                exception_type = ImmichValidationError

        return exception_type(
            message,
            status_code=response.status_code,
            error=error,
            response=response,
        )

    def __str__(self) -> str:
        return f"Immich API error {self.status_code}: {self.message}"


class ImmichAuthenticationError(ImmichApiError):
    pass


class ImmichNotFoundError(ImmichApiError):
    pass


class ImmichValidationError(ImmichApiError):
    pass
