from playwright.async_api import Page
class Login:
    def __init__(self, page:Page):
        self.page=page
        self.modal_frame=self.page.locator("#logInModal")
        self.username_locator= self.modal_frame.locator("#loginusername")
        self.password_locator=self.modal_frame.locator("#loginpassword")
        self.login_btn_locator=self.modal_frame.get_by_role("button",name="Log in")
        self.confirm_login_locator=self.page.locator("#nameofuser")
        

    async def enter_username(self, username:str):
        await self.username_locator.fill(username)

    async def enter_password(self, password:str):
        await self.password_locator.fill(password)

    async def click_login_btn(self):
        await self.login_btn_locator.click()