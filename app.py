from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/v1/hello-world-15")
    def hello():
        return "Hello World 15!"

    return app
