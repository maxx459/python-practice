from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run() #we can also do like this to start instead of the "$flask --app helloflask run"