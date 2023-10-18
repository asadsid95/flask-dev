from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/home')
def home_page(name='Asad'):
    return render_template("greet_user.html", name=name)

@app.route('/market')
def market_page(): 
    items= [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    
    return render_template('market.html', items=items)