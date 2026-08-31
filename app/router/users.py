from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.schema import UserCreate, UserLogin
from app.crud import create_user
from app.crud import get_users, user_login

router = APIRouter(prefix="/users")


@router.post("/")
def add_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(db, user)


@router.get("/")
def read_users(
    db: Session = Depends(get_db)
):

    return get_users(db)


@router.post("/")
async def login(
    user_details:UserLogin,
    db : Session = Depends(get_db)
):
    result = await user_login(user_details,db)
    return result