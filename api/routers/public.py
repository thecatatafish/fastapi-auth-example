from datetime import datetime

from fastapi import APIRouter
from starlette.responses import RedirectResponse

from ..schemas import PublicExample

router = APIRouter()


@router.get("/public", response_model=PublicExample)
def public_endpoint():
    return PublicExample(current_time=datetime.now().strftime("%H:%M:%S"))


@router.get("/")
def api_documentation():
    return RedirectResponse(url="/docs")
