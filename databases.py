from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :
def add_product(name , year , tipe , price):
 	product_object = Product(
 		name = name,
 		year = year,
 		tipe = tipe,
 		price = price)
 	session.add(product_object)
 	session.commit()
 	

def create_product():
  #TODO: complete the functions (you will need to change the function's inputs)

  pass

def update_product(tipe , year , price):
  #TODO: complete the functions (you will need to change the function's inputs)
  product_object = session.query(
  	Product).filter_by(tipe = tipe).all()
  product_object.year = year
  product_object.price = price
  session.commit()
 

def delete_product(id):
	session.query(product).filter_by(
		id=id).delete()
	session.commit()
  

def get_product(id):
	product = session.query(
		Product).filter_by(id = id)
	return product
  
