import logging
from datetime import datetime

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
        select user_password from users
        where
        email = '{email}';
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

    @staticmethod
    def get_id_by_email(email):
        
        query = f"""
        select id from users where email = '{email}';
        """
        
        return DataBaseUser.conn_db(query, fetch=True)[0]


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
    
    
class DataBaseTwoAuth:
    
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
    def verify_if_two_auth_exists(id_user):
        
        query = f"""
        select * from two_auth where id_user = '{id_user}'
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
                
    @staticmethod
    def delete_jwt_by_id_user(id_user):
        
        query = f"""
        delete from two_auth where id_user = '{id_user}';
        """

        return DataBaseTwoAuth.conn_db(query)
        
    @staticmethod
    def create_jwt(jwt, id_user):
        
        date_now = datetime.now().date()
        
        query = f"""
        insert into two_auth values 
        ('{id_user}', '{jwt}', '{date_now}');
        """
        
        return DataBaseTwoAuth.conn_db(query)
    
    @staticmethod
    def delete_user_code(id_user):
        
        query = f"""
        delete from user_code_two_auth 
        where id_user = '{id_user}';
        """

        return DataBaseTwoAuth.conn_db(query)
    
    @staticmethod
    def create_code_two_auth(code, id_user):
        
        date_now = datetime.now().date()
        
        query = f"""
        insert into user_code_two_auth values 
        ('{id_user}', '{code}', '{date_now}');
        """

        return DataBaseTwoAuth.conn_db(query)
    
    @staticmethod
    def get_code_two_auth_by_id(id_user):
        
        query = f"""
        select * from user_code_two_auth
        where id_user = '{id_user}';
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
        
    @staticmethod
    def verify_if_token_is_revoked(id_user, jti):
        
        query = f"""
        select * from revoket_jwt
        where id_user = '{id_user}' and
        jti = '{jti}';
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
         
    @staticmethod
    def revoked_token(id_user, jti):
        
        date_now = datetime.now().date()
        
        query = f"""
        insert into revoked_jwt
        values ('{id_user}', '{jti}', '{date_now}');
        """
        
        return DataBaseTwoAuth.conn_db(query)
    
    
    
    