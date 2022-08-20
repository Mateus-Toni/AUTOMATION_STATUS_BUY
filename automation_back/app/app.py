from flask import Flask

from models.user.users import User


app = Flask(__name__)

@app.route('/')
def index():
    return 'ola'

if __name__ == '__main__':

    app.run(debug=True)