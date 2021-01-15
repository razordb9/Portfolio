from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email       = StringField("Email", validators=[DataRequired()])
    password    = StringField("Password", validators=[DataRequired()])
    rememberme  = BooleanField("Remember Me")
    submit      = SubmitField("Login")

class RegisterForm(FlaskForm):
    email               = StringField("Email", validators=[DataRequired()]) 
    password            = StringField("Password", validators=[DataRequired()])
    password_confirm    = StringField("Confirm Password", validators=[DataRequired()])
    firstname    = StringField("First Name", validators=[DataRequired()])
    lastname    = StringField("Last Name", validators=[DataRequired()])
    submit      = SubmitField("Register Now")
