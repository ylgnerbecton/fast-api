from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.db import Base


class InternationalMigration(Base):

    __tablename__ = "migration"

    id = Column(Integer, primary_key=True)
    year_month = Column(String(50))
    month_of_release = Column(String(50))
    passenger_type = Column(String(50))
    direction = Column(String(50))
    citizenship = Column(String(50))
    visa = Column(String(50))
    country_of_residence = Column(String(50))
    estimate = Column(Integer)
    standard_error = Column(Integer)
    status = Column(String(50))
 
    def __init__(self, year_month, month_of_release, passenger_type, direction, citizenship, visa, country_of_residence, estimate, standard_error, status):
        self.year_month = year_month
        self.month_of_release = month_of_release
        self.passenger_type = passenger_type
        self.direction = direction
        self.citizenship = citizenship
        self.visa = visa
        self.country_of_residence = country_of_residence
        self.estimate = estimate
        self.standard_error = standard_error
        self.status = status


class InternationalMigrationSchema(BaseModel):
    year_month: str = Field(..., min_length=1, max_length=50)
    month_of_release: str = Field(..., min_length=1, max_length=50)
    passenger_type: str = Field(..., min_length=1, max_length=50)
    direction: str = Field(..., min_length=1, max_length=50)
    citizenship: str = Field(..., min_length=1, max_length=50)
    visa: str = Field(..., min_length=1, max_length=50)
    country_of_residence: str = Field(..., min_length=1, max_length=50)
    estimate : int = Field(...)
    standard_error: int = Field(...)
    status: str = Field(..., min_length=1, max_length=50)


class InternationalMigrationDB(InternationalMigrationSchema):
    id: int

    class Config:
        orm_mode = True
