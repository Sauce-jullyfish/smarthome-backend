from fastapi import FastAPI
from CORS import CORS
from SQL import models

# 初始化資料庫
models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

CORS.add_cors(app)
