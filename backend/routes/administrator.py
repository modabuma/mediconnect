from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request

from shared.loader import load_data
from shared.custom_exceptions import BadRoleError
from shared.schema_validation import validate_data
from controllers.AdministratorController import AdministratorController

administrator = Blueprint("administrator", __name__, url_prefix="/administrator")

@administrator.post("/send_verification_code")
@jwt_required()
@load_data
def send_verification_code(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    administrator_controller = AdministratorController(session)
    
    administrator_controller.send_verification_code(payload)
    
    return jsonify(
        {
            "message": "Código de verificación enviado con éxito."
        }
    )


@administrator.post("/verify_code")
@jwt_required()
@load_data
def verify_code(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    administrator_controller = AdministratorController(session)
    
    administrator_controller.verify_code(payload)
    
    return jsonify(
        {
            "message": "Código de verificación válido."
        }
    )
    

@administrator.post("/create_users")
@jwt_required()
@load_data
def create_users(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    administrator_controller = AdministratorController(session)
    
    administrator_controller.create_users(payload)
    
    return jsonify(
        {
            "message": "Registro creado exitosamente."
        }
    ), 201


@administrator.put("/update_users")
@jwt_required()
@load_data
def update_users(session, payload):
    administrator_controller = AdministratorController(session)
    
    administrator_controller.update_users(payload)
    
    return jsonify(
        {
            "message": "Registro actualizado exitosamente."
        }
    )


@administrator.delete("/delete_users")
@jwt_required()
@load_data
def delete_users(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] not in ["AD", "SU"]:
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    administrator_controller = AdministratorController(session)
    
    administrator_controller.delete_users(payload)
    
    return jsonify(
        {
            "message": "Registro eliminado exitosamente."
        }
    )


@administrator.get("/get_users")
@jwt_required()
@load_data
def get_users(session):
    
    payload = {
        "limit": request.args.get("limit", default=5, type=int),
        "page": request.args.get("page", default=0, type=int),
        "option": request.args.get("option", default=0, type=int),
        "id": request.args.get("id", type=int),
        "membership_id": request.args.get("membership_id", type=int),
        "role": request.args.get("role", type=int),
        "email_like": request.args.get("email", type=str),
        "document_like": request.args.get("document", type=str),
        "document_type": request.args.get("document_type", type=int),
        "names_like": request.args.get("names", type=str),
        "lastnames_like": request.args.get("lastnames", type=str),
        "department": request.args.get("department", type=int),
        "city": request.args.get("city", type=int),
        "address_like": request.args.get("address", type=str),
        "phone": request.args.get("phone", type=int),
        "initial_date": request.args.get("initial_date", type=str),
        "final_date": request.args.get("final_date", type=str)
    }
    
    validate_data(payload, "administrator", "get_users")
    
    administrator_controller = AdministratorController(session)
    
    response = administrator_controller.get_users(payload)
    
    return jsonify(
        {
            "message": "Exitoso.",
            "data": response
        }
    )