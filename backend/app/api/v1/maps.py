from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.services.map.processor import preprocess_pointcloud
from app.core.config import settings

router = APIRouter(prefix="/maps", tags=["maps"])


@router.post("/upload")
async def upload_map(
    name: str = Form(...),
    file: UploadFile = File(...),
):
    save_path = settings.map_storage_path / name
    save_path.mkdir(parents=True, exist_ok=True)

    file_path = save_path / file.filename
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)

    result = preprocess_pointcloud(str(file_path))
    return {
        "name": name,
        "filename": file.filename,
        "preprocessed": result["output_path"],
        "points_original": result["points_original"],
        "points_processed": result["points_processed"],
    }


@router.get("/")
async def list_maps():
    maps = []
    for p in settings.map_storage_path.iterdir():
        if p.is_dir():
            maps.append({"name": p.name})
    return maps
