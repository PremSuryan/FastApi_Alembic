from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.requests import Request
from pydantic import BaseModel
import asyncio


app = FastAPI()

class Number(BaseModel):
    number : int


@app.post('/')
def number_processing(numb:Number):

    def generator():
        for i in range(1,numb.number+1):
            yield i

    return StreamingResponse(
        generator(),
        media_type='text/plain'
    )


#ASYNC METHOD

@app.post("/")
async def number_processing(numb: Number):

    async def stream():
        for i in range(1, numb.number + 1):
            yield f"{i}\n"
            await asyncio.sleep(1)

    return StreamingResponse(stream(), media_type="text/plain")

    # if it is json
    # return StreamingResponse(stream(), media_type="application/json")
