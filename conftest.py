import pytest_asyncio
from playwright.async_api import async_playwright
from api.auth_api import AuthAPI
from api.cart_api import CartAPI



@pytest_asyncio.fixture(scope="session")
async def api_context():
    '''Fixture to create setup for API test'''
    async with async_playwright() as p:
        request_context=await p.request.new_context()
        try:
            yield request_context
        finally:
            await request_context.dispose()

@pytest_asyncio.fixture(scope="session")
async def auth_token(api_context):
    '''Fixture to fetch authentication token during login for API test'''
    auth_api=AuthAPI(api_context)
    token= await auth_api.login()
    return token

@pytest_asyncio.fixture(scope="function")
async def add_item_to_cart(api_context, auth_token):
    '''FIxture to add item in cart and delete added item in teardown for API test'''
    cart_api=CartAPI(api_context)
    payload= await cart_api.add_product_to_cart(4,auth_token)
    try:
        yield payload
    finally:
        response=await cart_api.delete_item(payload["id"])

####################################################################

@pytest_asyncio.fixture(scope="session")
async def browser():
    ''' Fixture to initialise browser for UI test'''
    browser=None
    async with async_playwright() as p:
        browser=await p.firefox.launch(headless=False)
        try:
            yield browser
        finally:
            if browser != None:
                await browser.close()

@pytest_asyncio.fixture(scope="function")
async def context(browser):
    ''' Fixture to initialise context for UI test'''
    context=None
    context=await browser.new_context()
    try:
        yield context
    finally:
        if context!=None:
            await context.close()

@pytest_asyncio.fixture(scope="function")
async def page(context):
    ''' Fixture to initialise page for UI test'''
    
    page=None
    if context is not  None:
        page=await context.new_page()
    try:
        yield page
    finally:
        if page is not None:
            await page.close()
        

