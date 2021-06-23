from flask import Flask

app = Flask(__name__)

# if app:
#      app.run(debug=True)



@app.route('/')
def hello_world():
    return 'Hello world!'
