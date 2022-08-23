from flask import Flask, request, jsonify

from models.user.users import User
from dao import DataBaseUser


app = Flask(__name__)

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
    

@app.route('/login', methods=['POST'])
def login():
    
    return ''


@app.route('/meu_perfil/<id_user: int>/update', methods=['GET', 'POST'])  # type: ignore
def update(id_user):
    
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
        
        
        
    
    
    

if __name__ == '__main__':

    app.run(debug=True)