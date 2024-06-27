from functools import wraps

from flask import request, jsonify
from jsonschema import ValidationError
from sqlalchemy.exc import IntegrityError

from .schema_validation import validate_data
from .database import get_session
from .custom_exceptions import (
    BadRequestError, BadCredentialsError, BadRoleError, 
    NotFoundError, FiltersDateError, DuplicatedFieldsError, CodeError)

def load_data(function):
    @wraps(function)
    def wrapper():
        try:            
            if request.method != "GET":
                payload = request.json
                
                module_name = (function.__module__).split(".")[-1]

                validate_data(payload, module_name, function.__name__)

                with get_session() as session:
                    return function(session, payload)

            else:
                with get_session() as session:
                    return function(session)
                
        except ValidationError as e:
            return jsonify({"message": e.message}), 400
        
        except BadRequestError as e:
            return jsonify({"message": str(e)}), 400
        
        except BadCredentialsError as e:
            return jsonify({"message": str(e)}), 401
        
        except BadRoleError as e:
            return jsonify({"message": str(e)}), 401
        
        except NotFoundError as e:
            return jsonify({"message": str(e)}), 404
        
        except FiltersDateError as e:
            return jsonify({"message": str(e)}), 400
        
        except DuplicatedFieldsError as e:
            return jsonify({"message": str(e)}), 400
        
        except CodeError as e:
            return jsonify({"message": str(e)}), 400
        
        except IntegrityError as e:
            error = str(e)
            print(error)
            if "Duplicate" in error:
                if "code" in error:
                    field = "código"
                
                if "email" in error:
                    field = "correo"
                
                return jsonify({"message": f"El {field} ingresado ya existe."}), 400
            
            elif "IntegrityError" in error:
                if "(`document_type`)" in error:
                    field = "tipo de documento"
                
                elif "(`symptom_id`)" in error:
                    field = "síntoma"
                    
                return jsonify({"message": f"El {field} que intenta ingresar no existe."}), 404 
                
    return wrapper