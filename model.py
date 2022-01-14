from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=Ture,nullable=False)
    password =db.Column(db.String(20),unique=Ture,nullable=False)

class data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),unique=True,nullable=False)
    description = db.Column(db.String(10000),unique=True,nullable=False)

    def __repr__(self):
        return f"data('{self.title}','{self.description}')"  