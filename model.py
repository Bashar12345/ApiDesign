from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=Ture,nullable=False)