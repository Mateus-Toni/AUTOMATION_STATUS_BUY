
from flask import Flask, request, jsonify

ACCESS_EXPIRES = ''

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Change this!


@app.route('/')
def index():
    
    return ''


if __name__ == '__main__':
    
    app.run(debug=True)