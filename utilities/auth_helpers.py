from pages.home_page import HomePage
from pages.login_page import Login
from playwright.async_api import expect

async def goto_url(page):
    home_page=HomePage(page)
    await home_page.go_to_homepage()
    return home_page

async def login(page,home_page,username,password):
    await home_page.navigate_to_login()
    log_in=Login(page)
    await log_in.enter_username(username)
    await log_in.enter_password(password)
    await log_in.click_login_btn()
    return log_in

async def logout(home_page):
    await home_page.navigate_to_logout()