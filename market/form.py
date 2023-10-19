from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField,validators


class RegisterForm(FlaskForm):
    username=StringField('Username:', [validators.Length(min=4, max=25), validators.DataRequired()])
    email=StringField('Email: ', [validators.Length(min=4, max=10), validators.DataRequired()])
    password=PasswordField('Password: ', [validators.Length(min=6), validators.DataRequired()])
    confirm_password=PasswordField('Confirm Password: ', [validators.EqualTo('password'), validators.DataRequired()])
    submit=SubmitField('Create Account')
    