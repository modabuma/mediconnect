import json
import math
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from shared.custom_exceptions import NotFoundError, FiltersDateError

class QueriesMixin:
    
    def get_data(
            self, session: sessionmaker, filters: dict = {},
            response_type: str = "first") -> any:
        
        filters = self.get_filters(filters)
        
        return getattr(
            session.query(self.__class__).filter(*filters), response_type)()
    
    def get_paginated_data(
            self, session: sessionmaker, limit: int, 
            page: int, filters: dict = {}) -> list:
        
        page -= 1 if page != 0 else 0
        limit = limit if limit >= 0 else 0
        
        filters = self.get_filters(filters)
        
        records = session.query(self.__class__).filter(
            *filters, self.__class__.active == 1
        ).limit(limit).offset(limit*page).all()
        
        if not records:
            raise NotFoundError("No se encontraron registros.")
        
        number_of_records = session.query(self.__class__).filter(
            *filters, self.__class__.active == 1
        ).count()
        
        return {
            "number_of_records": number_of_records,
            "pages": math.ceil(number_of_records/limit),
            "records": json.loads(str(records))
        }
    
    def insert_data(
            self, session: sessionmaker, payload: dict) -> int:
        
        record = self.__class__(payload)
        
        session.add(record)

        session.commit()
        
        return record.id
    
    def update_data(
            self, session: sessionmaker, filters: dict,
            payload: dict) -> int:
        
        filters = self.get_filters(filters)
        
        response = session.query(self.__class__).filter(*filters).update(payload)
        
        session.commit()
        
        return response
    
    def exclude_none_values_from_filters(self, item: tuple) -> tuple:
        if item[1] is not None:
            if isinstance(item[1], str):
                if item[1].strip() != "":
                    return (item[0], item[1])

                else:
                    return None
                
            else:
                return (item[0], item[1]) 
            
        else:
            return None
    
    def get_date_filters(self, initial_date: str, final_date: str) -> list:
        aux = lambda date: datetime.strptime(date, "%Y-%m-%d").date() if date is not None else None
        now = datetime.now().date()
        
        initial_date = aux(initial_date)
        final_date = aux(final_date)

        if initial_date is not None and final_date is not None:
            if initial_date > now:
                raise FiltersDateError("La fecha inicial no puede ser mayor a la fecha actual.")
            
            elif final_date > now:
                raise FiltersDateError("La fecha final no puede ser mayor a la fecha actual.")
            
            elif initial_date > final_date:
                raise FiltersDateError("La fecha inicial no puede ser mayor a la fecha final.")
            
            else:
                return [
                    func.DATE(self.__class__.created_at) >= initial_date,
                    func.DATE(self.__class__.created_at) <= final_date
                ]
        
        elif initial_date is not None:
            if initial_date > now:
                raise FiltersDateError("La fecha inicial no puede ser mayor a la fecha actual.")
            
            else:
                return [
                    func.DATE(self.__class__.created_at) >= initial_date,
                ]
        
        elif final_date is not None:
            if final_date > now:
                raise FiltersDateError("La fecha final no puede ser mayor a la fecha actual.")
            
            else:
                return [
                    func.DATE(self.__class__.created_at) <= final_date,
                ]
        
        else:
            return []
    
    def get_filters(self, payload: dict, model: object = None) -> list:
        
        initial_date = payload.pop("initial_date", None)
        final_date = payload.pop("final_date", None)
        
        if model is None:
            model = self.__class__
            
        aux = dict(filter(self.exclude_none_values_from_filters, payload.items()))
        
        filters = list(map(
            lambda item: getattr(model, item[0]) == item[1] \
                if "like" not in item[0] else getattr(model, item[0].split("_")[0]).like(f"%{item[1]}%"), 
                aux.items()
        ))
        
        filters += self.get_date_filters(initial_date, final_date)
        
        return filters