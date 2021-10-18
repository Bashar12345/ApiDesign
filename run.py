from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



from routes import app


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# if app:
#      app.run(debug=True)
db = SQLAlchemy(app)


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    data = db.relationship('Data',lazy=True) 

class Data(db.Model):
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(7500), unique=True, nullable=False)


    def __repr__(self):
        return f"User('{self.id}','{self.username}')"





