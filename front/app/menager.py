import requests

PATH = 'http://127.0.0.1:5000'

URL_LOGIN = '{path}/login'

URL_REGISTER = '{path}/register'

URL_UPDATE_USER = '{path}/meu_perfil/{id_user}/update'

URL_LOGOUT = '{path}/logout'

URL_TWO_AUTH = '{path}/two_auth'

URL_VERIFY_TOKEN = '{path}/verify_token'


def login_user(email, password):
    
    data = requests.post(
        
        url=URL_LOGIN.format(path=PATH),
        json={'email': email, 'password': password}
        
    )
    
    return data

def register(data_json):
    
    data = requests.post(
        
        url=URL_REGISTER.format(path=PATH),
        json=data_json
        
    )
    
    return data
    
def get_update_user(id_user, session):
    
    data = requests.get(
        
        url=URL_UPDATE_USER.format(path=PATH, id_user=id_user),
        headers={'Authorization': f'Bearer {session["token"]}'}
        
    )
    
    return data

def post_update_user(id_user, session, data_json):
    
    data = requests.post(
        
        url=URL_UPDATE_USER.format(path=PATH, id_user=id_user),
        headers={'Authorization': f'Bearer {session["token"]}'},
        json=data_json
        
    )
    
    return data

def two_auth(session, code):
    
    data = requests.post(
        
        url=URL_TWO_AUTH.format(path=PATH),
        headers={'Authorization': f'Bearer {session["token"]}'},
        json={'code': code}
        
    )
    
    return data
    
def logout(session):
    
    data = requests.delete(
        
        url=URL_LOGOUT.format(path=PATH),
        headers={'Authorization': f'Bearer {session["token"]}'}
        
    )
    
    return data
        
def verify_token(session):
    
    data = requests.post(
        
        url=URL_VERIFY_TOKEN.format(path=PATH),
        headers={'Authorization': f'Bearer {session["token"]}'}
        
    )
    
    return data
    