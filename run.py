from flask import Flask

app = Flask(__name__)

# if app:
#      app.run(debug=True)

from routes import app


