from fastapi import FastAPI, APIRouter, Depends, UploadFile
import os
from src.helpers.config import get_settings, Settings
from src.controllers.DataControllers import DataController

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str, file: UploadFile, 
                    app_settings: Settings = Depends(get_settings)):
    # validate the file type and size
    is_valid, return_signal = DataController().validate_uploaded_file(file = file)
    
    return {"Signal" : return_signal}