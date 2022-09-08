import mysql.connector 
from automation_back.app.parameters import DATABASE, HOST, NAME, PASSWORD
import logging

class DataBase:
    
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        
    def __enter__(self):
        
        try:
            
            self.db = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host
                )
            self.cursor = self.db.cursor(dictionary=True)
            self.cursor.execute(f'use {self.database};')
        
        except Exception as erro:
            
            logging.critical(erro)
       
        else:
            
            return self.cursor

    def __exit__(self, *args):
        
        try:
            
            self.db.commit()
            self.db.close()
            
        except Exception as erro:
            
            logging.critical(erro)

def get_user_by_id(id_user):
        
        query = f"""
        select * from users 
        where id = '{id_user}';
        """
        
        with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
                
            if cursor:
                
                try:
                
                    cursor.execute(query)
                    data = cursor.fetchone()
            
                except Exception as erro_:
                
                    logging.warning('-'*50)
                    logging.warning(f'error in DB\nname error:\n{erro_}')
                    logging.warning('-'*50)
                    
                    return False
            
                else:
                    
                    return data




