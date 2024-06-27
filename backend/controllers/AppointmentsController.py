from sqlalchemy.orm import sessionmaker

from shared.custom_exceptions import NotFoundError
from models.MedicalAppointmentsModel import MedicalAppointmentsModel
from models.AdditionalDataAppointmentsModel import AdditionalDataAppointmentsModel

class AppointmentsController:
    
    def __init__(self, session: sessionmaker):
        self.additional_medical_appointments_model = AdditionalDataAppointmentsModel()
        self.session = session
    
    def create(self, payload: dict):      
        medical_appointments_model = MedicalAppointmentsModel()
        
        hour = payload.pop("hour")
        
        main_data = {
            "sub_symptom_id": payload.pop("sub_symptom_id"),
            "appointment_date": payload.pop("appointment_date"),
        }
        
        id_doctor = payload.pop("id_doctor")
        
        response = medical_appointments_model.insert_data(self.session, main_data)
        
        payload["medical_appointment_id"] = response
        
        self.additional_medical_appointments_model.insert_data(self.session, payload)
        
        payload["user_id"] = id_doctor
        
        self.additional_medical_appointments_model.insert_data(self.session, payload)

    def delete(self, payload: dict):
        id = payload.pop("id")
        medical_appointments_model = MedicalAppointmentsModel()
        
        response = medical_appointments_model.update_data(self.session, {"id": id, "active": 1}, {"active": 0})
        
        if not response:
            raise NotFoundError("La cita que intenta cancelar ya se encuentra cancelada.")
        
    def get(self, payload: dict):
        limit = payload.pop("limit")
        page = payload.pop("page")
        
        filters_main = {
            "user_id": payload.pop("user_id",),
            "user_id": payload.pop("doctor_id")    
        }
        
        return self.additional_medical_appointments_model.get_paginated_data_with_join(self.session, limit, page, filters_main, payload)