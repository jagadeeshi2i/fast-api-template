from typing import Dict, List, Optional

from pydantic import EmailStr, Field

from app.schemas.base import PydanticBaseModel


class UserReq(PydanticBaseModel):
    email: EmailStr = Field(..., description="User email")
    first_name: str = Field(..., description="User first name")
    last_name: str = Field(..., description="User last name")
    password: str = Field(..., description="User password")
    role: Optional[str] = Field(None, description="User role")


UserReq.model_rebuild()
