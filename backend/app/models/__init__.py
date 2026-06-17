from enum import StrEnum
from pydantic import BaseModel


class DeviceType(StrEnum):
    HOLOLENS2 = "hololens2"
    KINECT = "kinect"
    OTHER = "other"


class DeviceCreate(BaseModel):
    id: str
    name: str
    type: DeviceType


class DeviceResponse(BaseModel):
    id: str
    name: str
    type: DeviceType
    token: str
    online: bool
