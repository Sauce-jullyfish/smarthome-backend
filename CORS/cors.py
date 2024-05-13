from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class CORS:
    @classmethod
    def add_cors(cls, app: FastAPI, origins: list = ["*"]):
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
