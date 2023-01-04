# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn as uvicorn
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from rpn_source.rpn_controllor import RpnController

rpn_controller = RpnController()


async def rpn_operation(request):
    return await rpn_controller.rpn_operation(request)


routes = [
    Route('/operate', rpn_operation, methods=['POST']),
]
middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True,
               allow_methods=["*"],
               allow_headers=["*"])
]
app = Starlette(debug=True, routes=routes, middleware=middleware)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
