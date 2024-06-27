import json

from sqlalchemy import Column, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from shared.database import base
from .QueriesMixin import QueriesMixin
from .SubSymptomsModel import SubSymptomsModel

class MedicalAppointmentsModel(QueriesMixin, base):
    __tablename__ = "medical_appointments"
    
    id = Column(Integer, primary_key=True)
    sub_symptom_id = Column(Integer, ForeignKey("sub_symptoms.id"), nullable=False)
    appointment_date = Column(TIMESTAMP, nullable=False)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    sub_symptom = relationship("SubSymptomsModel")
    
    def __init__(self, payload: dict = {}):
        self.sub_symptom_id = payload.get("sub_symptom_id", None)
        self.appointment_date = payload.get("appointment_date", None)        
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "sub_symptom": json.loads(str(self.sub_symptom)) if self.sub_symptom is not None else {},
                "appointment_date": str(self.appointment_date),
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )