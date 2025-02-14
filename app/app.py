# from connector import connect

from fastapi import FastAPI, Request

app = FastAPI(title="Jeudis Givres API", version="1.0.0")

@app.get("/")
def root(request: Request):
    endpoints = {
        "To see current ladder [GET]": f"{request.url}ladder",
    }

    return {
        "API_status": "c est bon ca marche",
        "API Documentation": f"{request.url}docs",
        "avalaible endpoints": endpoints,
    }
