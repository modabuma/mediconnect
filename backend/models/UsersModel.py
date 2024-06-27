import json

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import sessionmaker
import math
import bcrypt

from shared.custom_exceptions import NotFoundError
from shared.database import base
from .QueriesMixin import QueriesMixin
from .AdditionalDataModel import AdditionalDataModel
from .MembershipModel import MembershipModel
from .RolesModel import RolesModel

class UsersModel(QueriesMixin, base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    additional_data_id = Column(Integer, ForeignKey("additional_data.id"), nullable=False)
    membership_id = Column(Integer, ForeignKey("membership.id"), nullable=False)
    role = Column(Integer, ForeignKey("roles.id"), nullable=False)
    email = Column(String, nullable=False)
    password = Column(Text, nullable=False)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    additional_data = relationship("AdditionalDataModel")
    membership = relationship("MembershipModel")
    roles = relationship("RolesModel")
    
    def __init__(self, payload: dict = {}):
        self.additional_data_id = payload.get("additional_data_id", None)
        self.membership_id = payload.get("membership_id", None)
        self.role = payload.get("role", None)
        self.email = payload.get("email", "")
        self.password = self.hash_password(payload.get("password", ""))
    
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    def verify_password(self, password_: str) -> bool:
        return bcrypt.checkpw(password_.encode('utf-8'), self.password.encode('utf-8'))
    
    def get_paginated_data_with_join(
            self, session: sessionmaker, limit: int, 
            page: int, filters_main: dict = {}, filters_second: dict = {}) -> list:
        
        page -= 1 if page != 0 else 0
        limit = limit if limit >= 0 else 0
        
        filters_main = self.get_filters(filters_main)
        filters_second = self.get_filters(filters_second, AdditionalDataModel)
        
        records = session.query(self.__class__).join(
            AdditionalDataModel
        ).join(
            RolesModel
        ).filter(
            *filters_main,
            *filters_second,
            RolesModel.code.in_(["DO", "PA"]),
            self.__class__.active == 1
        ).limit(limit).offset(limit*page).all()

        if not records:
            raise NotFoundError("No se encontraron registros.")
        
        number_of_records = session.query(self.__class__).join(
            AdditionalDataModel
        ).join(
            RolesModel
        ).filter(
            *filters_main, 
            *filters_second, 
            RolesModel.code.in_(["DO", "PA"]),
            self.__class__.active == 1
        ).count()
        
        return {
            "number_of_records": number_of_records,
            "pages": math.ceil(number_of_records/limit),
            "records": json.loads(str(records))
        }
         
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "additional_data": json.loads(str(self.additional_data)) if self.additional_data is not None else {},
                "membership": json.loads(str(self.membership)) if self.membership is not None else {},
                "role": json.loads(str(self.roles)) if self.roles is not None else {},
                "email": self.email,
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )