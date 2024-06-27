import json

from sqlalchemy import Column, Integer, TIMESTAMP, func
from sqlalchemy.dialects.mysql import TINYINT

from shared.database import base
from .QueriesMixin import QueriesMixin

class VerificationCodesModel(QueriesMixin, base):
    __tablename__ = "verification_codes"
    
    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False, unique=True)
    active = Column(TINYINT, nullable=False, default=1)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, payload: dict = {}):
        self.code = payload.get("code", None)
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "code": self.code,
                "active": self.active,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )