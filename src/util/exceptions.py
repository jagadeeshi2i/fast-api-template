import logging
import traceback

from fastapi.exceptions import FastAPIError
from fastapi.responses import JSONResponse
from starlette.requests import Request

logger = logging.getLogger(__name__)


# TODO: Fix the exception handler
async def exception_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except FastAPIError as exc:
        logger.error({"error": type(exc).__name__, "message": exc, "at": traceback.format_exc()})
        return JSONResponse(content={"error": type(exc).__name__, "message": str(exc)}, status_code=400)
