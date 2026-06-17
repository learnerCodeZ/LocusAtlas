from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.api.v1 import router as v1_router
from app.api.v1.devices import router as devices_router
from app.api.v1.maps import router as maps_router
from app.api.v1.localization import router as localization_router
from app.api.ws import router as ws_router

app = FastAPI(title=settings.app_name, version=settings.version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router, prefix="/api/v1")
app.include_router(devices_router, prefix="/api/v1")
app.include_router(maps_router, prefix="/api/v1")
app.include_router(localization_router, prefix="/api/v1")
app.include_router(ws_router)


@app.on_event("startup")
async def startup():
    settings.map_storage_path.mkdir(parents=True, exist_ok=True)
    settings.pointcloud_upload_path.mkdir(parents=True, exist_ok=True)
