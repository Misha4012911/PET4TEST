from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
import codecs
from flask_login import UserMixin, LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

loginmanager = LoginManager(app)


class Users(db.Model):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'public'}
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)


@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/names", methods=['GET'])
def get_names():
    users = Users.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,  # Decode the name attribute
            'login': user.login
        }
        user_list.append(user_data)
        print({'users': user_list})
    return jsonify({'users': user_list})

if __name__ == "__main__":
    app.run()