from uuid import UUID
from litestar import Controller, get, post, put, delete
from litestar.di import Provide
from app.models.user_model import User
from app.services.user_service import UserService


class UserController(Controller):
    path = "/users"
    dependencies = {"user_service": Provide(UserService)}

    @post()
    async def create_user(self, data: User, user_service: UserService) -> User:
        created = user_service.create_user(data)
        return created

    @get()
    async def list_users(self, user_service: UserService) -> list[User]:
        users = user_service.list_users()
        return users

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID, data: User, user_service: UserService) -> User:
        if user_id != data.id:
            raise ValueError("user_id does not match data.id")
        updated = user_service.update_user(user_id, data)
        return updated

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID, user_service: UserService) -> User:
        user = user_service.get_user(user_id)
        return user

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID, user_service: UserService) -> None:
        user_service.delete_user(user_id)
