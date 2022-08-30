
import utils
from dao import DataBaseCode

class AllCodeUser:
    
    def __init__(self) -> None:
        
        pass


class Code:
    
    def __init__(self, code, id_user,  surname, status, type_mensage, timing_to_mensage):
        
        self.code = code 
        self.id_user = id_user
        self.surname = surname
        self.status = status
        self.type_mensage = type_mensage
        self.timing_to_mensage = timing_to_mensage
        
    def create_code_db(self):
        
        if DataBaseCode.verify_if_code_exists(self):
            
            return {'msg': 'code alredy exists'}, 400
        
        if utils.validate_data_code(self.code):
            
            if DataBaseCode.create_code(self):
                
                return {'msg': 'sucess'}, 200
                
            else:
                
                return {'msg': 'error in db'}, 400     
            
        else:
            
            return {'msg': 'invalid input'}, 400
        
        
    def update_code_db(self, code, surname, status, type_mensage, timing_to_mensage):
        
        if utils.validate_data_code(self.code):
            
            if DataBaseCode.update_code(self, code, surname, status, type_mensage, timing_to_mensage):
                
                return {'msg': 'sucess'}, 200
            
            else:
                
                return {'msg': 'error in db'}, 400
        
        else:
            
            return {'msg': 'invalid input'}, 400
    
    def delete_code_db(self):
        
        pass
    
        
        
        
        
    