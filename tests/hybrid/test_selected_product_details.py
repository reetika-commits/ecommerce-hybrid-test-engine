import pytest
from pages.product_page import ProductPage
from playwright.async_api import Page, expect
from utilities.auth_helpers import goto_url,login,logout
from api.product_api import ProductAPI

category_mapping = {
    "Phones": "phone",
    "Laptops": "notebook",
    "Monitors": "monitor"
}

@pytest.mark.parametrize("category",('Phones','Laptops','Monitors'))
async def test_selected_product_details(page:Page, api_context, category):
    api_category = category_mapping[category]
    #load homepage
    homepage=await goto_url(page)
    productapi=ProductAPI(api_context)
    productpage=ProductPage(page)
    #login
    log_in=await login(page,homepage,"reetikas", "admin")
    try:
        #select category
        await productpage.select_product_category(category)
        #retrive all products of given category and get id and title of 1st product
        product_id, product_title=await get_selected_product_id_title(await productapi.retrieve_all_products_by_category(api_category))
        #click on first product in UI
        await productpage.click_product(product_title)
        await expect(page).to_have_url(f"https://www.demoblaze.com/prod.html?idp_={product_id}")
        #get selected product details for API and UI
        product_details_api=await productapi.get_selected_product_details_API(product_id)
        product_details_ui=await productpage.get_selected_product_details_ui()

        compare(product_details_api,product_details_ui)
    finally:
        await logout(homepage)

    
def compare(product_details_api,product_details_ui):
   assert (product_details_ui[0]==product_details_api['title'])
   assert (product_details_api['price']==normalize_price(product_details_ui[1]))
   assert (product_details_ui[2]==product_details_api['desc'])


def normalize_price(price)->float:
    return float(((price).replace("*includes tax","")).replace("$",""))
    
async def get_selected_product_id_title(response_data):
    response_product_list=response_data["Items"]
    assert response_product_list, "Product response is empty"
    id_title_dict={item["id"]:item["title"] for item in response_product_list}
    return next(iter(id_title_dict.items()))

