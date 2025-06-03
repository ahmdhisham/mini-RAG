from fastapi import FastAPI, APIRouter
import os

base_router = APIRouter(
    prefix='/api/v1',
    tags=['api_v1'],
)

@base_router.get("/")
async def welcome():
    return {"app_name":app_name,
            "app_ver":app_ver,
            }