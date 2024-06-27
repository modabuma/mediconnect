import json

from sqlalchemy.orm import sessionmaker

from models.MembershipModel import MembershipModel
from shared.custom_exceptions import NotFoundError

class MembershipController:
    def __init__(self, session: sessionmaker):
        self.membership_model = MembershipModel()
        self.session = session
        
    def create(self, payload: dict):
        self.membership_model.insert_data(self.session, payload)
    
    def update(self, payload: dict):
        id = payload.pop("id")
        
        response = self.membership_model.update_data(self.session, {"id": id, "active": 1}, payload)
        
        if not response:
            raise NotFoundError("La afiliación que intenta editar no existe.")
    
    def delete(self, payload: dict):
        id = payload.pop("id")
        
        response = self.membership_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("La afiliación que intenta eliminar no existe.")
    
    def get(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")
        
        if payload["option"] == 1:
            return json.loads(str(self.membership_model.get_data(self.session, {"active": 1}, response_type="all")))

        return self.membership_model.get_paginated_data(self.session, limit, page, payload)