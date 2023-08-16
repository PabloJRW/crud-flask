from flask import Flask
from app.auth import auth_bp


app = Flask(__name__, template_folder='templates')
app.register_blueprint(auth_bp, url_prefix='/auth')


if __name__=='__main__':
    app.run(debug=True)