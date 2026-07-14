from collections.abc import AsyncIterator
from typing import Protocol, TypedDict


class Tick(TypedDict):
    symbol: str
    price: str
    sequence: int


class MarketDataProvider(Protocol):
    def stream(self) -> AsyncIterator[Tick]: ...
    async def stop(self) -> None: ...
