from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Wecome by TargetX25'


if __name__ == "__bot__":
    app.run()
