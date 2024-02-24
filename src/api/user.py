from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_session
from src.schemas.user.user_req import UserReq
from src.services.user import UserService

router = APIRouter()


@router.post(
    "/users",
    responses={
        201: {"model": JSONResponse, "description": "User created successfully"},
        401: {"model": JSONResponse, "description": "Unauthorized"},
    },
    tags=["User"],
    summary="Add user",
)
async def create_user(
    user_req: UserReq = Body(description=""),
    session: AsyncSession = Depends(get_session),
):
    """
    Create a new user.

    Args:
        user_req (UserReq): The user request object containing user details.
        session (AsyncSession): The async session object for database operations.

    Returns:
        JSONResponse: The JSON response containing the status code and user data.
    """
    user = await UserService.create_user(user_req, session)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "User created successfully", "data": user},
    )
