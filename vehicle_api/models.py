from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)

    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))

    deals = relationship(
        "Deal", back_populates="customers", cascade="all, delete, delete-orphan", uselist="false"
    )


class Deal(Base):
    __tablename__ = "deals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    vehicles = relationship("Vehicle", back_populates="deals", cascade="all, delete, delete-orphan", uselist="false")


class Dealer(Base):
    __tablename__ = "dealers"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True)

    vehicles = relationship("Vehicle", back_populates="dealers", cascade="all, delete, delete-orphan")


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vin = Column(String, index=True)
    model = Column(String)
    year = Column(Date)
    brand = Column(String)

    dealer_id = Column(Integer, ForeignKey("dealers.id"))
