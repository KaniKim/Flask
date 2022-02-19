from sqlalchemy.orm import Session
import models, database
from domain import Message


def insert_message(db: Session, message: Message):
    db_message = models.Message(
        id=message.id,
        message=message.message,
        duration=message.duration,
        creation_date=message.creation_date,
        message_category=message.message_category,
        printed_times=message.printed_times,
        printed_once=message.printed_once,
    )

    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


def get_message(db: Session, id: int):
    return db.query(models.Message).filter(models.Message.id == id).first()


def delete_message(db: Session, id: int):
    db.query(models.Message).filter(models.Message.id == id).delete()
