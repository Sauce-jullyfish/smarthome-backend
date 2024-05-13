from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    password = Column(String)
    permission = Column(Integer)


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    devices_name = relationship("DeviceName", back_populates="room")
    devices_type = relationship("DeviceType", back_populates="room")
    devices_history = relationship("DeviceHistory", back_populates="room")


class DeviceName(Base):
    __tablename__ = "devices_name"

    room_id = Column(Integer, ForeignKey('rooms.id'))
    a0 = Column(String)
    a1 = Column(String)
    a2 = Column(String)
    d0 = Column(String)
    d1 = Column(String)
    d2 = Column(String)

    room = relationship("Room", back_populates="devices_name")


class DeviceType(Base):
    __tablename__ = "devices_type"

    room_id = Column(Integer, ForeignKey('rooms.id'))
    a0 = Column(Integer)
    a1 = Column(Integer)
    a2 = Column(Integer)
    d0 = Column(Integer)
    d1 = Column(Integer)
    d2 = Column(Integer)

    room = relationship("Room", back_populates="devices_type")


class DeviceHistory(Base):
    __tablename__ = "devices_history"

    room_id = Column(Integer, ForeignKey('rooms.id'))
    a0 = Column(Integer)
    a1 = Column(Integer)
    a2 = Column(Integer)
    d0 = Column(Integer)
    d1 = Column(Integer)
    d2 = Column(Integer)
    time = Column(DateTime)

    room = relationship("Room", back_populates="devices_history")
