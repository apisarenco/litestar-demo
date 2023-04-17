from litestar import Litestar

from app.controllers.user_controller import UserController

app = Litestar(route_handlers=[UserController])
