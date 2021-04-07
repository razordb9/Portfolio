from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User

class LoginForm(FlaskForm):
    email       = StringField("Email", validators=[DataRequired(), Email()])
    password    = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit      = SubmitField("Login")

class RegisterForm(FlaskForm):
    email               = StringField("Email", validators=[DataRequired(), Email()])
    password            = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm    = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name          = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name           = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    permission          = SelectField(u'Permission', choices=[('SUDO', 'SUDO'), ('Admin', 'Admin'), ('User', 'User')], validators=[DataRequired()])
    #permission          = StringField("Permission", validators=[DataRequired(), Length(min=2,max=55)])
    submit              = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

class UpdateUserForm(FlaskForm):
    first_name  = StringField("First Name")
    last_name   = StringField("Last Name")
    email       = StringField("Email")
    permission  = SelectField(u'Permission', choices=[('Permission', 'Sudo'), ('Permission', 'Admin'), ('Permission', 'User')], validators=[DataRequired()])
    #submit      = SubmitField("Updateas")
    #submet      = SubmitField("Remove")

class MyWorkItem(FlaskForm):
    title           = StringField("Title")
    description     = StringField("Description")

class AddMyWorkItem(FlaskForm):
    title           = StringField("Title", validators=[DataRequired(),Length(min=5,max=30)])
    description     = TextAreaField("Description", validators=[DataRequired(),Length(min=1,max=2555)])
    submit          = SubmitField("Add work item")

class AddBlogEntry(FlaskForm):
    title           = StringField("Titel", validators=[DataRequired(),Length(min=5,max=100)])
    text            = TextAreaField("Text", validators=[DataRequired(),Length(min=1,max=4096)])
    hashTag         = StringField("Hashtag", validators=[DataRequired(),Length(min=1,max=4096)])
    visibility      = BooleanField("Visibility")
    submit          = SubmitField("Add new blog entry")

class BlogEntry(FlaskForm):
    title           = StringField("Title")
    text            = StringField("Text")
    visibility      = BooleanField("Visibility")