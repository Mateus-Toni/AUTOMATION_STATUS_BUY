import logging

import mysql.connector

from parameters import NAME, DATABASE, HOST, PASSWORD

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
            
class DataBaseUser:
    
    @staticmethod
    def verify_if_data_exists(email, cpf, phone):
        query = f"""
        select email, cpf, phone from users
        where 
        email='{email}' 
        or 
        cpf='{cpf}'
        or 
        phone='{phone}';
        """

        with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
            
            if cursor:
                
                try:
                
                    cursor.execute(query)
                    exists = bool(cursor.fetchall())
            
                except Exception as erro_:
                
                    logging.warning('-'*50)
                    logging.warning(f'error in DB\nname error:\n{erro_}')
                    logging.warning('-'*50)
                    
                    return False
            
                else:
                    
                    return exists

    @staticmethod
    def crate_user(obj):
        
        query = f"""
        insert into users values
        (
        default,
        '{obj.name}',
        '{obj.last_name}',
        '{obj.birthday}',
        '{obj.password}',
        '{obj.phone}',
        '{obj.email}',
        '{obj.cpf}'
        );"""
        
        with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
            
            if cursor:
                
                try:
                    
                    cursor.execute(query)
                
                except Exception as erro_:
                    
                    logging.warning('-'*50)
                    logging.warning(f'error in DB\nname error:\n{erro_}')
                    logging.warning('-'*50)
                    
                    return False
                
                else:
                    
                    return True
    
    @staticmethod          
    def update_user(obj, name, last_name, cpf, phone, password, email, birthday):
        
        query = f"""
        UPDATE users
        SET name = '{name}',
        last_name = '{last_name}',
        birthday = '{birthday}',
        password = '{password}',
        phone = '{phone}',
        email = '{email}',
        cpf = '{cpf}'
        WHERE 
        phone = '{obj.phone}'
        email = '{obj.email}'
        cpf = '{obj.cpf}';
        """
        
        with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
            
            if cursor:
                
                try:
                    
                    cursor.execute(query)
                
                except Exception as erro_:
                    
                    logging.warning('-'*50)
                    logging.warning(f'error in DB\nname error:\n{erro_}')
                    logging.warning('-'*50)
                    
                    return False
                
                else:
                    
                    return True
    
                
              