def verifica(nick_name, nome, sobrenome, telefone, email, senha):
    import re
    c = 0
    erro = ''
    if re.match(r'[a-z1-9_!#$%@]+', nick_name):
        c += 1
    else:
        erro = 'Nome de usuário'

    if re.match(r"[a-zA-Z\s]+", nome):
        c += 1
    else:
        erro = 'Nome'

    if re.match(r"[a-zA-Z\s]+", sobrenome):
        c += 1
    else:
        erro = 'Sobre nome'

    if re.match(r"\([0-9]{2}\)\s?9\s?[0-9]{4}\s?-?\s?[0-9]{4}", telefone):
        c += 1
    else:
        erro = 'Telefone'

    if re.match(r"[a-zA-Z0-9]+@[a-z]+.[a-z]+.?b?r?", email):
        c += 1
    else:
        erro = 'E-mail'

    if re.match(r"[a-zA-Z0-9!@#$%&*]+", senha):
        c += 1
    else:
        erro = 'Senha'

    return (True, None) if c == 6 else (None, erro)


def verifica_user_email(user):
    import re
    return bool(re.match(r"[a-zA-Z0-9]+@[a-z]+.[a-z]+.?b?r?", user))
