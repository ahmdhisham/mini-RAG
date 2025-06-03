path_env = "mini_RAG/.env"
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(path_env)

from mini_RAG.routes import base

app = FastAPI()

app.include_router(base.base_router)