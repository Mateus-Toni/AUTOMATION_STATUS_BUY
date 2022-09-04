from datetime import datetime, timedelta
from random import randint

import logging
import re
from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required 
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_jwt_identity

from models.user.users import User
from dao import DataBaseTwoAuth
from dao import DataBaseUser

ACCESS_EXPIRES = ''

app = Flask(__name__)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Change this!
jwt = JWTManager(app)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    
    data = request.get_json()
    
    if data:
        
        name = data['name']
        last_name = data["last_name"]
        phone = data["phone"]
        email = data["email"]
        password = data["password"]
        birthday = data["birthday"]
        cpf = data["cpf"]
        
        user = User(
            name=name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
            birthday=birthday,
            cpf=cpf
            ).create_user_db()
        
        if user:
            
            return user
            
        else:
            
            return user
    
    else:
        
        return {"msg": "missing json data"}, 400


@app.route('/meu_perfil/<id_user>/update', methods=['GET', 'POST'])  # type: ignore
@jwt_required()
def update(id_user):
    
    id_user = get_jwt_identity()
    jti = get_jwt()['jti']
    
    if DataBaseTwoAuth.verify_if_token_is_revoked(id_user=id_user, jti=jti):
    
        if request.method == 'GET':
            
            data_user = DataBaseUser.get_user_by_id(id_user)
            
            if data_user:
                
                return {
                    "user_name": data_user['user_name'],
                    "last_name": data_user['last_name'],
                    "phone": data_user['phone'],
                    "email": data_user['email'],
                    "birthday": data_user['birthday'],
                    "cpf": data_user['cpf']
                }, 200
            
            else:
                
                return {"msg": "id not found"}, 400
            
            
        elif request.method == 'POST':
            
            try:
            
                data = request.get_json()
                
            except:
                
                return {"msg": "missing json data"}, 400
            
            else:
                
                if data:
                    
                    old_data_user = DataBaseUser.get_user_by_id(id_user)
                    
                    user = User(
                        name=old_data_user["user_name"],
                        last_name=old_data_user["last_name"],
                        phone=old_data_user["phone"],
                        email=old_data_user["email"],
                        password=old_data_user["user_password"],
                        birthday=old_data_user["birthday"],
                        cpf=old_data_user["cpf"]
                    ).update_user_db(
                        name=data["user_name"],
                        last_name=data["last_name"],
                        phone=data["phone"],
                        email=data["email"],
                        birthday=data["birthday"],
                        cpf=data["cpf"]   
                    )
                    
                    return jsonify(user)
                
                else:
                    
                    return {"msg": "wrong json data"}, 400
    
    else:
        
        return {'msg': 'jwt is revoked'} 
        
@app.route('/login', methods=['POST'])
def login():
    
    try:
        
        data = request.get_json()
        
    except Exception as erro_:
        
        return {'msg': 'missing json data'}, 400
    
    else:
        
        if data:
            
            email_user = data['email']
            password_user = data['password'].strip()
            
            password_db = DataBaseUser.get_password_by_email(email_user)
            
            if password_db:
            
                if check_password_hash(password=password_user, pwhash=password_db['user_password']):
                    
                    id_user = DataBaseUser.get_id_by_email(email_user)['id']
                    
                    two_auth = DataBaseTwoAuth.verify_if_two_auth_exists(id_user)
                    
                    if two_auth:
                        
                        date_now = datetime.now()
                        date_db = two_auth['timming'] 
                        
                        if (date_now - date_db).days > 2:
                            
                            try:
                                
                                DataBaseTwoAuth.delete_jwt_by_id_user(id_user)
                                DataBaseTwoAuth.delete_user_code(id_user)
                            
                            except Exception as erro_:
                                
                                logging.critical(erro_)
                                return {'msg': 'error in db'}
                                
                            else:
                                
                                try:
                                    
                                    access_token = create_access_token(
                                        identity=id_user,
                                        expires_delta=timedelta(days=3),
                                        additional_claims={'two_auth': False}
                                        )
                                    
                                    user_code_two_auth = str(randint(111111, 999999))
                                    
                                    DataBaseTwoAuth.create_jwt(id_user=id_user, jwt=access_token)
                                    DataBaseTwoAuth.create_code_two_auth(id_user=id_user, code=user_code_two_auth)
                                    
                                except Exception as erro_:
                                    
                                    logging.critical(erro_)
                                    
                                    return {'msg': 'error in db'}
                                
                                else:
                                    
                                    #manda email do código
                                    print(user_code_two_auth)
                                    
                                    return {'acess_token': access_token}, 200
                                
                        else:
                            
                            return {'acess_token': two_auth['jwt']}, 200
          
                    else:
                        
                        try:
                                
                            DataBaseTwoAuth.delete_jwt_by_id_user(id_user)
                            DataBaseTwoAuth.delete_user_code(id_user)
                        
                        except Exception as erro_:
                            
                            logging.critical(erro_)
                            return {'msg': 'error in db'}
                            
                        else:
                            
                            try:
                                
                                access_token = create_access_token(
                                        identity=id_user,
                                        expires_delta=timedelta(days=3),
                                        additional_claims={'two_auth': False}
                                        )
                                
                                user_code_two_auth = str(randint(111111, 999999))
                                
                                DataBaseTwoAuth.create_jwt(id_user=id_user, jwt=access_token)
                                DataBaseTwoAuth.create_code_two_auth(id_user=id_user, code=user_code_two_auth)
                                
                            except Exception as erro_:
                                
                                logging.critical(erro_)
                                return {'msg': 'error in db'}
                            
                            else:
                                
                                #manda email do código
                                print(user_code_two_auth)
                                
                                return {'acess_token': access_token}, 200
                
                else:
                    
                    return {'msg': 'invalid data'}, 401
                
            else:
                
                return {'msg': 'invalid data or user dont exists'}, 400
        
        else:
            
            return {'msg': 'missing json data'}, 400

    
@app.route('/two_auth', methods=['POST'])
@jwt_required()
def two_auth():
    
    two_auth = get_jwt()['two_auth']
    
    if two_auth:
        
        return {'msg': 'user have two factor'}, 200
    
    else:
        
        try:
            
            user_code_input = request.get_json()
            
        except Exception as erro_:
            
            return {'msg': 'missing json data'}, 400
        
        else:
            
            id_user = get_jwt_identity()
            
            user_code_db = DataBaseTwoAuth.get_code_two_auth_by_id(id_user)
            
            if user_code_db and user_code_input:
                
                if user_code_db['timming_code'] <= user_code_db['timming_code'] + timedelta(30):
                    
                    if str(user_code_db['user_code']) == str(user_code_input['code_jwt']):
                        
                        jti = get_jwt()['jti']
                        
                        revoked_old_token = DataBaseTwoAuth.revoked_token(id_user=id_user, jti=jti)
                        
                        if revoked_old_token:
                            
                            DataBaseTwoAuth.delete_jwt_by_id_user(id_user)
                            
                            new_access_token = create_access_token(
                                identity=id_user,
                                expires_delta=timedelta(days=3),
                                additional_claims={'two_auth': True}
                                )
                            
                            DataBaseTwoAuth.create_jwt(id_user=id_user, jwt=new_access_token)
                            
                            return {'access_token': new_access_token}, 200
                        
                        else:
                            
                            return {'msg': 'error in db'}
                    
                    else:
                        
                        return {'msg': 'missing input'}, 400
                
                else:
                    
                     return {'msg': 'code expired'}, 400
                
            else:
                
                return {'msg': 'missing data'}, 400
 
               
@app.route("/logout", methods=['DELETE'])
@jwt_required()
def modify_token():
    
    id_user = get_jwt_identity()
    jti = get_jwt()["jti"]
    
    status = DataBaseTwoAuth.revoked_token(id_user=id_user, jti=jti)
    
    if status:
    
        return {'msg': 'token revoked'}, 200
    
    else:
        
        return {'msg': 'error in db'}
        
                 

if __name__ == '__main__':

    app.run(debug=True)