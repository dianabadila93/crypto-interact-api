from flask import Flask
from flask_restplus import Api
from src.api.controllers.interact_controller import blueprint \
    as interact_blueprint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(interact_blueprint)

if __name__ == "__main__":
    app.run()