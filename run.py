
from flask_sqlalchemy import SQLAlchemy
 
from iapp import app

#from routes import app


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# if app:
#      app.run(debug=True)
db = SQLAlchemy(app)








