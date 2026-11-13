import pytest_asyncio
from playwright.async_api import async_playwright
from api.auth_api import AuthAPI


@pytest_asyncio.fixture(scope="session")
async def api_context():
    async with async_playwright() as p:
        request_context=await p.request.new_context()
        try:
            yield request_context
        finally:
            await request_context.dispose()

@pytest_asyncio.fixture(scope="session")
async def auth_token(api_context):
    auth_api=AuthAPI(api_context)
    token= await auth_api.login()
    return token
