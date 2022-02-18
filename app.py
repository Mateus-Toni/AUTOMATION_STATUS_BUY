from flask import Flask, render_template, request, session, url_for, redirect
import defs_asb as funcao
import CRUD_banco_users as Banco

NAME = 'root'
PASSWORD = ''
NAME_DB = 'asb'
HOST = 'localhost'

app = Flask(__name__)
app.secret_key = 'mateus'


@app.route("/login")
def login():
    return render_template('loginnovo.html')


@app.route("/autenticar", methods=['POST', 'GET'])
def autenticar():
    if is_email := funcao.verifica_user_email(request.form['login']):
        db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
        if db:
            cursor.execute(f"""select email, senha, nick_name from usuarios where email = '{request.form['login']}'""")
            if not (lista_dados := cursor.fetchall()):
                return redirect(url_for('login'))
            for dicionario in lista_dados:
                email = dicionario['email']
                senha = dicionario['senha']
                nick = dicionario['nick_name']

            if request.form['senha'] != senha:
                return redirect(url_for('login'))
            session['usuario_logado'] = nick
            return redirect(url_for('home'))
    else:
        db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
        if db:
            cursor.execute(f"""select senha, nick_name from usuarios where nick_name = '{request.form['login']}'""")
            if not (lista_dados := cursor.fetchall()):
                return redirect(url_for('login'))
            for dicionario in lista_dados:
                senha = dicionario['senha']
                nick = dicionario['nick_name']

            if request.form['senha'] != senha:
                return redirect(url_for('login'))
            session['usuario_logado'] = nick
            return redirect(url_for('home'))
        

@app.route("/cadastro")
def cadastro():
    return render_template('cadastronovo.html')


@app.route("/criar", methods=['POST'])
def criar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    nick = request.form['nick_name']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    valido, erro = funcao.verifica(nick, nome, sobrenome, telefone, email, senha)
    if valido:
        TEL = Banco.procura_telefone(telefone)
        NICK_NAME = Banco.procura_nick(nick)
        EMAIL = Banco.procura_email(email)

        if TEL and NICK_NAME and EMAIL:
            Banco.create_user(nick, nome, sobrenome, telefone, email, senha)
            return redirect(url_for('login'))
        else:
            if not TEL:
                return redirect(url_for('cadastro'))
            
            if not NICK_NAME:
                return redirect(url_for('cadastro'))
            
            if not EMAIL:
                return redirect(url_for('cadastro'))

    else:
        return redirect(url_for('cadastro'))



@app.route("/logout",)
def logout():
    session['usuario_logado'] = None
    return redirect(url_for('index'))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    return render_template("home.html")


@app.route("/novocodigo", methods=['POST'])
def codigo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    import re
    codigo = request.form['codigo']
    apelido = request.form['apelido']
    nick = session['usuario_logado']
    if re.match(r'AA[1-9]{9}BR', codigo):
        Banco.guarda_cod(apelido, codigo, nick)
        return redirect(url_for('home'))
    return redirect(url_for('home'))
    

@app.route("/perfil", methods=['GET'])
def perfil():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    nick = session['usuario_logado']
    db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
    cursor.execute(f"select * from usuarios where nick_name = '{nick}'")
    user_list = cursor.fetchall()
    for user in user_list:
        id_user = user['id_user']
        nome = user['nome']
        sobrenome = user['sobrenome']
        email = user['email']
        telefone = user['telefone']
        senha = user['senha']
    session['id_user'] = id_user
    return render_template('perfil.html', nome=nome,nick=nick, sobrenome=sobrenome, email=email, telefone=telefone, senha=senha)

@app.route("/atualizar", methods=['POST'])
def autentincar():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login'))
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    nick_name = request.form['nick']
    email = request.form['email']
    telefone = request.form['telefone']
    senha = request.form['senha']
    session['usuario_logado'] = nick_name
    id_user = session['id_user']
    
    db, cursor = Banco.open_db(NAME, PASSWORD, HOST, NAME_DB)
    
    if db:
        cursor.execute(f"""update usuarios set nick_name = '{nick_name}', nome = '{nome}', sobrenome = '{sobrenome}', telefone = '{telefone}', email = '{email}', senha = '{senha}' 
                       where id_user = '{id_user}';""")
        db.commit()
        db.close()
        
        return redirect(url_for('home'))
    
    
@app.route("/about")
def about():
    return render_template("about.html")
    

if __name__ == "__main__":
    app.run(debug=True)