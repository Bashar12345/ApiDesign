
from RED import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    password =db.Column(db.String(20),unique=True,nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.username}')"

# class data(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(100),unique=True,nullable=False)
#     description = db.Column(db.String(10000),unique=True,nullable=False)

   

class Topic(db.Model):
    topic_id = db.Column(db.Integer, primary_key=True)
    t_name = db.Column(db.String(20), unique=True, nullable=False)
    data = db.relationship('Data',backref="author",lazy=True) 

class Data(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(7500), unique=True, nullable=False)
    data_id = db.Column(db.Integer, db.ForeignKey(
        'topic.topic_id'), nullable=False)

    def __repr__(self):
        return f"data('{self.title}','{self.description}')"  

    
    
    