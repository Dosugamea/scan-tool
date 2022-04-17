import pytest
from doujinApi.api import DoujinApi


@pytest.mark.asyncio
async def test_search_book_by_name(client: DoujinApi) -> None:
    """
    Test the searchBookByName method of the DoujinApi class.
    """
    resp = await client.searchBookByName("魔法少女は深淵になにをみるか?")
    assert len(resp) == 1
