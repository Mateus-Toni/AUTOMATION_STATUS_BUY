import utils
from dao import DataBaseUser

class User:
    
    def __init__(self, name, last_name, cpf, phone, password, email, birthday):
        
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.birthday = birthday    
        self.cpf = cpf    
    
    def create_user_db(self):
        
        exists = DataBaseUser.verify_if_data_exists(
            cpf=self.cpf, 
            email=self.email, 
            phone=self.phone
            )
        
        if exists:
            
           return {'msg': 'user alredy exists'}, 400
       
        else:
            
            valid = utils.validate_data(
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
                    
                    return {'msg': 'error in '}, 400     
            
            else:
                
                return {'msg': 'invalid input'}, 400
            
                
    def soft_delete_user_db(self):
        
        pass
    
    
    def update_user_db(self, name, last_name, cpf, phone, password, email, birthday):
        
        valid = utils.validate_data(
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
                password,
                email,
                birthday
                )
            
            if status:
              
                return {'msg': 'user updated'}, 200   
                
            else:
                    
                return {'msg': 'error in db'}, 400     
            
        else:
            
            return {'msg': 'invalid input'}, 400
    
    
    

