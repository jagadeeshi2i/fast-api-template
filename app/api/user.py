from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session
from app.schemas.user.user_req import UserReq
from app.services.user import UserService

router = APIRouter()


@router.post(
    "/users",
    responses={
        201: {"model": JSONResponse, "description": "User created successfully"},
        401: {"model": JSONResponse, "description": "Unauthorized"},
    },
    tags=["User"],
    summary="Add user"

)
async def create_user(user_req: UserReq = Body(description=""), session: AsyncSession = Depends(get_session)):
    user = await UserService.create_user(user_req, session)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "User created successfully", "data": user})