import pytest
from pages.product_page import ProductPage
from playwright.async_api import Page, expect
from utilities.auth_helpers import goto_url,login,logout

@pytest.mark.parametrize(
    "ui_category, api_category",
    [
        ("Phones", "phone"),
        ("Laptops", "notebook"),
        ("Monitors", "monitor")
    ]
)
async def test_category(page:Page,ui_category,api_category ):
    homepage=await goto_url(page)
    product_list = await get_product_list(page, homepage, ui_category)
    try:
        assert product_list, "No products returned"
        print(product_list)
        assert all(item["cat"] == api_category for item in product_list)
    finally:
        print(product_list)
        await logout(homepage)

@pytest.mark.parametrize("category",('Laptops','Monitors','Phones'))
async def test_all_product_titles(page,category):
    homepage=await goto_url(page)
    response_product_list=await get_product_list(page,homepage,category)
    try:
        productpage=ProductPage(page)
        ui_product_list=await productpage.get_all_products()
        title_list=[item["title"] for item in response_product_list]
        assert ui_product_list ==title_list
    finally:
        await logout(homepage)

async def get_product_list(page,homepage,category):
    await login(page,homepage,"reetikas", "admin")
    
    productpage=ProductPage(page)
    async with page.expect_response("**/bycat") as response:
        await productpage.select_product_category(category)
        
    response_data=await response.value
    product_list=await response_data.json()
    return product_list["Items"]

