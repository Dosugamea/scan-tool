import asyncio
import sys
from os import environ
from os.path import dirname, join
from typing import Generator

import pytest_asyncio
from dotenv import load_dotenv
from doujinApi.api import DoujinApi

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


API_KEY = str(environ.get("API_KEY"))


@pytest_asyncio.fixture
async def client() -> DoujinApi:
    return DoujinApi(API_KEY)


@pytest_asyncio.fixture(scope="session")
def event_loop() -> Generator[asyncio.AbstractEventLoop, None, None]:
    """
    Creates an instance of the default event loop for the test session.
    """
    if sys.platform.startswith("win") and sys.version_info[:2] >= (3, 8):
        # Avoid "RuntimeError: Event loop is closed" on Windows
        # https://github.com/encode/httpx/issues/914
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
