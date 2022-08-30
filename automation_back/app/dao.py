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
            
    """def conn_db(self, query, fetch=False):
        
        if fetch:
            
            with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
                
                if cursor:
                    
                    try:
                    
                        cursor.execute(query)
                        data = cursor.fetchall()
                
                    except Exception as erro_:
                    
                        logging.warning('-'*50)
                        logging.warning(f'error in DB\nname error:\n{erro_}')
                        logging.warning('-'*50)
                        
                        return False
                
                    else:
                        
                        return data
        
        else:      
            
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
                        
                        return True"""
            
class DataBaseUser:
    
    @staticmethod
    def conn_db(query, fetch=False):
        
        if fetch:
            
            with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
                
                if cursor:
                    
                    try:
                    
                        cursor.execute(query)
                        data = cursor.fetchall()
                
                    except Exception as erro_:
                    
                        logging.warning('-'*50)
                        logging.warning(f'error in DB\nname error:\n{erro_}')
                        logging.warning('-'*50)
                        
                        return False
                
                    else:
                        
                        return data
        
        else:      
            
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
    def verify_if_user_exists(email, cpf, phone):
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
        
        return DataBaseUser.conn_db(query)
    
    @staticmethod          
    def update_user(obj, name, last_name, cpf, phone, email, birthday):
        
        query = f"""
        UPDATE users 
        SET user_name = '{name}',
        last_name = '{last_name}',
        birthday = '{birthday}',
        phone = '{phone}',
        email = '{email}',
        cpf = '{cpf}' 
        where
        phone = '{obj.phone}' and
        email = '{obj.email}' and
        cpf = '{obj.cpf}'
        """
        
        return DataBaseUser.conn_db(query)
    
    @staticmethod
    def get_user_data_db(email):
        
        query = f"""
        select * from users 
        where email = '{email}'
        """
        
        return DataBaseUser.conn_db(query, fetch=True)
    
    @staticmethod
    def get_user_by_id(id_user):
        
        query = f"""
        select * from users 
        where id = '{id_user}';
        """
        
        return DataBaseUser.conn_db(query, fetch=True)[0]
    
    @staticmethod
    def get_password_by_email(email):
        
        query = f"""
        select password from users
        where
        email = '{email}';
        """
        
        return DataBaseUser.conn_db(query, fetch=True)

class DataBaseCode:
    
    @staticmethod
    def conn_db(query, fetch=False):
        
        if fetch:
            
            with DataBase(NAME, PASSWORD, HOST, DATABASE) as cursor:
                
                if cursor:
                    
                    try:
                    
                        cursor.execute(query)
                        data = cursor.fetchall()
                
                    except Exception as erro_:
                    
                        logging.warning('-'*50)
                        logging.warning(f'error in DB\nname error:\n{erro_}')
                        logging.warning('-'*50)
                        
                        return False
                
                    else:
                        
                        return data
        
        else:      
            
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
    def create_code(obj):
        
        query = f"""
        insert into user_code values
        (
        default,
        '{obj.code}',
        '{obj.id_user}',
        '{obj.surname}',
        '{obj.status}',
        '{obj.type_mensage}',
        '{obj.timing_to_mensage}',
        );"""
        
        return DataBaseCode.conn_db(query)
    
    @staticmethod
    def verify_if_code_exists(obj):
        
        query = f"""
        select * from user_code
        where id_user = '{obj.id_user}' and
        code = '{obj.code}';
        """
        
        return DataBaseCode.conn_db(query, fetch=True)
    
    @staticmethod
    def update_code(obj, code,  surname, status, type_mensage, timing_to_mensage):
        
        query = f"""
        UPDATE users_code 
        SET code = '{code}',
        surname = '{surname}',
        status = '{status}',
        type_mensage = '{type_mensage}',
        timing_to_mensage = '{timing_to_mensage}' 
        where
        code = '{obj.code}' and
        id_user = '{obj.id_user}';
        """
        
        return DataBaseCode.conn_db(query)
    
    