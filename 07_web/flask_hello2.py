from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("hello.html", title = "HELLO")

@app.route("/first")
def first():
    return render_template("first.html", title = "FIRST")

@app.route("/second")
def second():
    return render_template("first.html", title = "SECOND")

if __name__ == "__main__":
    app.run(host="0.0.0.0")