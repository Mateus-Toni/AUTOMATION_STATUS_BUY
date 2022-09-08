import requests

PATH = 'http://127.0.0.1:5000'
URL_LOGIN = '{path}/login'
URL_REGISTER = '{path}/register'
URL_UPDATE_USER = '{path}/meu_perfil/{id_user}/update'
URL_LOGOUT = '{path}/logout'
URL_TWO_AUTH = '{path}/two_auth'




def login_user(email, password):
    
    data = requests.post(
        url=URL_LOGIN.format(path=PATH),
        json={'email': email, 'password': password}
    )
    
    print(data.content)
    
login_user("lucaxnunex@teste.com", "amootoni")