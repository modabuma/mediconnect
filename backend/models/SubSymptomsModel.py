import json

from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

from shared.database import base
from .QueriesMixin import QueriesMixin
from .SymptomsModel import SymptomsModel

class SubSymptomsModel(QueriesMixin, base):
    __tablename__ = "sub_symptoms"
    
    id = Column(Integer, primary_key=True)
    symptom_id = Column(String, ForeignKey("symptoms.id"), nullable=False)
    code = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    symptom = relationship("SymptomsModel")
    
    def __init__(self, payload: dict = {}):
        self.symptom_id = payload.get("symptom_id", None)
        self.code = payload.get("code", "")
        self.description = payload.get("description", "")
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "symptom": json.loads(str(self.symptom)) if self.symptom is not None else {},
                "code": self.code,
                "description": self.description,
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )