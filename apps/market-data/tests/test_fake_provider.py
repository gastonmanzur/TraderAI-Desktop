import pytest
from market_data.providers.fake import FakeMarketDataProvider


@pytest.mark.asyncio
async def test_fake_provider_sequence_and_stop() -> None:
    provider = FakeMarketDataProvider(limit=3)
    ticks = [tick async for tick in provider.stream()]
    assert [tick["sequence"] for tick in ticks] == [0, 1, 2]
    await provider.stop()
    assert [tick async for tick in provider.stream()] == []
