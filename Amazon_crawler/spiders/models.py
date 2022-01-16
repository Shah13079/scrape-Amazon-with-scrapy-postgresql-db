from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String,  Float, )
from scrapy.utils.project import get_project_settings



DeclarativeBase = declarative_base()

def db_connect():
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Amazon_data_model(DeclarativeBase):
    __tablename__ = "products_data"

    id = Column(Integer, primary_key=True)
    Product_Url= Column('Product_Url',String(1200))
    ASIN = Column('ASIN', String(100))
    title = Column('title', String(500))
    Price = Column('Price', Float(20))
    Currancy = Column('Currancy', String(100))
    Ratings = Column('Ratings', String(100))
    Brand = Column('Brand', String(100))
    Amazon_choice = Column('Amazon_choice', String(1000))
    
