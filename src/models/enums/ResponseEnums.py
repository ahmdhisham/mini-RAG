from enum import Enum

class ResponseSignals(Enum):
    
    FILE_VALIDATE_SUCCESS = "File Validate Successfuly"
    FILE_TYPE_NOT_SUPPORTED = "File type is Not Supported"
    FILE_EXCEEDS_LIMIT = "File Size Exceeds Limit "
    FILE_UPLOAD_SUCCESS = "File was Uploaded Successfully"
    FILE_UPLOAD_FAIL = "File Upload Failed"