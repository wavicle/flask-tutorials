from flask import Flask, request, render_template, redirect
import sqlite3
from Product import Product
import ProductDao

app = Flask(__name__)

@app.route('/productList.html')
def productList():
  products = ProductDao.getAllProducts()
  return render_template ('product_list.html', products = products)

@app.route('/deleteProduct.html')
def deleteProduct():
  productId = request.args.get('productId')
  ProductDao.deleteProductById(productId)
  return redirect('/productList.html')

@app.route('/editProduct.html', methods=['GET', 'POST'])
def editProduct():
  if request.method == 'GET':
    productId = request.args.get('productId')
    product = ProductDao.getProductById(productId)
    return render_template('product_add_edit.html', product = product)
  else:
    productId = request.form.get('id')
    print('Saving product with ID: ' + str(productId))
    product = ProductDao.getProductById(productId)
    name = request.form.get('name')
    qty = request.form.get('qty')
    product.name = name
    product.availableQty = qty
    ProductDao.updateProduct(product)
    return render_template('product_add_edit.html', product = product, saveComplete = True)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)

