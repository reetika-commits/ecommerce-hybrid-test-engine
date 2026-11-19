from utilities.auth_helpers import goto_url, login, logout
from playwright.async_api import expect, Page

async def test_login_valid(page:Page):
    homepage= await goto_url(page)

    await expect(page).to_have_title("STORE")
    
    log_in=await login(page, homepage,"reetikas", "admin")

    await expect(log_in.confirm_login_locator).to_be_visible()
    await expect(log_in.confirm_login_locator).to_have_text("Welcome reetikas",timeout=5000)

async def test_login_invalid_username(page:Page):
    homepage= await goto_url(page)
    
    await expect(page).to_have_title("STORE")
    
    async with page.expect_event("dialog") as dialog_info:
        log_in=await login(page, homepage,"wrong_username", "admin")
        dialog=await dialog_info.value

        assert dialog.type=="alert"
        print(dialog.message)
        assert dialog.message=="User does not exist."
        await dialog.accept()

async def test_login_invalid_password(page:Page):
    homepage= await goto_url(page)
        
    await expect(page).to_have_title("STORE")
        
    async with page.expect_event("dialog") as dialog_info:
        log_in=await login(page, homepage,"reetikas", "wrong_password")
        dialog=await dialog_info.value

        assert dialog.type=="alert"
        assert dialog.message=='Wrong password.'
        await dialog.accept()

async def test_logout(page:Page):
    homepage= await goto_url(page)
    
    await expect(page).to_have_title("STORE")
        
    log_in=await login(page, homepage,"reetikas", "admin")
    await expect(log_in.confirm_login_locator).to_be_visible()
    
    await logout(homepage)
    await expect(log_in.confirm_login_locator).not_to_be_visible()

    