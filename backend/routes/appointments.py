from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, request

from shared.loader import load_data
from shared.schema_validation import validate_data
from controllers.AppointmentsController import AppointmentsController
 
appointments = Blueprint("appointments", __name__, url_prefix="/appointments")

@appointments.post("/create")
@jwt_required()
@load_data
def create(session, payload):
    appointments_controller = AppointmentsController(session)
    
    appointments_controller.create(payload)
    
    return jsonify(
        {
            "message": "Registro creado exitosamente."
        }
    ), 201
    
@appointments.delete("/delete")
@jwt_required()
@load_data
def delete(session, payload):
    appointments_controller = AppointmentsController(session)
    
    appointments_controller.delete(payload)
    
    return jsonify(
        {
            "message": "Cita cancelada exitosamente."
        }
    )
    
@appointments.get("/get")
@jwt_required()
@load_data
def get(session):
    payload = {
        "limit": request.args.get("limit", default=5, type=int),
        "page": request.args.get("page", default=0, type=int),
        "user_id": request.args.get("user_id", type=int),
        "doctor_id": request.args.get("doctor_id", type=int),
        "sub_symptom_id": request.args.get("sub_symptom_id", type=int),
        "initial_date": request.args.get("initial_date", type=str),
        "final_date": request.args.get("final_date", type=str)
    }
    
    validate_data(payload, "appointments", "get")
    
    appointments_controller = AppointmentsController(session)
    
    response = appointments_controller.get(payload)
    
    return jsonify(
        {
            "message": "Exitoso.",
            "data": response
        }
    )