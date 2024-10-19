from flask import Flask
import os
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = get_username()
    
    return f"<h1>Username: {username}</h1>"

def get_username():
    try:
        return os.getlogin()
    except:
        return os.getenv('USER') or os.getenv('USERNAME', getpass.getuser())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
