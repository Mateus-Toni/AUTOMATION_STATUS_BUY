from flask import Flask

from models.user.users import User


app = Flask(__name__)

user = User(name='adads',phone=1321, email=12312,password=123,birthday=123, last_name=123)

@app.route('/')
def index():
    return 'ola'

if __name__ == '__main__':

    app.run(debug=True)