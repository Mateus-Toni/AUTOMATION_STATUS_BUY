import defs_asb as funcao
import CRUD_banco_users as Banco
import json

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
        pass
else:
    pass
