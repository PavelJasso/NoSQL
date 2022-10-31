import redis
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import InputRequired, Email, Length
from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_client = FlaskRedis(app)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_text'

class LoginForm(FlaskForm):
    Email = StringField('email', validators = [InputRequired(), Length(min = 10, max = 50)])
    password = PasswordField('heslo', validators = [InputRequired(), Length(min = 10, max = 50)])
    remember = BooleanField('Pamatuj si mě')

class RegisterForm(FlaskForm):
    email = StringField('Email', [InputRequired(), Length(min = 10, max = 50)])
    password = PasswordField('Nové heslo', [
        validators.DataRequired(),
        validators.EqualTo('Potvrdit', message='Hesla musí být stejná!')])
    confirm = PasswordField('Heslo znovu')
    accept_tos = BooleanField('Přijímám podmínky.', [validators.DataRequired()])

@app.route("/")
def html():
    return render_template('template.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route("/register")
def register():
    form = RegisterForm() #zmenit
    return render_template('register.html', form = form)

if __name__ == "__main__":
    app.run(debug=True)

