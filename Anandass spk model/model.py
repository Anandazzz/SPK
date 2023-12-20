from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Laptop(Base):
    __tablename__="laptop_asus"
    id =Column(Integer, primary_key=True)
    brand=Column(String(255))
    ram=Column(String(10))
    prosesor=Column(String(255))
    storage=Column(String(10))
    baterai=Column(String(10))
    harga=Column(String(20))
    webcam=Column(String(10))

    def __repr__(self):
        return f"Laptop(id={self.id!r}, brand={self.brand!r})"
