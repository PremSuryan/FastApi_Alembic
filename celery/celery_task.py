
from pathlib import Path
from openpyxl import load_workbook

from app.celery_app import celery_app


@celery_app.task(
    bind=True,
    autoretry_for=(OSError,),
    retry_backoff=True,
    retry_kwargs={"max_retries": 3},
)
def process_excel(self, file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Excel file not found: {file_path}"
        )

    workbook = load_workbook(
        filename=path,
        read_only=True,
        data_only=True,
    )

    try:
        sheet = workbook.active
        row_count = 0

        for row in sheet.iter_rows(
            min_row=2,
            values_only=True,
        ):
            if all(value is None for value in row):
                continue

            # Real application:
            # validate the row
            # transform its values
            # write to PostgreSQL in batches

            row_count += 1

        return {
            "status": "completed",
            "rows_processed": row_count,
        }

    finally:
        workbook.close()