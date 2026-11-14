
import uuid

class CartAPI:
    def __init__(self,api_context):
           self.api_context=api_context
           
           self.addcart_endpoint="https://api.demoblaze.com/addtocart"
           self.viewcart_endpoint="https://api.demoblaze.com/viewcart"
           self.deleteitem_endpoint="https://api.demoblaze.com/deleteitem"

    async def add_product_to_cart(self,prod_id,auth_token):
          unique_id=await self.generate_Unique_id()
          payload= {"id":unique_id,"cookie":auth_token,"prod_id":prod_id,"flag":True}
          response=await self.api_context.post(url=self.addcart_endpoint, data=payload)

          return payload

    async def generate_Unique_id(self):
          unique_id=uuid.uuid4().__str__()
          return unique_id

    async def retrieve_cart(self, auth_token):
          payload={"cookie":auth_token,"flag":True}
          response=await self.api_context.post(url=self.viewcart_endpoint, data=payload)

          return response

    async def delete_item(self,unique_id):
      payload={"id":unique_id}
      response=await self.api_context.post(url=self.deleteitem_endpoint, data=payload)
      return response