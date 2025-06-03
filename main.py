from fastapi import FastAPI
from mini_RAG.routes import base

app = FastAPI()

app.include_router(base.base_router)