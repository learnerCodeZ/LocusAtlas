from fastapi import APIRouter, Depends, HTTPException, status
from app.core.config import settings
from app.models.device import DeviceCreate, DeviceResponse, DeviceType

router = APIRouter(prefix="/devices", tags=["devices"])

# In-memory store for MVP; replace with DB later
_devices: dict[str, dict] = {}


@router.post("/", response_model=DeviceResponse, status_code=status.HTTP_201_CREATED)
async def register_device(data: DeviceCreate):
    if data.id in _devices:
        raise HTTPException(status_code=409, detail="Device already registered")
    token = f"{settings.auth_secret}_{data.id}"
    device = {
        "id": data.id,
        "name": data.name,
        "type": data.type,
        "token": token,
        "online": False,
    }
    _devices[data.id] = device
    return DeviceResponse(**device)


@router.get("/", response_model=list[DeviceResponse])
async def list_devices():
    return [DeviceResponse(**d) for d in _devices.values()]


@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(device_id: str):
    if device_id not in _devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return DeviceResponse(**_devices[device_id])


@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_device(device_id: str):
    if device_id not in _devices:
        raise HTTPException(status_code=404, detail="Device not found")
    del _devices[device_id]
