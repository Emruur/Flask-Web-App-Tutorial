from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key= True)
    email= db.Column(db.String(150), unique= True)
    name= db.Column(db.String(150))
    password= db.Column(db.String(150))
    notes= db.relationship("Note")

    def __init__ (self, email, name, password):
        self.email= email
        self.name= name
        self.password= password
        print("User Created")

    def __str__(self) -> str:
        return self.name +" "+ self.email

class Note(db.Model):
    id= db.Column(db.Integer, primary_key= True)
    note= db.Column(db.String(1500))
    date= db.Column(db.DateTime(timezone= True),default= func.now())
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'))
    


