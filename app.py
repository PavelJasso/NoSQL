import redis
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import InputRequired, Email, Length
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask import logging


app  = Flask(__name__)
redis_client = FlaskRedis(app)
app.config['SECRET_KEY'] = 'hardsecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root@127.0.0.1:3308/registration"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route("/")
def html():
    return render_template('template.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    """if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login = User.query.filter_by(username=username, password=password).first()
        if login is not None:
            return redirect(url_for("template.html"))
            """
    return render_template("login.html")

@app.route('/register' , methods = ['GET', 'POST'])
def register():


    if request.method == "POST":
        username = request.form["username"]
        if username not in db.session.execute(db.select(User.username)).scalars():
            register =User(request.form["username"], request.form["password"])

            db.session.add(register)
            db.session.commit()

            flash("Registrace byla úspěšná!")
            return redirect(url_for('login'))
        else:
            flash("Jméno už existuje!")
            
    db.create_all()
    return render_template('register.html')
    

if __name__ == "__main__":  
    app.run(debug=True)

