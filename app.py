from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
  return jsonify({"menssage":"pong"}) # usando jsonify para retornar un json

@app.route('/products', methods=["GET"]) # creando ruta products indicando metodos  
def getProducts():
  return jsonify({"products":products, "message":"Product's List"})

@app.route('/products', methods=["POST"])
def addProduct():
  print(request.json)
  newProduct = {
    "name": request.json['name'],
    "price": request.json['price'],
    "quantity": request.json['quantity']
  }
  products.append(newProduct)
  return jsonify({"message": "product Added Sucessfully", "products": products })

@app.route('/products/<string:product_name>', methods=["PUT"])
def editProduct(product_name):
  productFound = [product for product in products if product['name'] == product_name]
  if(len(productFound) > 0):
    productFound[0]['name'] = request.json['name']
    productFound[0]['price'] = request.json['price']
    productFound[0]['quantity'] = request.json['quantity']
    return jsonify({
      "message":"Product Updated",
      "product": productFound[0]
    })
  return jsonify({"error": "Product Not found"})


@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productsFound = [product for product in products if product['name'] == product_name]
  # productsFound = products.index(."name"='laptop')
  # print(te, ga)
  # print(type(productsFound))
  print(productsFound)
  if(productsFound != []):
    return jsonify({"product":productsFound[0]})
  else:
    return jsonify({"error":"Not found"})

@app.route('/products/<string:product_name>', methods=["DELETE"])
def deleteProduct(product_name):
  productsFound = [product for product in products if product["name"] == product_name]
  if len(productsFound) > 0:
    products.remove(productsFound[0])
    # print(productsFound[0])
    return jsonify({
      "message": "Product Deleted",
      "products": products
    })
  return jsonify({"message": "product not found"
  })

if __name__ == '__main__':
  app.run(debug=True, port=4000)