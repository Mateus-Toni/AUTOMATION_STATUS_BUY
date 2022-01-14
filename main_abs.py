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
            if k == 'first_name':
                nome = v
            if k == 'last_name':
                sobrenome = v
            if k == 'nick_name':
                nick_name = v
            if k == 'cellphone':
                telefone = v
            if k == 'email':
                email = v
            if k == 'password':
                senha = v


valido, erro = funcao.verifica(nick_name, nome, sobrenome, telefone, email, senha)

if valido:

    TEL = Banco.procura_telefone(telefone.replace(' ', '').replace('-', ''))
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

if is_email:

    db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:

        cursor.execute(f"""select email from usuarios where email = '{email}';""")
        existe = cursor.fetchone()

        if existe:

            cursor.execute(f"""select senha from usuarios where email = '{email}' """)
            valida_senha = cursor.fetchone()

            if valida_senha['senha'] == senha:
                print('login feito')

            else:
                print('login ou senha podem estar incorretos')

    else:
        print('E-mail pode estar incorreto')

else:

    db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
    if db:

        cursor.execute(f"""select nick_name from usuarios where nick_name = '{nick_name}';""")
        existe = cursor.fetchone()

        if existe:

            cursor.execute(f"""select senha from usuarios where nick_name = '{nick_name}' """)
            valida_senha = cursor.fetchone()

            if valida_senha['senha'] == senha:
                print('login feito')

            else:
                print('login ou senha podem estar incorretos')

    else:
        print('Nome de usuário pode estar incorreto')
