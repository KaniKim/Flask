import datetime


class Message:
    id: str
    message: str
    duration: datetime.time
    creation_date: datetime.datetime
    message_category: str
    printed_times: int
    printed_once: bool
