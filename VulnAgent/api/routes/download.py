from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/download/{filename}")
def download_file(filename: str):
    path = os.path.join("outputs", filename)
    return FileResponse(path, filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")