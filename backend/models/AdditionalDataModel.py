import json

from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship

from .QueriesMixin import QueriesMixin
from .DocumentTypesModel import DocumentTypesModel
from .UsersModel import base

class AdditionalDataModel(QueriesMixin, base):
    __tablename__ = "additional_data"
    
    id = Column(Integer, primary_key=True)
    document = Column(String, nullable=False)
    document_type = Column(Integer, ForeignKey("document_types.id"), nullable=False)
    names = Column(String, nullable=False)
    lastnames = Column(String, nullable=False)
    department = Column(Integer, nullable=False)
    city = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    document_types = relationship("DocumentTypesModel") 
    
    def __init__(self, payload: dict = {}):
        self.document = payload.get("document", "")
        self.document_type = payload.get("document_type", None)
        self.names = payload.get("names", "")
        self.lastnames = payload.get("lastnames", "")
        self.department = payload.get("department", None)
        self.city = payload.get("city", None)
        self.address = payload.get("address", "")
        self.phone = payload.get("phone", 0)
        
    def __repr__(self) -> str:
        return json.dumps(
            {
                "id": self.id,
                "document": self.document,
                "document_type": json.loads(str(self.document_types)) if self.document_types is not None else {},
                "names": self.names,
                "lastnames": self.lastnames,
                "department": self.department,
                "city": self.city,
                "address": self.address,
                "phone": self.phone,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)
            }
        )
        