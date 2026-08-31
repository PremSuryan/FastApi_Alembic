from pydantic import BaseModel


class UserCreate(BaseModel):

    username: str
    age: int
    email: str
    phone: str


class UserResponse(UserCreate):

    id: int

    class Config:
        from_attributes = True



class UserLogin(BaseModel):
    username : str
    password : str