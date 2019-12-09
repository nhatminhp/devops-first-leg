from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)

# load dotenv in the base root
APP_ROOT = os.path.join(os.path.dirname(__file__), '.')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

# app.config['MYSQL_HOST'] = 'db-annotator.cmj2loi1ze2d.ap-southeast-1.rds.amazonaws.com:3306'
# app.config['MYSQL_USER'] = 'admin'
# app.config['MYSQL_PASSWORD'] = '1234567890'
# app.config['MYSQL_DB'] = 'auth-db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:1234567890@db-annotator.cmj2loi1ze2d.ap-southeast-1.rds.amazonaws.com:3306/auth-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'
db = SQLAlchemy(app)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


app.config['JWT_SECRET_KEY'] = 'jwt-secret-key'
jwt = JWTManager(app)


import views, models, resources

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

