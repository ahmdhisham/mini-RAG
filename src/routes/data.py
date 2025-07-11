from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
import os
from src.helpers import get_settings, Settings
from src.controllers import DataController

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, 
                    app_settings: Settings = Depends(get_settings)):
    
    # validate the file type and size
    is_valid, result_signal = DataController().validate_uploaded_file(file = file)
    
    if not is_valid:
        return JSONResponse(
            status_code = status.HTTP_400_BAD_REQUEST,
            content = {
                "Signal":result_signal
            }
        )