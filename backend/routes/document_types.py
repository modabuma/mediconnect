from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request

from shared.loader import load_data
from shared.custom_exceptions import BadRoleError
from shared.schema_validation import validate_data
from controllers.DocumentTypesController import DocumentTypesController

document_types = Blueprint("document_types", __name__, url_prefix="/document_types")

@document_types.post("/create")
@jwt_required()
@load_data
def create(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] != "SU":
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    document_types_controller = DocumentTypesController(session)
    
    document_types_controller.create(payload)
    
    return jsonify(
        {
            "message": "Registro creado exitosamente."
        }
    ), 201


@document_types.put("/update")
@jwt_required()
@load_data
def update(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] != "SU":
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    document_types_controller = DocumentTypesController(session)
    
    document_types_controller.update(payload)
    
    return jsonify(
        {
            "message": "Registro actualizado exitosamente."
        }
    )


@document_types.delete("/delete")
@jwt_required()
@load_data
def delete(session, payload):
    identity = get_jwt_identity()
    
    if identity["role"] != "SU":
        raise BadRoleError("Usted no está autorizado para realizar esta acción.")
    
    document_types_controller = DocumentTypesController(session)
    
    document_types_controller.delete(payload)
    
    return jsonify(
        {
            "message": "Registro eliminado exitosamente."
        }
    )


@document_types.get("/get")
@jwt_required()
@load_data
def get(session):
    payload = {
        "limit": request.args.get("limit", default=5, type=int),
        "page": request.args.get("page", default=0, type=int),
        "id": request.args.get("id", type=int),
        "option": request.args.get("option", default=0, type=int),
        "code": request.args.get("code", type=str),
        "description_like": request.args.get("description", type=str),
        "initial_date": request.args.get("initial_date", type=str),
        "final_date": request.args.get("final_date", type=str)
    }
    
    validate_data(payload, "document_types", "get")
    
    document_types_controller = DocumentTypesController(session)
    
    response = document_types_controller.get(payload)
    
    return jsonify(
        {
            "message": "Exitoso.",
            "data": response
        }
    )