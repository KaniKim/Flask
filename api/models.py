from sqlalchemy import Column, Integer, String, DateTime, Time, Boolean
from .database import Base


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True)
    message = Column(String(64))
    duration = Column(Time())
    creation_date = Column(DateTime())
    message_category = Column(String(64))
    printed_times = Column(Integer(64))
    printned_once = Column(Boolean())
