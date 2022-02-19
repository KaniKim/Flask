from sqlalchemy.orm import Session
from .models import Message


class CRUD_API:
    def insert_message(db: Session, message: Message) -> Message:
        db_message = Message(
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

    def get_message(db: Session, id: int) -> Message:
        return db.query(Message).filter(Message.id == id).first()

    def delete_message(db: Session, id: int):
        db.query(Message).filter(Message.id == id).delete()

    def patch_message(db: Session, id: int, message: Message) -> Message:
        db_message = db.query(Message).filter(Message.id == id)
        db_message.update(
            message=message.message,
            duration=message.duration,
            creation_date=message.creation_date,
            message_category=message.message_category,
            printed_times=message.printed_times,
            printed_once=message.printed_once,
        )

        return message
