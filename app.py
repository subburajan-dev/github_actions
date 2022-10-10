from flask import Flask

app = Flask(__name__)


@app.get("/")
def homepage():
    return {"message": "homepage"}


if __name__ == "__main__":
    app.run("0.0.0.0")
