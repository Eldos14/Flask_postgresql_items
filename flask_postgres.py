from flask import Flask, render_template,redirect, request
from postgres_sql import get_items, get_buys, add_buy

app = Flask(__name__)

@app.route('/items')
def items1():
    items = get_items()
    return render_template("items.html", items=items)

@app.route('/buy', methods=['POST'])
def buy():
    item_name = request.form['item_name']
    price = request.form['price']
    user_name = "Eldos"  
    add_buy(user_name, item_name, price)
    return redirect('/buys')

@app.route('/buys')
def buyus1():
   user_name = "Eldos"
   buys = get_buys()
   return render_template("buys.html", user=user_name, buys=buys)


if __name__ == '__main__':
    app.run(debug=True)
