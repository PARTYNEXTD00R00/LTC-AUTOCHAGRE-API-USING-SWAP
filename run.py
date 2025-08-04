from flask import Flask, g
from routes import blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    for bp in blueprints:
        app.register_blueprint(bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080)