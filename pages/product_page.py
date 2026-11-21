from playwright.async_api import Page, expect

class ProductPage:
    def __init__(self, page:Page):
            self.page=page
            self.product_container_locator=self.page.locator("#tbodyid")
            self.product_card_locator=self.page.locator(".col-lg-4.col-md-6.mb-4")
            self.product_title_locator=self.page.locator("a.hrefch")
            # self.cat_phones_locator=self.page.get_by_role("link", name="Phones")
            # self.cat_laptops_locator=self.page.get_by_role("link", name="Laptops")
            # self.cat_monitors_locator=self.page.get_by_role("link", name="Monitors")
            parent_container_locator=self.page.locator(".product-content product-wrap clearfix product-deatil")
            self.selected_product_title_locator=self.page.locator(".name")
            self.selected_product_price_locator=self.page.locator(".price-container")
            self.selected_product_description_locator=self.page.locator("//div[@id='more-information']/p")
        

    async def select_product_category(self, category)->None:
          locator=self.page.get_by_role("link", name=category)
          await expect(self.product_container_locator).to_be_visible()
          await locator.click()

    async def get_all_products(self)->list:
        return await self.product_title_locator.all_text_contents()         


    # Samsung galaxy s6
    async def click_product(self, product):
        product_locator=self.page.get_by_role("link", name=product)
        await expect(self.product_container_locator).to_be_visible()
        await product_locator.click()

    async def get_selected_product_details_ui(self):
        title=await self.selected_product_title_locator.text_content()
        price=await self.selected_product_price_locator.text_content()
        description=await self.selected_product_description_locator.text_content()

        return(title, price, description)


