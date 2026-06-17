from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.localization.pose_manager import subscribe_poses

router = APIRouter(tags=["websocket"])


@router.websocket("/ws/poses")
async def ws_poses(websocket: WebSocket):
    await websocket.accept()
    try:
        async for pose_update in subscribe_poses():
            await websocket.send_json(pose_update)
    except WebSocketDisconnect:
        pass
