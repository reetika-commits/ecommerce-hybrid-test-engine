from utilities import assertions as a
from api.product_api import ProductAPI
from api.cart_api import CartAPI

async def test_product_listing(api_context):
    await items_details(api_context)

async def test_validate_cart_items(api_context,add_item_to_cart):
    cart_api=CartAPI(api_context)
    response=await cart_api.retrieve_cart(add_item_to_cart["cookie"])
    await a.assert_status_code(response,200)
    response_data=await response.json()
    assert response_data["Items"]
    await a.assert_is_list(response_data,"Items")
    items=response_data["Items"]
    product=next((item for item in items if item["id"]==add_item_to_cart["id"]), None)
    assert product is not None, "The product was not added to the cart"
    assert product["prod_id"]==add_item_to_cart["prod_id"], "Cart item contains an unexpected product ID"


async def test_delete_cart_item(api_context,auth_token):
    cart_payload=await add_cart_item(api_context,auth_token)
    await delete_cart_item(api_context,auth_token, cart_payload)


async def add_cart_item(api_context,auth_token):
    cart_api=CartAPI(api_context)
    cart_payload=await cart_api.add_product_to_cart(5,auth_token)
    #helper function
    product = await view_cart_retrival(cart_api,auth_token, cart_payload)

    assert product is not None, "The product was not added to the cart"
    assert product["prod_id"]==cart_payload["prod_id"], "Cart item contains an unexpected product ID"

    return cart_payload

async def view_cart_retrival(cart_api,auth_token, cart_payload):
    response=await cart_api.retrieve_cart(auth_token)
    response_data=await response.json()
    
    await a.assert_status_code(response,200)
    await a.assert_is_list(response_data,"Items")

    items=response_data["Items"]
    product=next((item for item in items if item["id"]==cart_payload["id"]), None)
    
    return product


async def items_details(api_context):
    product_api= ProductAPI(api_context)
    
    response= await product_api.retrieve_all_products()

    response_data=await response.json()

    await a.assert_status_code(response,200)
    items=response_data["Items"]
    await a.assert_is_list(response_data,"Items")
    assert all("title" in item for item in items), "One item is missing 'title'"

    invalid_product=[item for item in items if not item["title"].strip()]
    assert not invalid_product, f"Products with empty 'title' are {[item['id'] for item in invalid_product]}"
    
async def delete_cart_item(api_context,auth_token, cart_payload):
    delete_api=CartAPI(api_context)
    response=await delete_api.delete_item(cart_payload["id"])
    response_text=await response.text()
    await a.assert_status_code(response,200)
    assert response_text=='"Item deleted."\n' , f"Item was not deleted. {response_text}"

    product=await view_cart_retrival(delete_api,auth_token,cart_payload)

    assert product is None, f"Product was not deleted"

