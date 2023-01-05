from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from models.base import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    created = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return '<Contact %r>' % (self.name)
