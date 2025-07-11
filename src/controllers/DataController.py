from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResponseSignals

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_conversion = 1048576 # 1 MB = 1024 * 1024 bytes

    # Validate the uploaded file type and size
    # Returns True if valid, False otherwise
    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, f'{ResponseSignals.FILE_TYPE_NOT_SUPPORTED.value} {ResponseSignals.FILE_SUPPORTED_TYPES.value} {self.app_settings.FILE_ALLOWED_TYPES}'
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_conversion:
            return False, f'{ResponseSignals.FILE_EXCEEDS_LIMIT.value} {self.app_settings.FILE_MAX_SIZE} MB'

        return True, ResponseSignals.FILE_UPLOAD_SUCCESS.value
