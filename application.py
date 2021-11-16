from flask import Flask, request, render_template

application = Flask(__name__)


@application.route("/")
def hello_world():
    return "<p>Hello, Welcome to my Page!</p>"


if __name__ == '__main__':
    application.run()
