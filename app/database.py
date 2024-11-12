from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail

# Khởi tạo SQLAlchemy
db = SQLAlchemy() # Đối tượng quản lý cơ sở dữ liệu

ma = Marshmallow() # Đối tượng hỗ trợ serialization/deserialization

bcrypt = Bcrypt() # Đối tượng để mã hóa mật khẩu

jwt = JWTManager() # Đối tượng quản lý JWT

# Khởi tạo đối tượng Mail
mail = Mail()