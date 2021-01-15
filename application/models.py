import flask
from application import db

class work(db.Document):
    work_id     =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )