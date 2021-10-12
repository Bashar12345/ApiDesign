from flask import  render_template
import nasa_api
from run import app

@app.route('/')
def index():
    return render_template("index.html")
