import utils

class User:
    
    @utils.validate_data_user
    def __init__(self, name, last_name, phone, password, email, birthday):
        
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.birthday = birthday        
        
    def create_user_db(self):
        
        pass
    
    def soft_delete_user_db(self):
        
        pass
    
    def update_user_db(self):
        
        pass
    
    def get_user_db(self):
        
        pass
    
    

