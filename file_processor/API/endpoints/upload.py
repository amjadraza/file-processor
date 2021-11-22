import shutil
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException


from fastapi import FastAPI, UploadFile, File
from pathlib import Path
from tempfile import NamedTemporaryFile
import os
router = APIRouter()

FILES_DATA_DIR = '../../data_dir'
os.makedirs(os.path.join('.', FILES_DATA_DIR), exist_ok=True)

@router.post("/")
async def create_upload_files(id: int, files: List[UploadFile] = File(...)):
    id_dir = os.path.join(FILES_DATA_DIR, str(id))
    os.makedirs(id_dir, exist_ok=True)
    file_names = [file.filename for file in files]
    for file_name in file_names:
        destination = os.path.join(id_dir, file_name)
        try:
            with destination.open("wb") as buffer:
                shutil.copyfileobj(file_name, buffer)
        finally:
            file_name.close()

    return {"filenames": [file.filename for file in files]}
