from werkzeug.security import generate_password_hash

import utils
from dao import DataBaseUser

class User:
    
    def __init__(self, name, last_name, cpf, phone, password, email, birthday):
        
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = generate_password_hash(password=password)
        self.birthday = birthday    
        self.cpf = cpf    
    
    def create_user_db(self):
        
        exists = DataBaseUser.verify_if_user_exists(
            cpf=self.cpf, 
            email=self.email, 
            phone=self.phone
            )
        
        if exists:
            
           return {'msg': 'user alredy exists'}, 400
       
        else:
            
            valid = utils.validate_data_user(
                cpf=self.cpf, 
                email=self.email, 
                phone=self.phone, 
                birthday=self.birthday
                )
            
            if valid:
            
                status = DataBaseUser.crate_user(self)
                
                if status:            
                    
                    return {'msg': 'user created'}, 200   
                
                else:
                    
                    return {'msg': 'error in db'}, 400     
            
            else:
                
                return {'msg': 'invalid input'}, 400
            
                
    def soft_delete_user_db(self):
        
        pass
    

    def update_user_db(self, name, last_name, cpf, phone, email, birthday):
        
        valid = utils.validate_data_user(
                cpf=cpf, 
                email=email, 
                phone=phone, 
                birthday=birthday
                )

        if valid:
            
            status = DataBaseUser.update_user(
                self,
                name,
                last_name,
                cpf,
                phone,
                email,
                birthday
                )
            
            if status:
              
                return {'msg': 'user updated'}, 200   
                
            else:
                    
                return {'msg': 'error in db'}, 400     
            
        else:
            
            return {'msg': 'invalid input'}, 400


    def get_user_id_by_email(self):
        
        return DataBaseUser.get_id_by_email(self.email)  
        
    
        