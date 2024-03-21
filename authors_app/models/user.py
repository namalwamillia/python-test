# In your authors_app/models/user.py file
from authors_app.extensions import db

class MyUser(db.Model):  
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    contact = db.Column(db.String(15))
    password = db.Column(db.Text())
    user_type = db.Column(db.String(20))
    create_at = db.Column(db.DateTime, default=db.func.now())
    #updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, first_name, last_name, email, contact, password, user_type='author'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contact = contact
        self.password = password
        self.user_type = user_type

    def __repr__(self):
        return f"<MyUser {self.email}>"
