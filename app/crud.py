import jwt
import secrets
from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models import User
from app.schema import UserCreate, UserLogin


SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_user(db: Session, user: UserCreate):

    db_user = User(
        username=user.username,
        age=user.age,
        email=user.email,
        phone=user.phone
    )

    db.add(db_user)
    

    db.commit()

    db.refresh(db_user)

    return db_user


def get_users(db: Session):

    return db.query(User).all()


async def user_login(user, db):
    user_name  = user.username
    password = user.password

    data = {"user_name" : user_name,
            "password": password}

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp":expire,"type":"access"})

    

