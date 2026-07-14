import asyncio

from market_data.config import Settings
from market_data.providers.fake import FakeMarketDataProvider


async def run_once() -> dict[str, str]:
    settings = Settings()
    if settings.market_data_mode != "fake":
        raise RuntimeError("Only fake market-data mode is available in E1-P01")
    provider = FakeMarketDataProvider(limit=0)
    await provider.stop()
    return {"status": "ok", "service": "market-data", "mode": "fake"}


if __name__ == "__main__":
    print(asyncio.run(run_once()))
