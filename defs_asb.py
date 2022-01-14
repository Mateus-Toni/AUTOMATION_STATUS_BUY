def verifica(nick_name, nome, sobrenome, telefone, email, senha):
    import re
    c = 0
    erro = ''
    if re.match(r'[a-z1-9_!#$%@]+', nick_name):
        c += 1
    else:
        erro = 'nick_name'

    if re.match(r"[a-zA-Z\s]+", nome):
        c += 1
    else:
        erro = 'nome'

    if re.match(r"[a-zA-Z\s]+", sobrenome):
        c += 1
    else:
        erro = 'sobrenome'

    if re.match(r"\([0-9]{2}\)\s?9\s?[0-9]{4}\s?-?\s?[0-9]{4}", telefone):
        c += 1
    else:
        erro = 'telefone'

    if re.match(r"[a-zA-Z0-9]+@[a-z]+.[a-z]+.?b?r?", email):
        c += 1
    else:
        erro = 'email'

    if re.match(r"[a-zA-Z0-9!@#$%&*]+", senha):
        c += 1
    else:
        erro = 'senha'

    if c == 6:
        return True, None
    else:
        return None, erro


