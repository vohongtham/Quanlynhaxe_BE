# class Config:
#     SECRET_KEY = 'app_aip'
#     SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost:3306/qlnhaxe'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

    #  Add other configurations as needed

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('KEY')  # Load SECRET_KEY from .env file
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # Load database URL from .env file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# class Config:
#     # Load SECRET_KEY from .env file, or set a default value
#     SECRET_KEY = os.getenv('KEY', 'default_secret_key')

#     # Load database URL from .env file
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

#     # Disable SQLALCHEMY_TRACK_MODIFICATIONS to avoid overhead
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

#     # Load JWT_SECRET_KEY from .env file, or use a default value
#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret')
