from sqlalchemy.orm import Session
from .. import models, schemas


def get_room(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.id == room_id).first()


def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def update_room(db: Session, room_id: int, update_fields: dict):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        for key, value in update_fields.items():
            setattr(db_room, key, value) if value else None
        db.commit()
        db.refresh(db_room)
    return db_room


def delete_room(db: Session, room_id: int):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room
