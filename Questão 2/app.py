from flask import Flask, request, jsonify
from models.product import Product
from models.cart import Cart
from models.order import Order

app = Flask(__name__)

products = []
cart = Cart()

def serialize_product(product):
        return {
            'name': product.name,
            'price': product.price,
            'stock': product.stock
        }

@app.route('/products', methods=['GET', 'POST'])
def list_products_add():
    if request.method == 'GET':
        products_json = [serialize_product(product) for product in products]
        return jsonify(products_json)

    if request.method == 'POST':
        data = request.json
        product = Product(data['name'], data['price'], data['stock'])
        products.append(product)
        return jsonify(product.to_dict()), 201

@app.route('/cart', methods=['GET', 'POST', 'DELETE'])
def operations_cart():
    if request.method == 'GET':
        
        return jsonify(cart.products)

    if request.method == 'POST':
        
        data = request.json
        product_id = data['product_id']
        qtd = data.get('qtd', 1)

        product = next((p for p in products if p.id == product_id), None)
        if product:
            cart.add_product(product, qtd)
            return jsonify(cart.products)
        else:
            return "Produto não encontrado", 404

    if request.method == 'DELETE':
        data = request.json
        product_id = data['product_id']
        qtd = data.get('qtd', 1)

        product = next((p for p in products if p.id == product_id), None)
        if product:
            cart.remove_product(product, qtd)
            return jsonify(cart.products)
        else:
            return "Produto não encontrado", 404

@app.route('/order', methods=['POST'])
def create_order():
    total = cart.calculate_total()
    order = Order(cart.products, total)
    cart.finalize_order()
    return jsonify(order.__dict__), 201

if __name__ == '__main__':
    app.run(debug=True)
