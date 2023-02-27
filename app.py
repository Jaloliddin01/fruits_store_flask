from flask import Flask, request, render_template
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    # print(type(db.all()))
    all_products = {'all_products' : db.all()}
    # print(db.get_all_types())
    all_types = list(db.get_all_types())
    # print(all_types)
    return render_template("index.html", items = all_products, home=True, types = all_types)


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    data = request.get_json()
    db.add(data)
    return 'Added'


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    all_products = {'all_products' : db.get_by_type(type)}
    all_types = list(db.get_all_types())
    return render_template("index.html", items = all_products, home=False, types=all_types)


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    all_products = {'all_products' : db.get_by_name(name)}
    return render_template("index.html", items = all_products)


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    all_products = {'all_products' : db.get_by_price(price)}
    return render_template("index.html", items = all_products)



if __name__ == '__main__':
    app.run(debug=True)