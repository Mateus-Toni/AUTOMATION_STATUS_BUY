
import json
import logging
from flask import Flask, request, jsonify, session

import menager

ACCESS_EXPIRES = ''

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Change this!
app.secret_key = 'secret key'


@app.route('/')
def index():
    
    return {'msg': 'index'}


@app.route('/cadastro', methods=['POST'])
def register():
    
    # name = request.form['name']
    # last_name = request.form['last_name']
    # phone = request.form['phone']
    # email = request.form['email']
    # password = request.form['password']
    # birthday = request.form['birthday']
    # cpf = request.form['cpf']
    
    #formatar dados do usuário
    
    name = 'mateus'
    last_name = 'toni'
    phone = '(11)912341234'
    email = 'mateus@gmail.com'
    password = '123'
    birthday = '2022-05-01'
    cpf = '123.123.123-12'
    
    data_json = {
        
        'name': name,
        "last_name": last_name,
        "phone": phone,
        "email": email,
        "password": password,
        "birthday": birthday,
        "cpf": cpf
        
    }
    
    response = menager.register(data_json)
    
    if response.status_code == 200:#sucess create
        
        #redirect to login page
        #flash mensage ('cadastro feito com sucesso')
        return response.json()
    
    elif response.json()['msg'] == 'user alredy exists':#user exists
        
        #redirect to register page
        #flash mensage ('este email ja esta sendo usado')
        return response.json()
    
    elif response.json()['msg'] == 'invalid input': #error in input
        
        #redirect to register page
        #flash mensage ('preencha todos os campos corretamente')
        return response.json()
    
    elif response.json()['msg'] == 'missing json data': # missing data
        
        #redirect to register page
        #flash mensage ('preencha todos os campos')
        return response.json()
    
    else:
        
        logging.critical(response.json())
        return response.json() # page 404


@app.route('/login', methods=['POST'])
def login():
    
    email = 'mateus@gmail.com'
    password = '123'
    
    response = menager.login_user(email=email, password=password)
    
    if response.status_code == 200:
        
        session['token'] = response.json()['access_token']
        
        return response.json() #redirect to two auth code page
    
    
    return response.json()

@app.route('/code_two_auth', methods=['POST'])
def validate():
    
    user_code = '111186'
    
    response = menager.two_auth(session=session, code=user_code)
    
    print(response)
    
    if response:
        return response.json()
    else:
        return {'msg': 'erro'}, 400


if __name__ == '__main__':
    
    app.run(debug=True, port=3000)