from src.api.controllers.interact_controller import blueprint \
    as interact_blueprint
from flask import Blueprint
from flask_restx import Api
from src.api.controllers.interact_controller import interactNamespace

api_extension = Api(
    interact_blueprint,
    title='BIDS API',
    version='1.0',
    description='BIDS API',
    doc='/swagger'
)

api_extension.add_namespace(interactNamespace)