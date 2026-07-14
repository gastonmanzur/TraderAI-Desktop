import re
import uuid
from collections.abc import Awaitable, Callable

from starlette.requests import Request
from starlette.responses import Response

HEADER = "X-Correlation-ID"
_VALID = re.compile(r"^[A-Za-z0-9._:-]{1,128}$")


def normalize_correlation_id(value: str | None) -> str:
    if value and _VALID.fullmatch(value):
        return value
    return str(uuid.uuid4())


async def correlation_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    correlation_id = normalize_correlation_id(request.headers.get(HEADER))
    request.state.correlation_id = correlation_id
    response = await call_next(request)
    response.headers[HEADER] = correlation_id
    return response
