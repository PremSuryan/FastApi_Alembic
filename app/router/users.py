from typing import List

from fastapi import APIRouter
from fastapi import Depends,UploadFile,File

from sqlalchemy.orm import Session

from app.database import get_db
from app.schema import UserCreate, UserLogin
from app.crud import create_user
from app.crud import get_users, user_login,file_processing

router = APIRouter(prefix="/users")

async def fileValidation(files:List[UploadFile]=File(...)):
    all_files=[]
    for file in files:
        if file.filename.endswith(".xlsx"):
            all_files.append(file)
        continue

    return all_files


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


@router.post("/ws/file-processing")
async def fileProcessing(files:List[UploadFile]=File(...),
                         validationFile=Depends(fileValidation)):
    
    result = await file_processing(validationFile)
    return result
