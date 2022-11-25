import redis
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import InputRequired, Email, Length
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
import flask_login
from flask_login import login_required, logout_user, UserMixin, LoginManager, login_user, current_user

app  = Flask(__name__)
redis_client = FlaskRedis(app)
app.config['SECRET_KEY'] = 'hardsecretkey'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root@127.0.0.1:3308/registration"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Prosím přihlaste se pro zobrazení této stránky!"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route("/")
def html():
    return render_template('template.html')

@app.route("/login")
def login():        
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login_post():
    if request.method == "POST":
        user = request.form["username"]
        passw = request.form["password"]
        user_info = User.query.filter_by(username=user).first()
        if user not in db.session.execute(db.select(User.username)).scalars():
            flash("Neexistující uživatel!")
        elif passw != user_info.password:
            flash("Existující uživatel ale chybné heslo!")
        else:
            login_user(user_info)
            return render_template("profil.html")
            
            
    return render_template("login.html")

@app.route('/register' , methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form["username"]
        passw = request.form["password"]
        if user not in db.session.execute(db.select(User.username)).scalars():
            register =User(user, passw)

            db.session.add(register)
            db.session.commit()

            flash("Registrace byla úspěšná!")
            return redirect(url_for('login'))
        else:
            flash("Jméno už existuje!")
            
    db.create_all()
    return render_template('register.html')

@app.route("/profil")
@login_required
def profil():
    return render_template("profil.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    

if __name__ == "__main__":  
    app.run(debug=True)

