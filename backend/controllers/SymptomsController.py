import json

from sqlalchemy.orm import sessionmaker

from models.SymptomsModel import SymptomsModel
from shared.custom_exceptions import NotFoundError

class SymptomsController:
    
    def __init__(self, session: sessionmaker):
        self.symptoms_model = SymptomsModel()
        self.session = session
    
    def create(self, payload: dict):
        self.symptoms_model.insert_data(self.session, payload)
    
    def update(self, payload: dict):
        id = payload.pop("id")
        
        response = self.symptoms_model.update_data(self.session, {"id": id, "active": 1}, payload)
        
        if not response:
            raise NotFoundError("El síntoma que intenta editar no existe.")
    
    def delete(self, payload: dict):
        id = payload.pop("id")
        
        response = self.symptoms_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("EL síntoma que intenta eliminar no existe.")
    
    def get(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")

        option = payload.pop("option")
        
        if option == 1:
            return json.loads(str(self.symptoms_model.get_data(self.session, {"active": 1}, response_type="all")))
        
        return self.symptoms_model.get_paginated_data(self.session, limit, page, payload)