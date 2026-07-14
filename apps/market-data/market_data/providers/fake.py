import asyncio
from collections.abc import AsyncIterator

from market_data.providers.base import Tick


class FakeMarketDataProvider:
    def __init__(self, symbol: str = "FAKE-USD", limit: int = 3) -> None:
        self.symbol = symbol
        self.limit = limit
        self._stopped = False

    async def stream(self) -> AsyncIterator[Tick]:
        for idx in range(self.limit):
            if self._stopped:
                break
            await asyncio.sleep(0)
            yield {"symbol": self.symbol, "price": f"{100 + idx}.00", "sequence": idx}

    async def stop(self) -> None:
        self._stopped = True
