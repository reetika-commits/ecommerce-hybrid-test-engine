class AuthAPI:
    def __init__(self, api_context):
        self.auth_api=api_context
        self.auth_endpoint="https://api.demoblaze.com/login"


    async def login(self):
        payload={"username":"reetikas","password":"YWRtaW4="}

        response=await self.auth_api.post(url=self.auth_endpoint, data=payload, timeout=15000)
        response_text = await response.text()
        auth_token = response_text.split(":")[1].strip().strip('"')
        return auth_token
