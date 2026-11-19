from playwright.async_api import expect
from pages.home_page import HomePage
from utilities.auth_helpers import goto_url,login,logout

async def test_goto_url(page):
    homepage=await goto_url(page)

    await expect(page).to_have_url("https://www.demoblaze.com/index.html")
    await expect(page).to_have_title("STORE", timeout=50000)

async def test_goto_contact(page):
    homepage=await goto_url(page)

    await homepage.navigate_to_contact()
    await expect(homepage.contact_modal_locator).to_be_visible(timeout=50000)

async def test_goto_aboutus(page):
    homepage=await goto_url(page)
    await homepage.navigate_to_aboutus()

    await expect(homepage.aboutus_modal_locator).to_be_visible(timeout=50000)

async def test_goto_cart(page):
    homepage=await goto_url(page)
    await homepage.navigate_to_cart()

    await expect(homepage.cart_placeorder_locator).to_be_visible(timeout=50000)

async def test_goto_signup(page):
    homepage=await goto_url(page)
    await homepage.navigate_to_signup()

    await expect(homepage.signup_btn_locator).to_be_visible(timeout=50000)

async def test_goto_login(page):
    homepage=await goto_url(page)

    log_in=await login(page, homepage,"reetikas", "admin")
    await expect(log_in.confirm_login_locator).to_be_visible(timeout=50000)

async def test_goto_Logout(page):
    homepage= await goto_url(page)
        
    await expect(page).to_have_title("STORE")
            
    log_in=await login(page, homepage,"reetikas", "admin")
    await expect(log_in.confirm_login_locator).to_be_visible()
        
    await logout(homepage)
    await expect(log_in.confirm_login_locator).not_to_be_visible()


