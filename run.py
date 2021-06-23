from flask import Flask,render_template

app = Flask(__name__)

# if app:
#      app.run(debug=True)



@app.route('/')
def hello_world():
    return render_template("index.html")
