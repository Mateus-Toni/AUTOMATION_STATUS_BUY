

import defs_asb as funcao
import CRUD_banco_users as Banco
import json

#costantes

NAME = 'root'
PASSWORD = ''
NAME_DB = 'asb'
HOST = 'localhost'

# cadastro

with open('users.json', 'r+') as arq:
    var = json.load(arq)
    for dicio in var:
        for k, v in dicio.items():
            if k == 'cellphone':
                telefone = v.replace(' ', '').replace('-', '')
            elif k == 'email':
                email = v
            elif k == 'first_name':
                nome = v
            elif k == 'last_name':
                sobrenome = v
            elif k == 'nick_name':
                nick_name = v
            elif k == 'password':
                senha = v


valido, erro = funcao.verifica(nick_name, nome, sobrenome, telefone, email, senha)

if valido:

    TEL = Banco.procura_telefone(telefone)
    NICK = Banco.procura_nick(nick_name)
    EMAIL = Banco.procura_email(email)

    if TEL and NICK and EMAIL:

        Banco.create_user(nick_name, nome, sobrenome, telefone, email, senha)

    else:

        if not TEL:
            print('Telefone em uso')

        if not NICK:
            print('Nome de usuário em uso')

        if not EMAIL:
            print('E-mail em uso')

else:

    print(f'{erro} não é válido')

# lógica login

is_email = funcao.verifica_user_email(email)

db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)

if db:

    if is_email:
        cursor.execute(f"select id_user from usuarios where email = '{email}';")
    else:
        cursor.execute(f"select id_user from usuarios where nick_name = '{nick_name}';")


    if ID := cursor.fetchone():
        cursor.execute(f"""select senha from usuarios where id_user = '{ID['id_user']}';""")
        valida_senha = cursor.fetchone()


        if valida_senha['senha'] == senha:
            print('login feito')
        else:
            print('login ou senha podem estar incorretos')
else:
    print("login ou senha podem estar incorretos")

# lógica para guardar o código de rastreio no banco de dados

codigo = 'AA123456789BR'

nick_name_logado = nick_name

db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)

if db:

    cursor.execute(f"""select id_user from usuarios where nick_name = '{nick_name_logado}'""")
    id_user = funcao.retorna_num(cursor.fetchone())
    cursor.execute(f"""insert into codigo values (default, '{codigo.upper()}', '{id_user}')""")
    db.commit()
    db.close()


