from datetime import datetime
import mysql.connector

NAME = 'root'
PASSWORD = ''
NAME_DB = 'asb'
HOST = 'localhost'


def open_db(user, password, host, database):
    try:
        db = mysql.connector.connect(user=user,  password=password, host=host, database=database)
        cursor = db.cursor()
    except:
        return None, None
    else:
        return db, cursor




query_create = """insert into usuarios values ('{}','{}','{}','{}','{}','{}')"""
query_read = """select * from usuários"""
query_update = """update usuarios set {} = {} where id_user = {}"""
query_delete = """delete {} from usuarios"""



