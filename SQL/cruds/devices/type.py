from sqlalchemy.orm import Session
from ... import models, schemas


def get_device_type(db: Session, device_type_id: int):
    return db.query(models.DeviceType).filter(models.DeviceType.id == device_type_id).first()


def create_device_type(db: Session, device_type: schemas.DeviceTypeCreate):
    db_device_type = models.DeviceType(**device_type.model_dump())
    db.add(db_device_type)
    db.commit()
    db.refresh(db_device_type)
    return db_device_type


def update_device_type(db: Session, device_type_id: int, update_fields: dict):
    db_device_type = db.query(models.DeviceType).filter(
        models.DeviceType.id == device_type_id).first()
    if db_device_type:
        for key, value in update_fields.items():
            setattr(db_device_type, key, value) if value else None
        db.commit()
        db.refresh(db_device_type)
    return db_device_type


def delete_device_type(db: Session, device_type_id: int):
    db_device_type = db.query(models.DeviceType).filter(
        models.DeviceType.id == device_type_id).first()
    if db_device_type:
        db.delete(db_device_type)
        db.commit()
    return db_device_type
