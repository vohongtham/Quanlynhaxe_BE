# class Config:
#     SECRET_KEY = 'app_aip'
#     SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/qlnhaxe'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  Add other configurations as needed

import os
from dotenv import load_dotenv
from datetime import timedelta

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('KEY')  # Load SECRET_KEY from .env file
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Load database URL from .env file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    # Set JWT token expiration to 24 hours
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    # Cấu hình gửi email
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = os.getenv('MAIL_PORT')
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') == 'True'  # Đảm bảo là kiểu boolean
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    # Thiết lập địa chỉ gửi mặc định
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')  # Hoặc bạn có thể dùng trực tiếp 'nhaxe9442@gmail.com'
