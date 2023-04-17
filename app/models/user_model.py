from uuid import UUID
from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(default=..., title="First Name", description="The user's first name")
    last_name: str = Field(default=..., title="Last Name", description="The user's last name")
    id: UUID = Field(default=..., title="ID", description="The user's ID")
