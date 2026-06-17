import asyncio
import time
from collections import defaultdict

# In-memory pose store for MVP: device_id -> pose data
_poses: dict[str, dict] = {}
_subscribers: list[asyncio.Queue] = []


def update_pose(device_id: str, position: list[float], orientation: list[float], **extra) -> dict:
    pose = {
        "device_id": device_id,
        "position": position,
        "orientation": orientation,
        "timestamp": time.time(),
        **extra,
    }
    _poses[device_id] = pose
    # Notify subscribers
    for q in _subscribers:
        q.put_nowait(pose)
    return pose


def get_pose(device_id: str) -> dict | None:
    return _poses.get(device_id)


def get_all_poses() -> dict[str, dict]:
    return _poses


async def subscribe_poses():
    """Async generator yielding pose updates for WebSocket."""
    q = asyncio.Queue()
    _subscribers.append(q)
    try:
        while True:
            pose = await q.get()
            yield pose
    finally:
        _subscribers.remove(q)
