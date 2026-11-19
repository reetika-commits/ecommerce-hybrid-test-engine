from playwright.async_api import Page

class HomePage:
    def __init__(self,page:Page):
        self.page=page
        self.url="https://www.demoblaze.com/index.html"
        self.home_locator=self.page.locator("#nava")
        self.contact_locator=self.page.locator("//*[@id='navbarExample']/ul/li[2]/a")
        self.about_us_locator=self.page.locator("//*[@id='navbarExample']/ul/li[3]/a")
        self.cart_locator=self.page.get_by_text("Cart")
        self.login_locator=self.page.locator("#login2")
        self.signup_locator=self.page.locator("#signin2")
        self.logout_locator=self.page.locator("#logout2")
        self.contact_modal_locator=self.page.get_by_role("dialog", name="New message")
        self.aboutus_modal_locator=self.page.get_by_role("heading", name="About us")
        self.cart_placeorder_locator=self.page.get_by_role("button", name=" Place Order")
        self.signup_btn_locator=self.page.get_by_role("button", name="Sign up")
        
        

        
    async def go_to_homepage(self)->None:
        await self.page.goto(self.url)

    async def navigate_to_login(self)->None:
       await self.login_locator.click()

    async def navigate_to_signup(self)->None:
        await self.signup_locator.click()

    async def navigate_to_aboutus(self)->None:
        await self.about_us_locator.click()

    async def navigate_to_cart(self)->None:
        await self.cart_locator.click()
            
    async def navigate_to_contact(self)->None:
        await self.contact_locator.click()

    async def navigate_to_homepage(self)->None:
        await self.home_locator.click()

    async def navigate_to_logout(self)->None:
        await self.logout_locator.click()