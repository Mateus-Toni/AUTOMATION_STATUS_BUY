import defs_asb as funcao
import mysql.connector

NAME = 'root'
PASSWORD = ''
NAME_DB = 'asb'
HOST = 'localhost'

query_create = """insert into usuarios values (default,'{}','{}','{}','{}','{}','{}','{}')"""
query_read = """select * from usuarios"""
query_update = """update usuarios set {} = '{}' where {} = '{}'"""
query_delete = """delete from usuarios where id_user = '{}'"""


def open_db(user, password, host, database):
    try:
        db = mysql.connector.connect(user=user, password=password,
                                     host=host, database=database)
        cursor = db.cursor(dictionary=True)
    except:
        return None, None
    else:
        return db, cursor


def create_user(nick_name, nome, sobrenome, telefone, email, senha):
    from datetime import datetime
    data = datetime.today().date()
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(query_create.format(nick_name, nome, sobrenome, telefone,
                                           email, senha, data))
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



def procura_nick(nick_name):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(f"""select nick_name from usuarios 
        where nick_name = '{nick_name}'""")
        var = cursor.fetchone()
        return not var


def procura_email(email):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(f"""select email from usuarios 
            where email = '{email}'""")
        var = cursor.fetchone()
        return not var


def procura_telefone(telefone):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:
        cursor.execute(f"""select telefone from usuarios 
                where telefone = '{telefone}'""")
        var = cursor.fetchone()
        return not var


def mostra_telefone(cellphone):

    lista = list(cellphone)

    lista.insert(4, ' ')
    lista.insert(6, ' ')
    lista.insert(11, '-')
    return ''.join(lista)


def guarda_cod(apelido, codigo, nick_name_logado):
    import defs_asb as funcao
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)

    if db:

        cursor.execute(f"""select id_user from usuarios where nick_name = '{nick_name_logado}'""")
        id_user = funcao.retorna_num(cursor.fetchone())
        cursor.execute(f"""insert into codigo values (default, '{codigo.upper()}', '{id_user}', '{apelido}')""")
        db.commit()
        db.close()
        
        
def return_user_id(nick):
    db, cursor = open_db(NAME, PASSWORD, HOST, NAME_DB)
    
    if db:
        
        cursor.execute(f"select id_user from usuarios where nick_name = '{nick}'")
        id_user = cursor.fetchall()
        id_user = id_user['id_user']
        return id_user