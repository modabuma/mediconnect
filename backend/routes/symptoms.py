from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request

from shared.loader import load_data
from shared.custom_exceptions import BadRoleError
from shared.schema_validation import validate_data
from controllers.SymptomsController import SymptomsController

symptoms = Blueprint("symptoms", __name__, url_prefix="/symptoms")

@symptoms.post("/create")
@jwt_required()
@load_data
def create(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    symptoms_controller = SymptomsController(session)
    
    symptoms_controller.create(payload)
    
    return jsonify(
        {
            "message": "Registro creado exitosamente."
        }
    ), 201


@symptoms.put("/update")
@jwt_required()
@load_data
def update(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    symptoms_controller = SymptomsController(session)
    
    symptoms_controller.update(payload)
    
    return jsonify(
        {
            "message": "Registro actualizado exitosamente."
        }
    )


@symptoms.delete("/delete")
@jwt_required()
@load_data
def delete(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    symptoms_controller = SymptomsController(session)
    
    symptoms_controller.delete(payload)
    
    return jsonify(
        {
            "message": "Registro eliminado exitosamente."
        }
    )


@symptoms.get("/get")
@jwt_required()
@load_data
def get(session):
    payload = {
        "limit": request.args.get("limit", default=5, type=int),
        "page": request.args.get("page", default=0, type=int),
        "option": request.args.get("option", default=0, type=int),
        "id": request.args.get("id", type=int),
        "code": request.args.get("code", type=str),
        "description_like": request.args.get("description", type=str),
        "initial_date": request.args.get("initial_date", type=str),
        "final_date": request.args.get("final_date", type=str)
    }
    
    validate_data(payload, "symptoms", "get")
    
    symptoms_controller = SymptomsController(session)
    
    response = symptoms_controller.get(payload)
    
    return jsonify(
        {
            "message": "Exitoso.",
            "data": response
        }
    )