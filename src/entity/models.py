from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    birthday = Column(Date)
    additional_info = Column(String, nullable=True)