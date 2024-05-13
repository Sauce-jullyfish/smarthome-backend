from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing_extensions import Literal


class UserBase(BaseModel):
    user_name: str
    permissions: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class RoomBase(BaseModel):
    name: str


class RoomCreate(RoomBase):
    pass


class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True


class DeviceBase(BaseModel):
    room_id: int
    a0: Optional[Literal["DHT11", "MQ2", "MQ135", None]] = None
    a1: Optional[Literal["DHT11", "MQ2", "MQ135", None]] = None
    a2: Optional[Literal["DHT11", "MQ2", "MQ135", None]] = None
    d0: Optional[Literal["LED", "PIR", None]] = None
    d1: Optional[Literal["LED", "PIR", None]] = None
    d2: Optional[Literal["LED", "PIR", None]] = None


class DeviceCreate(DeviceBase):
    pass


class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True


class DeviceTypeBase(BaseModel):
    room_id: int
    a0: Optional[int | None] = None
    a1: Optional[int | None] = None
    a2: Optional[int | None] = None
    d0: Optional[int | None] = None
    d1: Optional[int | None] = None
    d2: Optional[int | None] = None


class DeviceTypeCreate(DeviceTypeBase):
    pass


class DeviceType(DeviceTypeBase):
    id: int

    class Config:
        orm_mode = True


class DeviceHistoryBase(BaseModel):
    room_id: int
    a0: Optional[int | float | None] = None
    a1: Optional[int | float | None] = None
    a2: Optional[int | float | None] = None
    d0: Optional[int | None] = None
    d1: Optional[int | None] = None
    d2: Optional[int | None] = None
    time: datetime


class DeviceHistoryCreate(DeviceHistoryBase):
    pass


class DeviceHistory(DeviceHistoryBase):
    id: int

    class Config:
        orm_mode = True
