from flask import render_template,redirect, url_for 
from market import app
from market.models import Item, User
from market.form import RegisterForm
from market import db

@app.route('/')
def home_page(name='Asad'):
    return render_template("greet_user.html", name=name)

@app.route('/market')
def market_page(): 
    # items= [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    # ]
    
    items=Item.query.all()
    
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email.data, password_hash=form.password.data )
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors !={}:
        for err_msg in form.errors.values():
            print(f'Error: {err_msg}')
    return render_template('register.html', form=form)