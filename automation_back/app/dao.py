import logging

import mysql.connector

class DataBase:
    
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        
    def __enter__(self):
        try:
            self.db = mysql.connector.connect(user=self.user, password=self.password,
                                        host=self.host)
            self.cursor = self.db.cursor(dictionary=True)
            self.cursor.execute(f'use {self.database}')
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
            
