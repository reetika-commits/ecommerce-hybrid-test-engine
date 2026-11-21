

class ProductAPI:
    def __init__(self,api_context):
        self.api_context=api_context
        self.products_endpoint="https://api.demoblaze.com/entries"
        self.product_bycat_endpoint="https://api.demoblaze.com/bycat"
        self.selected_product_endpoint="https://api.demoblaze.com/view"
        

    async def retrieve_all_products(self):
        response=await self.aip_context.get(url=self.products_endpoint)
        return response

    async def retrieve_all_products_by_category(self,category):
        payload={"cat":category}
        response=await self.api_context.post(url=self.product_bycat_endpoint,data=payload)
        return await response.json()
    
    async def get_selected_product_details_API(self,product_id):
        payload={"id":product_id}
        response=await self.api_context.post(self.selected_product_endpoint, data=payload)
        return await response.json()