from flask import Flask
from .routes.planet_routes import planets_bp

# Add configuration, such as registering blueprints or configuring databases
def create_app(test_config=None):
    app = Flask(__name__)

    app.register_blueprint(planets_bp)

    return app
