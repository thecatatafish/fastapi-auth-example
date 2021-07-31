from fastapi import APIRouter, Depends

from ..schemas import User, UserBase
from ..utilities import get_current_active_user

router = APIRouter()


@router.get("/users/me")
def get_current_user(current_user: User = Depends(get_current_active_user)):
    return UserBase(username=current_user.username)
