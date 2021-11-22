"""
.. module:: main
   :synopsis: Main
.. moduleauthor:: MA Raza

This file is the entry point of API.

Example

    >>> uvicorn file_processor.API.main:app --reload

Todo:
    * Add more details/functionalities
    * Convert the Simple API into production ready API
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import os
import pandas as pd
from fastapi import FastAPI
import shutil
from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from fastapi import FastAPI, UploadFile, File , Query
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Optional
from file_processor.main import filter_json_date
from loguru import logger


FILES_DATA_DIR = 'data_dir/'
os.makedirs(os.path.join('.', FILES_DATA_DIR), exist_ok=True)

description = """
A Small App to render the filtered data from Text Files. 🚀

## Files

Upload text files with records in below format

`2020-12-04T11:14:23Z jane.doe@email.com 2f31eb2c-a735-4c91-a122-b3851bc87355`

## Date Time Ranges

Users will be able to provide:

* start_datetime: Start Datetime range in UTC format
* end_datetime: End Datetime range in UTC format
"""

# Define the App
app = FastAPI(openapi_url="/api/v1/openapi.json",
              title="File Processor",
              description=description,
              version="0.1.0",
              contact={
                "name": "MA Raza",
                "url": "https://github.com/amjadraza",
                "email": "amjadraza24@gmail.com",
                })

@app.post("/process_file/")
async def create_upload_file(
                             start_datetime: Optional[str]= Query('2000-01-01T17:25:49Z',
                                                  alias="Start DateTime",
                                                  title="Start datetime UTC Format",
                                                  ),
                             end_datetime: Optional[str]= Query('2000-01-06T06:27:36Z',
                                                  alias="End DataTie",
                                                  title="End datetime UTC Format",
                                                  ),
                             uploaded_file: UploadFile = File(...)):

    """
    API end point to run the filter. Users can upload the text file and datetime ranges t filter
    Args:
        start_datetime: Start Datetime range in UTC format
        end_datetime: End Datetime range in UTC format
        uploaded_file: text File

    Returns: Json format response
    """

    file_location = f"{FILES_DATA_DIR}/{uploaded_file.filename}"
    # Reading and saving the file
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(uploaded_file.file, file_object)

    logger.info(f'File copied at: {file_location}')
    # processing the file
    response = filter_json_date(file_location, start_datetime, end_datetime)
    logger.info(response)

    return response
