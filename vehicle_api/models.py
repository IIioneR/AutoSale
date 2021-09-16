from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Deal(Base):
    __tablename__ = "deal"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    owner = relationship("User", back_populates="items")


class Saler(Base):
    __tablename__ = "saler"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    name = Column(String, index=True)
    brand = Column(Integer, ForeignKey("users.id"))
