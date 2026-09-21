from pydantic import EmailStr, Field
from src.schemas.base import PydanticBaseModel


class UserReq(PydanticBaseModel):
    """
    Represents a user request.

    Attributes:
        email (EmailStr): User email.
        first_name (str): User first name.
        last_name (str): User last name.
        password (str): User password.
        role (str | None): User role.
    """

    email: EmailStr = Field(..., description="User email")
    first_name: str = Field(..., description="User first name")
    last_name: str = Field(..., description="User last name")
    password: str = Field(..., description="User password")
    role: str | None = Field(None, description="User role")


UserReq.model_rebuild()
