import logging

from app.db.user import UserCrud
from app.models.user import User
from app.schemas.user.user_req import UserReq

logger = logging.getLogger(__name__)


class UserService:
    @classmethod
    async def create_user(cls, user_req: UserReq, session) -> User:
        logger.info(f"Creating user with email: {user_req.email}")
        return await UserCrud.create_user(user_req, session)
