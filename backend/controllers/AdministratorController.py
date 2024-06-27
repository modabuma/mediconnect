import random
import json

from sqlalchemy.orm import sessionmaker

from models.UsersModel import UsersModel
from models.AdditionalDataModel import AdditionalDataModel
from models.MembershipModel import MembershipModel
from models.RolesModel import RolesModel
from models.VerificationCodesModel import VerificationCodesModel
from models.DocumentTypesModel import DocumentTypesModel
from shared.custom_exceptions import NotFoundError, DuplicatedFieldsError, CodeError
from shared.email_sender import send_email

class AdministratorController:
    
    def __init__(self, session: sessionmaker):
        self.users_model = UsersModel()
        self.session = session
    
    def send_verification_code(self, payload: dict):
        verification_codes = VerificationCodesModel()
        
        code = str(random.randint(10000, 99999))
        
        email = payload["email"]
        
        response = self.users_model.get_data(self.session, {"email": email})
        
        if response:
            raise DuplicatedFieldsError("El correo ingresado ya se encuentra registrado.")
        
        verification_codes.insert_data(self.session, {"code": code})
        
        content = f"Su código de verificación es: {code}"
        
        send_email(email, "Código de verificación", content)
    
    def verify_code(self, payload: dict):
        verification_codes = VerificationCodesModel()
        
        filters = {
            "code": payload["code"],
            "active": 1
        }
        
        response = verification_codes.get_data(self.session, filters)
        
        if response is None:
            raise CodeError("El código de verificación ingresado es inválido.")
        
        verification_codes.update_data(self.session, filters, {"active": 0})
        
    def create_users(self, payload: dict):
        additional_data_model = AdditionalDataModel()
        membership_model = MembershipModel()
        roles_model = RolesModel()
        
        main_data = {
            "membership_id": payload.pop("membership_id"),
            "role": payload.pop("role"),
            "email": payload.pop("email"),
            "password": payload.pop("password")
        }
        
        response = membership_model.get_data(self.session, {"id": main_data["membership_id"], "active": 1})
        
        if not response:
            raise NotFoundError("La afiliación que intenta ingresar no existe.")
        
        response = roles_model.get_data_with_in_method(self.session, {"id": main_data["role"]})
        
        if not response:
            raise NotFoundError("El rol que intenta ingresar no existe o no está disponible para esta acción.")

        response = self.users_model.get_data(self.session, {"email": main_data["email"]})
        
        if response:
            raise DuplicatedFieldsError("El correo ingresado ya se encuentra registrado.")
            
        additional_data_id = additional_data_model.insert_data(self.session, payload)
        
        main_data["additional_data_id"] = additional_data_id
        
        self.users_model.insert_data(self.session, main_data)
    
    def update_users(self, payload: dict):
        additional_data_model = AdditionalDataModel()
        document_types_model = DocumentTypesModel()
        membership_model = MembershipModel()

        id_user = payload.pop("id")
        
        main_data = {
            "membership_id": payload.pop("membership_id", None),
            "email": payload.pop("email", None),
        }
        
        main_data = dict(filter(membership_model.exclude_none_values_from_filters, main_data.items()))
        
        if "membership_id" in main_data:
            response = membership_model.get_data(self.session, {"id": main_data["membership_id"], "active": 1})

            if not response:
                raise NotFoundError("La afiliación que intenta ingresar no existe.")
        
        if "email" in main_data:
            response = self.users_model.get_data(self.session, {"email": main_data["email"]})

            if response:
                raise DuplicatedFieldsError("El correo ingresado ya se encuentra registrado.")
        
        if "document_type" in payload:
            response = document_types_model.get_data(self.session, {"id": payload["document_type"], "active": 1})
            
            if response is None:
                raise NotFoundError("El tipo de documento ingresado no existe.")
        
        response = self.users_model.get_data(self.session, {"id": id_user, "active": 1})
        
        if response is None:
            raise NotFoundError("El usuario no existe.")
        
        if main_data:
            self.users_model.update_data(self.session, {"id": id_user, "active": 1}, main_data)
        
        additional_data_model.update_data(self.session, {"id": response.additional_data_id}, payload)
    
    def delete_users(self, payload: dict):
        id = payload.pop("id")
        
        response = self.users_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("El usuario que intenta eliminar no existe.")
    
    def get_users(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")
        
        option = payload.pop("option")
        
        if option == 1:
            return json.loads(str(self.users_model.get_data(self.session, {"active": 1, "role": payload["role"]}, response_type="all")))
        
        filters_main = {
            "id": payload.pop("id", None),
            "membership_id": payload.pop("membership_id", None),
            "role": payload.pop("role", None),
            "email_like": payload.pop("email_like", None)
        }
        
        return self.users_model.get_paginated_data_with_join(self.session, limit, page, filters_main, payload)