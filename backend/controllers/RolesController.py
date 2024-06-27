import json

from sqlalchemy.orm import sessionmaker

from models.RolesModel import RolesModel
from shared.custom_exceptions import NotFoundError

class RolesController:
    
    def __init__(self, session: sessionmaker):
        self.roles_model = RolesModel()
        self.session = session
    
    def create(self, payload: dict):
        self.roles_model.insert_data(self.session, payload)
    
    def update(self, payload: dict):
        id = payload.pop("id")
        
        response = self.roles_model.update_data(self.session, {"id": id, "active": 1}, payload)
        
        if not response:
            raise NotFoundError("El rol que intenta editar no existe.")
    
    def delete(self, payload: dict):
        id = payload.pop("id")
        
        response = self.roles_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("EL rol que intenta eliminar no existe.")
    
    def get(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")
        
        if payload["option"] == 1:
            return json.loads(str(self.roles_model.get_data_with_in_method_all(self.session, {})))

        return self.roles_model.get_paginated_data(self.session, limit, page, payload)