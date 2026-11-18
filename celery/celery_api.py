from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from celery.result import AsyncResult

from app.celery_app import celery_app
from app.tasks import process_excel

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload", status_code=202)
async def upload_excel(
    file: UploadFile = File(...),
):
    if not file.filename or not file.filename.lower().endswith(
        ".xlsx"
    ):
        raise HTTPException(
            status_code=400,
            detail="Upload an .xlsx file",
        )

    file_path = UPLOAD_DIR / f"{uuid4().hex}.xlsx"

    try:
        with file_path.open("wb") as destination:
            while chunk := await file.read(1024 * 1024):
                destination.write(chunk)
    finally:
        await file.close()

    task = process_excel.delay(str(file_path.resolve()))

    return {
        "message": "Excel processing queued",
        "task_id": task.id,
        "status_url": f"/tasks/{task.id}",
    }


@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    task = AsyncResult(task_id, app=celery_app)

    response = {
        "task_id": task_id,
        "status": task.status,
    }

    if task.successful():
        response["result"] = task.result

    elif task.failed():
        response["error"] = "Task processing failed"

    return response