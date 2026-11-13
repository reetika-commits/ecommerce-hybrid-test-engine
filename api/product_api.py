

class ProductAPI:
    def __init__(self,api_context):
        self.aip_context=api_context
        self.products_endpoint="https://api.demoblaze.com/entries"
        

    async def retrieve_all_products(self):
        response=await self.aip_context.get(url=self.products_endpoint)
        return response