import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class blog(db.Document):
    blog_id     =   db.IntField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    text        =   db.StringField( max_length=4096 )
    visibility  =   db.BooleanField()

class work(db.Document):
    work_id     =   db.IntField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=4096 )

class User(db.Document):
    user_id     =   db.IntField( unique=True)
    first_name  =   db.StringField( max_length=50)
    last_name   =   db.StringField( max_length=50)
    email       =   db.StringField( max_length=100)
    password    =   db.StringField()
    permission  =   db.StringField()

    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def get_password(self,password):
        return check_password_hash(self.password, password)