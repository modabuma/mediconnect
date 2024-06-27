import json

from sqlalchemy.orm import sessionmaker

from models.DocumentTypesModel import DocumentTypesModel
from shared.custom_exceptions import NotFoundError

class DocumentTypesController:
    
    def __init__(self, session: sessionmaker):
        self.document_types_model = DocumentTypesModel()
        self.session = session
    
    def create(self, payload: dict):
        self.document_types_model.insert_data(self.session, payload)
    
    def update(self, payload: dict):
        id = payload.pop("id")
        
        response = self.document_types_model.update_data(self.session, {"id": id, "active": 1}, payload)
        
        if not response:
            raise NotFoundError("El tipo de documento que intenta editar no existe.")
    
    def delete(self, payload: dict):
        id = payload.pop("id")
        
        response = self.document_types_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("EL tipo de documento que intenta eliminar no existe.")
    
    def get(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")
        
        if payload["option"] == 1:
            return json.loads(str(self.document_types_model.get_data(self.session, response_type="all")))

        return self.document_types_model.get_paginated_data(self.session, limit, page, payload)