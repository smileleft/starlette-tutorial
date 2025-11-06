from contextlib import asynccontextmanager

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

def homepage(request):
  return PlainTextResponse('hello, world!')

def user_me(request):
  username = "Doctor Who"
  return PlainTextResponse('hello, %s!' % username)

def user(request):
  username = request.path_params['username']
  return PlainTextResponse('hello, %s!' % username)

async def websocket_endpoint(websocket):
  await websocket.accept()
  await websocket.send_text('Hello, websocket!')
  await websocket.close()

@asynccontextmanager
async def lifespan(app):
  print('Startup')
  yield
  print('Shutdown')

routes = [
  Route('/', homepage),
  Route('/user/me', user_me),
  Route('/user/{username}', user),
  WebsocketRoute('/ws', websocket_endpoint),
  Mount('/static', StaticFields(directory="static")),
]

app = Starlette(debug=True, routes=routes, lifespan=lifespan)
