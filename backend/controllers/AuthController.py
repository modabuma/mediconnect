from sqlalchemy.orm import sessionmaker

from models.UsersModel import UsersModel
from shared.custom_exceptions import BadCredentialsError

class AuthController:
    def __init__(self, session: sessionmaker):
        self.session = session
        
    def authenticate(self, payload: dict) -> dict:
        user_model = UsersModel()
        
        response = user_model.get_data(self.session, {
            "email": payload["email"],
            "active": 1
        })
        
        if not response:
            raise BadCredentialsError("El correo ingresado no coincide.")

        if not response.verify_password(payload["password"]):
            raise BadCredentialsError("La contraseña ingresada no coincide.")
        
        return {
            "id": response.id,
            "role": response.roles.code,
            "names": response.additional_data.names,
            "lastnames": response.additional_data.lastnames
        }