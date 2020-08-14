from flask import Flask

app = Flask(__name__)

# routes in flask are created using the "@" decorator and passing in a URL or path.
@app.route("/")
def index():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
