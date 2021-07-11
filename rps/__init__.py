from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secrety_key = 'random'

    from . import rps
    app.register_blueprint(rps.bp)

    return app
