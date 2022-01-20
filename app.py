from tkinter import Variable
from flask import Flask,redirect,url_for,render_template

import firebase_admin 
from firebase_admin import credentials, firestore

cred = credentials.Certificate("servicesKey.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)
db = firestore.client()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/<name>")
def red(name):
    return "{name}".format(name=name)

@app.route("/redi")
def redfrom():
    return redirect(url_for("red", name = "username"))

@app.route("/admin")
def end():
    return "adminPage"

@app.route("/users")
def users():
    _users = []
    for user in db.collection('Users').get():
        _users.append(user.to_dict())

    return render_template("users.html",users = _users)


@app.route("/user/<user_id>")
def user(user_id):
    _user = db.collection('Users').document(user_id).get().to_dict()
    return render_template("user.html",user = _user)


@app.route("/products")
def products():
    _products = []
    for product in db.collection('Products').get():
        _products.append(product.to_dict())

    return render_template("products.html",products = _products)


@app.route("/product/<product_id>")
def product(product_id):
    _product = db.collection('Products').document(product_id).get().to_dict()
    return render_template("product.html",product = _product)


if __name__ == "__main__":
    app.run(debug=True)