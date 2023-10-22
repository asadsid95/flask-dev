from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField,validators, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        
        if user:
            raise ValidationError('User already exists! Try again!')
         
    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        
        if email_address:
            raise ValidationError('Email address already exists, try again!')
    
    username=StringField('Username:', [validators.Length(min=4, max=25), validators.DataRequired()])
    email=StringField('Email: ', [validators.Length(min=4, max=10), validators.DataRequired()])
    password=PasswordField('Password: ', [validators.Length(min=6), validators.DataRequired()])
    confirm_password=PasswordField('Confirm Password: ', [validators.EqualTo('password'), validators.DataRequired()])
    submit=SubmitField('Create Account')
    