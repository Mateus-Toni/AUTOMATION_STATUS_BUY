
import mysql.connector

NAME = 'root'
PASSWORD = ''
NAME_DB = 'asb'
HOST = 'localhost'

query_create = """insert into usuarios values (default,'{}','{}','{}','{}','{}','{}')"""
query_read = """select * from usuarios"""
query_update = """update usuarios set {} = '{}' where {} = '{}'"""
query_delete = """delete from usuarios where id_user = '{}'"""


def open_db(user, password, host, database):
    try:
        db = mysql.connector.connect(user=user, password=password, host=host, database=database)
        cursor = db.cursor(dictionary=True)
    except:
        return None, None
    else:
        return db, cursor


def create_user(nick_name, nome, sobrenome, email, senha):
    from datetime import datetime
    data = datetime.today().date()
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        print(query_create.format(nick_name, nome, sobrenome, email, senha, data))
        cursor.execute(query_create.format(nick_name, nome, sobrenome, email, senha, data))
        db.commit()
        db.close()


def read_users():
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(query_read)
        users = cursor.fetchall()
        print(users)
        for dictionary in users:
            for key, value in dictionary.items():
                print(f'{key:-<30}> {value}')
        db.close()



def update_user(coluna, valor, modo, valor_modo):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(query_update.format(coluna,  valor, modo, valor_modo))
        db.commit()
        db.close()


def delete_user(id_usuario):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(query_delete.format(id_usuario))
        db.commit()
        db.close()

