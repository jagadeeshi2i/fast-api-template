from sqlalchemy.ext.asyncio import AsyncSession
from src.db.base import Crud
from src.models.user import User


class UserCrud(Crud):
    id_column = "uuid"

    @classmethod
    async def create_user(cls, user_req, session: AsyncSession):
        return await super().create(User, user_req, session)
