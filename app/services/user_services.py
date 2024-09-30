from app.database import db
from app.utils.utils import generate
from app.app_ma import UsersSchema
from app.model import Users
from flask import request
# import bcrypt
import logging
from flask_bcrypt import Bcrypt

# Initialize bcrypt
bcrypt = Bcrypt()

# Define the schema
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

# Configure logging
logging.basicConfig(level=logging.INFO)

# def add_user_service(request):
#     try:
#         data = request.get_json()
#         Ten_user = data.get('Ten_user')
#         Email = data.get('Email')
#         Password = data.get('Password')
#         GioiTinh = data.get('GioiTinh')
#         NgaySinh = data.get('NgaySinh')
#         Ma_BaiXe = data.get('Ma_BaiXe')
#         Ma_Quyen = data.get('Ma_Quyen')

#         # Validate input fields
#         if not all([Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_BaiXe, Ma_Quyen]):
#             return {"error": "Missing required fields."}, 400

#         # Check if the user already exists
#         if Users.query.filter_by(Email=Email).first():
#             return {"error": "Email already exists."}, 400

#         # Generate a unique Ma_user
#         Ma_user = generate()
#         while Users.query.filter_by(Ma_user=Ma_user).first():
#             Ma_user = generate()  # Regenerate if collision occurs

#         # Hash the password using bcrypt
#         hashed_password = bcrypt.hashpw(Password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#         # Create the new user with the hashed password and generated Ma_user
#         new_user = Users(
#             Ma_user=Ma_user,
#             Ten_user=Ten_user,
#             Email=Email,
#             Password=hashed_password,
#             GioiTinh=GioiTinh,
#             NgaySinh=NgaySinh,
#             Ma_BaiXe=Ma_BaiXe,
#             Ma_Quyen=Ma_Quyen
#         )

#         db.session.add(new_user)
#         db.session.commit()
#         return {"message": "User added successfully!"}, 201

#     except Exception as e:
#         db.session.rollback()
#         logging.error(f"Error adding user: {e}")
#         return {"error": str(e)}, 400

# add_user_service
def add_user_service(request):
    try:
        data = request.get_json()
        Ten_user = data.get('Ten_user')
        Email = data.get('Email')
        Password = data.get('Password')
        GioiTinh = data.get('GioiTinh')
        NgaySinh = data.get('NgaySinh')
        Ma_BaiXe = data.get('Ma_BaiXe')
        Ma_Quyen = data.get('Ma_Quyen')

        if not all([Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_BaiXe, Ma_Quyen]):
            return {"error": "Missing required fields."}, 400

        if Users.query.filter_by(Email=Email).first():
            return {"error": "Email đã sử dụng."}, 400

        Ma_user = generate()
        while Users.query.filter_by(Ma_user=Ma_user).first():
            Ma_user = generate()

        # Use bcrypt to hash the password
        hashed_password = bcrypt.generate_password_hash(Password).decode('utf-8')

        new_user = Users(
            Ma_user=Ma_user,
            Ten_user=Ten_user,
            Email=Email,
            Password=hashed_password,
            GioiTinh=GioiTinh,
            NgaySinh=NgaySinh,
            Ma_BaiXe=Ma_BaiXe,
            Ma_Quyen=Ma_Quyen
        )

        db.session.add(new_user)
        db.session.commit()
        return {"message": "User added successfully!"}, 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400


# update_user_service
def update_user_service(Ma_user, request):
    try:
        user = Users.query.filter_by(Ma_user=Ma_user).first()
        if not user:
            return {"error": "User not found"}, 404

        data = request.get_json()
        user.Ten_user = data.get('Ten_user', user.Ten_user)
        user.Email = data.get('Email', user.Email)
        if 'Password' in data:
            user.Password = bcrypt.generate_password_hash(data['Password']).decode('utf-8')
        user.GioiTinh = data.get('GioiTinh', user.GioiTinh)
        user.NgaySinh = data.get('NgaySinh', user.NgaySinh)
        user.Ma_BaiXe = data.get('Ma_BaiXe', user.Ma_BaiXe)
        user.Ma_Quyen = data.get('Ma_Quyen', user.Ma_Quyen)

        db.session.commit()
        return {"message": "Update success!"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

def get_user_by_criteria_service(Ma_user= None, Ten_user=None, Email=None, NgaySinh= None, Ma_BaiXe=None, Ma_Quyen=None):
    """
    Retrieve users by name, email, or role with partial matches.
    """
    try:
        query = Users.query

        if Ma_user:
            query = query.filter(Users.Ma_user.ilike(f"%{Ma_user}%"))
        if Ten_user:
            query = query.filter(Users.Ten_user.ilike(f"%{Ten_user}%"))
        if Email:
            query = query.filter(Users.Email.ilike(f"%{Email}%"))
        if NgaySinh:
            query = query.filter(Users.NgaySinh.ilike(f"%{NgaySinh}%"))
        if Ma_BaiXe:
            query = query.filter(Users.Ma_BaiXe.ilike(f"%{Ma_BaiXe}%"))
        if Ma_Quyen:
            query = query.filter(Users.Ma_Quyen.ilike(f"%{Ma_Quyen}%"))

        users = query.all()

        if not users:
            return {"message": "No users found matching the criteria"}, 404

        result = users_schema.dump(users)
        return result, 200

    except Exception as e:
        logging.error(f"Error retrieving users: {e}")
        return {"error": str(e)}, 400

def get_all_users_service():
    """
    Retrieve all users from the database.
    """
    try:
        users = Users.query.all()
        result = users_schema.dump(users)
        return result, 200

    except Exception as e:
        logging.error(f"Error retrieving all users: {e}")
        return {"error": str(e)}, 400

def delete_user_service(Ma_user):
    """
    Delete a user by Ma_user.
    """
    try:
        user = Users.query.filter_by(Ma_user=Ma_user).first()
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": f"User with Ma_user {Ma_user} deleted successfully"}, 200

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error deleting user: {e}")
        return {"error": str(e)}, 400

def delete_all_users_service():
    """
    Delete all users from the database.
    """
    try:
        count = db.session.query(Users).delete()
        db.session.commit()
        return {"message": f"{count} users deleted successfully!"}, 200

    except Exception as e:
        db.session.rollback()
        logging.error(f"Error deleting all users: {e}")
        return {"error": str(e)}, 400

# def update_user_service(Ma_user, request):
#     """
#     Update an existing user's details.
#     """
#     try:
#         user = Users.query.filter_by(Ma_user=Ma_user).first()
#         if not user:
#             return {"error": "User not found"}, 404

#         data = request.get_json()
#         user.Ten_user = data.get('Ten_user', user.Ten_user)
#         user.Email = data.get('Email', user.Email)
#         if 'Password' in data:
#             user.Password = bcrypt.hashpw(data['Password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#         user.GioiTinh = data.get('GioiTinh', user.GioiTinh)
#         user.NgaySinh = data.get('NgaySinh', user.NgaySinh)
#         user.Ma_BaiXe = data.get('Ma_BaiXe', user.Ma_BaiXe)
#         user.Ma_Quyen = data.get('Ma_Quyen', user.Ma_Quyen)

#         db.session.commit()
#         return {"message": "Update success!"}, 200

#     except Exception as e:
#         db.session.rollback()
#         logging.error(f"Error updating user: {e}")
#         return {"error": str(e)}, 400
