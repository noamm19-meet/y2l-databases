from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Product(Base):
    # TODO: complete this class
    __tablename__ = "Product"
    Product_id = Column(Integer , Priamary_key = True)
    name = Column(String)
    year = Column(Integer)
    tipe = Column(String)
    price = Column(Integer)

 def __repr__(self):
 	return ("Product name: {} \n"
 		"Product expiration date: {} \n"
 		"Product tipe: {}\n"
 		"Product price: {}").format(
 		self.name,
 		self.year,
 		self.tipe,
 		self.price)
 	
