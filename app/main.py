from fastapi import FastAPI, APIRouter, Depends
import uvicorn
from pydantic import BaseModel


from fastapi import FastAPI
from app.router.users import router

app = FastAPI()

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run(app, host="127.1.0.0", port=8000)
