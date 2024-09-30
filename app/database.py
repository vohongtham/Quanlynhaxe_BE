from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

# Khởi tạo SQLAlchemy
db = SQLAlchemy()

ma = Marshmallow()

bcrypt = Bcrypt()

jwt = JWTManager()