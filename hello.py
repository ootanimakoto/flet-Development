from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user_name": "password123",
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/')
@auth.login_required
def index():
    return 'See gitlab.com.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
