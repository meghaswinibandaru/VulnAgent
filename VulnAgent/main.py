from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from api.routes import upload, download

app = FastAPI(title="Vuln Agent")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/ui", StaticFiles(directory="ui", html=True), name="ui")

app.include_router(upload.router)
app.include_router(download.router)