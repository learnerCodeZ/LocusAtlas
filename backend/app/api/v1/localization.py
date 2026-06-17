from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.localization.matcher import match_pointcloud
from app.services.localization.pose_manager import get_pose, get_all_poses

router = APIRouter(prefix="/localization", tags=["localization"])


class MatchRequest(BaseModel):
    device_id: str
    map_name: str
    pointcloud_path: str  # server-side path of uploaded fragment


class MatchResponse(BaseModel):
    device_id: str
    position: list[float]  # [x, y, z]
    orientation: list[float]  # [qx, qy, qz, qw]
    fitness: float
    rmse: float


@router.post("/match", response_model=MatchResponse)
async def localize_device(req: MatchRequest):
    result = match_pointcloud(req.map_name, req.pointcloud_path)
    if result is None:
        raise HTTPException(status_code=400, detail="Matching failed")
    return MatchResponse(
        device_id=req.device_id,
        position=result["position"],
        orientation=result["orientation"],
        fitness=result["fitness"],
        rmse=result["rmse"],
    )


@router.get("/pose/{device_id}")
async def device_pose(device_id: str):
    pose = get_pose(device_id)
    if pose is None:
        raise HTTPException(status_code=404, detail="No pose for device")
    return pose


@router.get("/poses")
async def all_poses():
    return get_all_poses()


@router.get("/relative/{device_a}/{device_b}")
async def relative_position(device_a: str, device_b: str):
    pose_a = get_pose(device_a)
    pose_b = get_pose(device_b)
    if not pose_a or not pose_b:
        raise HTTPException(status_code=404, detail="Device not found or no pose")
    pos_a = pose_a["position"]
    pos_b = pose_b["position"]
    dx, dy, dz = pos_b[0] - pos_a[0], pos_b[1] - pos_a[1], pos_b[2] - pos_a[2]
    distance = (dx**2 + dy**2 + dz**2) ** 0.5
    return {
        "from": device_a,
        "to": device_b,
        "offset": [dx, dy, dz],
        "distance": distance,
    }
