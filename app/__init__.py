from flask import Flask
from config import Config
from flask_cors import CORS
import mysql.connector
from mysql.connector import errorcode
from .database import db, ma, bcrypt, jwt
from .routes.sinhvien_routes import sv_routes # Ensure this import matches the actual file structure
from .routes.user_routes import user_routes
from .routes.chitietravao_routes import chitiet_ravao_routes
from .routes.xe_routes import xe_routes
from .routes.baixe_routes import baixe_routes
from .routes.donvi_routes import donvi_routes
from .routes.nganh_routes import nganh_routes
from .routes.lop_routes import lop_routes
from .routes.loggin_routes import loggin_routes
from .routes.phanquyen_routes import phanquyen_routes


# Function to create the database if it doesn't exist
def create_db_if_not_exists():
    try:
        connection = mysql.connector.connect(
            user='root',
            # password='your_password_here',  # Add your MySQL password here
            host='localhost'
        )
        cursor = connection.cursor()

        # Create the database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS qlnhaxe;")
        print("Database 'qlnhaxe' created or already exists.")

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

# Function to create tables
def create_db(app):
    with app.app_context():
        db.create_all()
        print("Created tables!")

# Main function to create the Flask application
def create_app(config_class=Config):
    # Initialize the Flask application
    app = Flask(__name__)
    
    # Load configuration from Config class
    # app.config.from_object(config_class)
    app.config.from_object(Config)
    
    # Print SECRET_KEY to verify it's loaded
    print("SECRET_KEY:", app.config["SECRET_KEY"])
    print("JWT_SECRET_KEY:", app.config["JWT_SECRET_KEY"])

    # Create the database if it doesn't exist
    create_db_if_not_exists()

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    create_db(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register the routes Blueprint
    app.register_blueprint(sv_routes)  # Ensure this matches your Blueprint import

    app.register_blueprint(user_routes)

    app.register_blueprint(xe_routes)

    app.register_blueprint(baixe_routes)

    app.register_blueprint(donvi_routes)

    app.register_blueprint(nganh_routes)

    app.register_blueprint(lop_routes)

    app.register_blueprint(chitiet_ravao_routes)

    app.register_blueprint(loggin_routes)

    app.register_blueprint(phanquyen_routes)

    # app.register_blueprint(loggin_routes, name='loggin_routes')


    # Enable CORS
    CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for demonstration
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Check database connection on startup
    with app.app_context():
        try:
            # Test the database connection
            db.engine.connect()
            print("Database connection successful.")
        except Exception as e:
            print(f"Database connection failed: {e}")

        
        #  # Thực hiện các truy vấn hoặc hành động khác
        # result, error = authenticate_user('admin@gmail.com', 'password')
        # if error:
        #     print(f"Error: {error}")
        # else:
        #     print(f"Result: {result}")
    
    return app



# from flask import Flask
# from config import Config
# from flask_cors import CORS
# import mysql.connector
# from mysql.connector import errorcode
# from .database import db, ma, bcrypt, jwt
# from .routes.sinhvien_routes import sv_routes
# from .routes.user_routes import user_routes
# from .routes.chitietravao_routes import chitiet_ravao_routes
# from .routes.xe_routes import xe_routes
# from .routes.baixe_routes import baixe_routes
# from .routes.donvi_routes import donvi_routes
# from .routes.nganh_routes import nganh_routes
# from .routes.lop_routes import lop_routes
# from .routes.loggin_routes import loggin_routes
# from .routes.phanquyen_routes import phanquyen_routes

# # Function to create the database if it doesn't exist
# def create_db_if_not_exists():
#     try:
#         connection = mysql.connector.connect(
#             user='root',
#             password='your_password_here',  # Add your MySQL password here
#             host='localhost'
#         )
#         cursor = connection.cursor()
#         cursor.execute("CREATE DATABASE IF NOT EXISTS qlnhaxe;")
#         print("Database 'qlnhaxe' created or already exists.")
#         cursor.close()
#         connection.close()
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Error with your username or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)

# # Function to create tables
# def create_db(app):
#     with app.app_context():
#         db.create_all()
#         print("Created tables!")

# # Main function to create the Flask application
# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     # Print SECRET_KEY and JWT_SECRET_KEY for debugging (remove in production)
#     print("SECRET_KEY:", app.config.get("SECRET_KEY"))
#     print("JWT_SECRET_KEY:", app.config.get("JWT_SECRET_KEY"))

#     create_db_if_not_exists()

#     # Initialize extensions
#     db.init_app(app)
#     ma.init_app(app)
#     bcrypt.init_app(app)
#     jwt.init_app(app)

#     # Create tables
#     create_db(app)

#     # Register blueprints
#     app.register_blueprint(sv_routes)
#     app.register_blueprint(user_routes)
#     app.register_blueprint(xe_routes)
#     app.register_blueprint(baixe_routes)
#     app.register_blueprint(donvi_routes)
#     app.register_blueprint(nganh_routes)
#     app.register_blueprint(lop_routes)
#     app.register_blueprint(chitiet_ravao_routes)
#     app.register_blueprint(loggin_routes)
#     app.register_blueprint(phanquyen_routes)

#     # Enable CORS
#     CORS(app, resources={r"/*": {"origins": "*"}})
#     app.config['CORS_HEADERS'] = 'Content-Type'

#     # Check database connection on startup
#     with app.app_context():
#         try:
#             db.engine.connect()
#             print("Database connection successful.")
#         except Exception as e:
#             print(f"Database connection failed: {e}")

#     return app


