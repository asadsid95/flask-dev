from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField,validators


class RegisterForm(Form):
    username=StringField('Username:', [validators.Length(min=4, max=25)])
    email=StringField('Email: ', [validators.Length(min=4, max=10)])
    password=PasswordField('Password: ')
    confirm_password=PasswordField('Confirm Password: ')
    submit=SubmitField('Submit')
    