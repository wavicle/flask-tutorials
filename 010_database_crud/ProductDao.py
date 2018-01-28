import sqlite3
from Product import Product

def getAllProducts():
  products = []
  conn = sqlite3.connect('mydb.db')
  conn.row_factory = sqlite3.Row
  rows = conn.cursor().execute('SELECT * FROM product')
  for row in rows:
    product = Product (row['id'], row['name'], row['avail_qty'])
    products.append(product)
  conn.close()
  return products

def getProductIdFromName(name):
  conn = sqlite3.connect('mydb.db')
  conn.row_factory = sqlite3.Row
  row = conn.cursor().execute (
    'SELECT * FROM product WHERE name = :name',
    {'name': name}
  ).fetchone()
  if row is not None:
    return row['id']
  else:
    return None
  conn.close()

def getProductByName (name):
  conn = sqlite3.connect('mydb.db')
  conn.row_factory = sqlite3.Row
  row = conn.cursor().execute (
    'SELECT * FROM product WHERE name = :name',
    {'name': name}
  ).fetchone()
  if row is not None:
    id = row['id']
    name = row['name']
    availableQty = row['avail_qty']
    product = Product(id, name, availableQty)
    return product
  else:
    return None
  conn.close()

def insertProduct(product):
  conn = sqlite3.connect('mydb.db')
  cursor = conn.cursor()
  cursor.execute (
    'INSERT INTO product (name, avail_qty) VALUES (:name, :qty)',
   {'name': product.name, 'qty': product.availableQty}
  )
  conn.commit()
  conn.close()

def updateProduct(product):
  conn = sqlite3.connect('mydb.db')
  cursor = conn.cursor()
  cursor.execute (
    'UPDATE product SET name = :name, avail_qty = :qty WHERE id = :id',
   {'name': product.name, 'qty': product.availableQty, 'id': product.id}
  )
  conn.commit()
  conn.close()
  
def deleteProductById (productId):
  conn = sqlite3.connect('mydb.db')
  cursor = conn.cursor()
  cursor.execute (
    'DELETE FROM product WHERE id = :id',
   {'id': productId}
  )
  conn.commit()
  conn.close()

