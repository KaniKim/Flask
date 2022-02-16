from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACLCEHMY_DATABASE_URL = "postgresql://kanikim:rlarhksgml!4113@127.0.0.1:5432/flask"

engine = create_engine(SQLACLCEHMY_DATABASE_URL, connect_arg={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
