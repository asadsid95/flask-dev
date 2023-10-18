from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/<name>')
@app.route('/')
def about(name=None):
    return render_template("home.html", name=name)