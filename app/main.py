from fastapi import FastAPI, APIRouter, Depends
import uvicorn
from pydantic import BaseModel


from fastapi import FastAPI
from app.router.users import router

app = FastAPI()

app.include_router(router)



if __name__ == "__main__":
    uvicorn.run(app, host="127.1.0.0", port=8000)

# claude api key --> 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