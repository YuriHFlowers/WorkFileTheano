from flask import jsonify

app = jsonify(__name__)


@app.route("/person/")
def hello():
    return jsonify({"name": "Jimit", "address": "India"})


if __name__ == "__main__":
    app.run()
