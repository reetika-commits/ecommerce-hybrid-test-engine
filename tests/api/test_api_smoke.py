from playwright.async_api import async_playwright

async def test_demoblaze_entries(api_context):
    
    url="https://api.demoblaze.com/entries"

    response=await api_context.get(url=url)
    response_data=await response.json()

    #assert -> status==200, userId == 1, id == 1, title is not empty, body is not empty
    assert response.status==200
    product = next(
    (item for item in response_data["Items"] if item["id"] == 1),
    None
    )

    assert product is not None, "Product ID 1 not found"
    assert product["title"].strip()
            
     