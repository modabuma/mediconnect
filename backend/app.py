import os
from datetime import timedelta

from flask_jwt_extended import JWTManager
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from routes.auth import auth
from routes.membership import membership
from routes.administrator import administrator
from routes.document_types import document_types
from routes.symptoms import symptoms
from routes.sub_symptoms import sub_symptoms
from routes.appointments import appointments
from routes.roles import roles
from shared.blacklist import blacklist

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload['jti']
    return jti in blacklist

app.register_blueprint(auth)
app.register_blueprint(document_types)
app.register_blueprint(membership)
app.register_blueprint(roles)
app.register_blueprint(administrator)
app.register_blueprint(symptoms)
app.register_blueprint(sub_symptoms)
app.register_blueprint(appointments)