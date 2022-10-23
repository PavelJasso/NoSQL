from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_text'

class LoginForm(FlaskForm):
    Email = StringField('email', validators = [InputRequired(), Length(min = 10, max = 50)])
    password = PasswordField('password', validators = [InputRequired(), Length(min = 10, max = 50)])
    remember = BooleanField('remember me')

@app.route("/")
def html():
    return render_template('template.html')

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form = form)

@app.route("/register")
def register():
    form = LoginForm() #zmenit
    return render_template('register.html', form = form)

if __name__ == "__main__":
    app.run(debug=True)

