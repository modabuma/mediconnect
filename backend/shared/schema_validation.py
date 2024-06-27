import json

from jsonschema import validate, FormatChecker, ValidationError

from .custom_exceptions import BadRequestError

def validate_data(
        instance: dict, file_name: str, object_name: str):
    
    try:
        with open(f"schema/{file_name}.json", "r") as file:
            schema = json.load(file)
            file.close()

        validate(instance = instance, schema = schema[object_name], format_checker = FormatChecker)
    
    except ValidationError as e:

        if len(e.path) > 0:
            if e.path[0] == "email":
                raise BadRequestError("El correo debe tener un formato válido.")

            elif e.path[0] == "initial_date":
                raise BadRequestError("La fecha inicial debe cumplir el formato YYYY-MM-DD.")
            
            elif e.path[0] == "final_date":
                raise BadRequestError("La fecha final debe cumplir el formato YYYY-MM-DD.")
            
        raise e