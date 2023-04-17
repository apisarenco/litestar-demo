from uuid import UUID
from app.models.user_model import User
from pathlib import Path


class UserService:
    def __init__(self):
        project_dir = Path(__file__).parents[2]
        self.__data_dir = project_dir / "data" / "users"
        self.__data_dir.mkdir(parents=True, exist_ok=True)

    def create_user(self, data: User):
        user_file = self.__data_dir / f"{data.id}.json"
        if user_file.exists():
            # raise ValueError(f"User with ID {data.id} already exists")
            return None
        user_file.write_text(data.json())
        return data

    def list_users(self) -> list[User]:
        return [User.parse_raw(user_file.read_text()) for user_file in self.__data_dir.glob("*.json")]

    def get_user(self, user_id: UUID):
        user_file = self.__data_dir / f"{user_id}.json"
        if not user_file.exists():
            raise ValueError(f"User with ID {user_id} does not exist")
        return User.parse_raw(user_file.read_text())

    def update_user(self, user_id: UUID, data: User):
        user_file = self.__data_dir / f"{user_id}.json"
        if not user_file.exists():
            raise ValueError(f"User with ID {user_id} does not exist")
        user_file.write_text(data.json())
        return data

    def delete_user(self, user_id: UUID):
        user_file = self.__data_dir / f"{user_id}.json"
        if not user_file.exists():
            raise ValueError(f"User with ID {user_id} does not exist")
        user_file.unlink()
