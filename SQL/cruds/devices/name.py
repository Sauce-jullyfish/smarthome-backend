from sqlalchemy.orm import Session
from ... import models, schemas


def get_device(db: Session, device_id: int):
    return db.query(models.Device).filter(models.Device.id == device_id).first()


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(**device.model_dump())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def update_device(db: Session, device_id: int, update_fields: dict):
    db_device = db.query(models.Device).filter(
        models.Device.id == device_id).first()
    if db_device:
        for key, value in update_fields.items():
            setattr(db_device, key, value) if value else None
        db.commit()
        db.refresh(db_device)
    return db_device


def delete_device(db: Session, device_id: int):
    db_device = db.query(models.Device).filter(
        models.Device.id == device_id).first()
    if db_device:
        db.delete(db_device)
        db.commit()
    return db_device
