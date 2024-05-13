from sqlalchemy.orm import Session
from ... import models, schemas


def get_device_history(db: Session, device_history_id: int):
    return db.query(models.DeviceHistory).filter(models.DeviceHistory.id == device_history_id).first()


def create_device_history(db: Session, device_history: schemas.DeviceHistoryCreate):
    db_device_history = models.DeviceHistory(**device_history.model_dump())
    db.add(db_device_history)
    db.commit()
    db.refresh(db_device_history)
    return db_device_history


def update_device_history(db: Session, device_history_id: int, update_fields: dict):
    db_device_history = db.query(models.DeviceHistory).filter(
        models.DeviceHistory.id == device_history_id).first()
    if db_device_history:
        for key, value in update_fields.items():
            setattr(db_device_history, key, value) if value else None
        db.commit()
        db.refresh(db_device_history)
    return db_device_history


def delete_device_history(db: Session, device_history_id: int):
    db_device_history = db.query(models.DeviceHistory).filter(
        models.DeviceHistory.id == device_history_id).first()
    if db_device_history:
        db.delete(db_device_history)
        db.commit()
    return db_device_history
