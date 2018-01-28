import sqlite3
import os

# First delete any existing database and create a fresh one
try:
  os.remove('mydb.db')
  print('The database existed, but has been removed to be recreated')
except FileNotFoundError as e:
  print('The database will be created for the first time')

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

cursor.execute(''' 
CREATE TABLE product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  avail_qty INTEGER
)
''')

connection.close()

# Next, use the DAO to create a few 'product' rows in the DB
import ProductDao
from Product import Product

product1 = Product(None, 'XBox', 12)
ProductDao.insertProduct(product1)

product2 = Product(None, 'Pizza', 120)
ProductDao.insertProduct(product2)

# Print the products for everyone to see
print('Showing all products in the database')
products = ProductDao.getAllProducts()
for product in products:
  print ("ID: {}, Name: {}, Available Qty: {}".format(product.id, product.name, product.availableQty))

# Let's find a product by name and update and save it
xbox = ProductDao.getProductByName ('XBox')
print('The current XBox qty is: ' + str(xbox.availableQty))
print('We will now update it to 100 and save it to the DB')
xbox.availableQty = 100
ProductDao.updateProduct(xbox)
print('Let us search for XBox again in the DB and print the qty')
xbox = ProductDao.getProductByName ('XBox')
print('The new XBox qty from the DB is: ' + str(xbox.availableQty))

# Find if a product exists in the DB, by name
print("Let's see if we can find a product's ID from its name")
productId = ProductDao.getProductIdFromName ('Pizza')
if productId is not None:
  print('The product Pizza is found and has an ID: ' + str(productId))

# Show how deletes work
print('Let us now delete the Pizza product which we found had ID: ' + str(productId))
ProductDao.deleteProductById(productId)

print('Showing all products in the database (note that Pizza is not there anymore)')
products = ProductDao.getAllProducts()
for product in products:
  print ("ID: {}, Name: {}, Available Qty: {}".format(product.id, product.name, product.availableQty))

# Finally, insert some more products and exit
print('Let us insert a few more products and print them...')
product3 = Product(None, 'Samsung Galaxy 8', 15)
ProductDao.insertProduct(product3)
product4 = Product(None, 'Mouse', 200)
ProductDao.insertProduct(product4)
print('Showing all products in the database again...')
products = ProductDao.getAllProducts()
for product in products:
  print ("ID: {}, Name: {}, Available Qty: {}".format(product.id, product.name, product.availableQty))
