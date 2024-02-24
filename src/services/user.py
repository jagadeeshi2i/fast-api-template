import logging

from src.db.user import UserCrud
from src.models.user import User
from src.schemas.user.user_req import UserReq

logger = logging.getLogger(__name__)


class UserService:
    """
    Service class for user operations.
    """

    @classmethod
    async def create_user(cls, user_req: UserReq, session) -> User:
        """
        Create a new user.

        Args:
            user_req (UserReq): The user request object containing user details.
            session: The database session.

        Returns:
            User: The created user object.
        """
        logger.info(f"Creating user with email: {user_req.email}")
        return await UserCrud.create_user(user_req, session)
