from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse

from rpn_source.rpn_service import RpnService

rpn_service=RpnService()
class RpnController():

     async def rpn_operation(self,request):
        body = await request.json()
        stack= await rpn_service.rpn_operation(body['stack'],body['operand'])
        print(stack)
        response = JSONResponse(stack)
        print(response)
        return  response


