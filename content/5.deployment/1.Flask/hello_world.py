from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is the main page <h1>Hello World<h1>"


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(port=5000)
