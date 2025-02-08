import os
from flask import Flask
from app.routes import home


def create_app():
    app = Flask(
        __name__,
        static_folder=os.path.join(
            os.path.dirname(__file__), 'app/static')
    )

    # Register blueprints
    app.register_blueprint(home.bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
