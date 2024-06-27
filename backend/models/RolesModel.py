import json

from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import sessionmaker

from shared.database import base
from .QueriesMixin import QueriesMixin

class RolesModel(QueriesMixin, base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, payload: dict = {}):
        self.code = payload.get("code", "")
        self.description = payload.get("description", "")
    
    def get_data_with_in_method(self, session: sessionmaker, filters: dict) -> object:
        
        filters = self.get_filters(filters)
        
        return session.query(self.__class__).filter(
            *filters,
            self.__class__.active == 1,
            self.__class__.code.in_(["DO", "PA"])
        ).first()
    
    def get_data_with_in_method_all(self, session: sessionmaker, filters: dict) -> object:
        
        filters = self.get_filters(filters)
        
        return session.query(self.__class__).filter(
            *filters,
            self.__class__.active == 1,
            self.__class__.code.in_(["DO", "PA"])
        ).all()
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "code": self.code,
                "description": self.description,
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )