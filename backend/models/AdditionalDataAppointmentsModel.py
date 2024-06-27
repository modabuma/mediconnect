import json
import math

from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from shared.database import base
from shared.custom_exceptions import NotFoundError
from .QueriesMixin import QueriesMixin
from .UsersModel import UsersModel
from .MedicalAppointmentsModel import MedicalAppointmentsModel


class AdditionalDataAppointmentsModel(QueriesMixin, base):
    __tablename__ = "additional_data_appointments"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    medical_appointment_id = Column(Integer, ForeignKey("medical_appointments.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    user = relationship("UsersModel")
    medical_appointment = relationship("MedicalAppointmentsModel")
    
    def __init__(self, payload: dict = {}):
        self.user_id = payload.get("user_id", None)
        self.medical_appointment_id = payload.get("medical_appointment_id", None)
    
    def get_paginated_data_with_join(
            self, session: sessionmaker, limit: int, 
            page: int, filters_main: dict = {}, filters_second: dict = {}) -> list:
        
        page -= 1 if page != 0 else 0
        limit = limit if limit >= 0 else 0
        
        filters_main = self.get_filters(filters_main)
        filters_second = self.get_filters(filters_second, MedicalAppointmentsModel)
        
        records = session.query(self.__class__).join(
            MedicalAppointmentsModel
        ).filter(
            *filters_main,
            *filters_second,
            MedicalAppointmentsModel.active == 1
        ).limit(limit).offset(limit*page).all()

        if not records:
            raise NotFoundError("No se encontraron registros.")
        
        number_of_records = session.query(self.__class__).join(
            MedicalAppointmentsModel
        ).filter(
            *filters_main,
            *filters_second,
            MedicalAppointmentsModel.active == 1
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
                "user": json.loads(str(self.user)) if self.user is not None else {},
                "medical_appointment": json.loads(str(self.medical_appointment)) if self.medical_appointment is not None else {},
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )
        