from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.errors import errors
from flask_mail import Mail

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
mail = Mail(app)


api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/movie-bag'
}

from resources.routes import initialize_routes  # noqa

initialize_db(app)
initialize_routes(api)
