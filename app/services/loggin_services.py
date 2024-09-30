# from app.model import Users, Sinhvien
# from app.database import db, jwt, bcrypt
# from flask import request, jsonify
# from config import Config
# import datetime
# from flask_jwt_extended import create_access_token



# def register_student(Mssv, Ten_SV, Ma_Lop, Email, Password, NgaySinh, GioiTinh, SDT=None):
#     Email = Email.strip()
#     Password = Password.strip()

#     existing_student = Sinhvien.query.filter_by(Email=Email).first()
#     if existing_student:
#         return None, 'Email đã được sử dụng'

#     # Hash the password
#     hashed_password = bcrypt.generate_password_hash(Password)
#     print(f"Hashed Password (register): {hashed_password}")

#     new_student = Sinhvien(
#         Mssv=Mssv,
#         Ten_SV=Ten_SV,
#         Ma_Lop=Ma_Lop,
#         Email=Email,
#         Password=hashed_password,  # Store hashed password
#         NgaySinh=NgaySinh,
#         GioiTinh=GioiTinh,
#         Ma_Quyen='MQSV',
#         SDT=SDT
#     )

#     try:
#         db.session.add(new_student)
#         db.session.commit()
        
#     except Exception as e:
#         db.session.rollback()
#         return None, f"Đã xảy ra lỗi khi lưu thông tin sinh viên: {str(e)}"

#     return {
#         'message': 'Đăng ký thành công', 
#         'student': {
#             'Mssv': new_student.Mssv, 
#             'Ten_SV': new_student.Ten_SV, 
#             'Email': new_student.Email, 
#             'Ma_Quyen': new_student.Ma_Quyen
#         }
#     }, None


# def login_service():
#     """
#     Handles login for both students and users. Authorization based on Ma_Quyen.
#     """
#     data = request.get_json()
    
#     email = data.get('Email').strip()
#     password = data.get('Password').strip()

#     if not email or not password:
#         return jsonify({"error": "Vui lòng nhập email và mật khẩu"}), 400
    
#     student = Sinhvien.query.filter_by(Email=email).first()
#     user = Users.query.filter_by(Email=email).first()

#     if student:
#         stored_password = student.Password
#         print(f"Stored Hashed Password: {stored_password}")
#         print(f"Entered Password: {password}")

#         is_correct = bcrypt.check_password_hash(stored_password, password)
#         print(f"Password Check (Correct): {is_correct}")

#         if is_correct:
#             return generate_token(student.Mssv, student.Email, student.Ma_Quyen)
#         else:
#             return jsonify({"error": "Sai mật khẩu"}), 401

#     elif user:
#         stored_password = user.Password
#         print(f"Stored Hashed Password: {stored_password}")
#         print(f"Entered Password: {password}")

#         if bcrypt.check_password_hash(stored_password, password):
#             return generate_token(user.Ma_user, user.Email, user.Ma_Quyen)
#         else:
#             return jsonify({"error": "Sai mật khẩu"}), 401
#     else:
#         return jsonify({"error": "Không tìm thấy tài khoản"}), 404

# def generate_token(user_id, email, ma_quyen):
#     """
#     Generate JWT token after successful authentication.
#     """
#     try:
#         payload = {
#             'user_id': user_id,
#             'email': email,
#             'ma_quyen': ma_quyen,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
#         }
#         token = create_access_token(identity=payload)  

#         return jsonify({
#             "message": "Đăng nhập thành công",
#             "token": token,
#             "ma_quyen": ma_quyen
#         }), 200
    
#     except Exception as e:
#         return jsonify({"error": f"Đã xảy ra lỗi khi tạo token: {str(e)}"}), 500


# # # Logout
# # # Assuming you have a blacklist set for tokens
# # blacklisted_tokens = set()  # In a real application, this should be a persistent store

# # def logout_service():
# #     """
# #     Handles the logout request by blacklisting the provided JWT token.
# #     """
# #     try:
# #         # Retrieve the token from the request headers
# #         auth_header = request.headers.get('Authorization')
# #         if not auth_header:
# #             return jsonify({"error": "Authorization header missing"}), 401
        
# #         token = auth_header.split(" ")[1]  # Extract token from Bearer <token>
        
# #         # Add token to the blacklist
# #         blacklisted_tokens.add(token)
        
# #         return jsonify({"message": "Logged out successfully!"}), 200

# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 400


# from flask_jwt_extended import get_jwt, jwt_required

# # Assuming you have a persistent blacklist set for tokens (in-memory for now)
# blacklisted_tokens = set()  # In production, store this in a database or redis

# def is_token_blacklisted(jti):
#     """
#     Check if the token's jti (JWT ID) is blacklisted.
#     """
#     return jti in blacklisted_tokens

# def logout_service():
#     """
#     Handles the logout request by blacklisting the JWT token provided in the request.
#     """
#     try:
#         # Ensure the user is logged in and token is provided
#         jwt_data = get_jwt()
#         jti = jwt_data['jti']  # JWT ID, unique identifier for the token

#         # Add the token's jti to the blacklist
#         blacklisted_tokens.add(jti)
        
#         return jsonify({"message": "Logged out successfully!"}), 200
    
#     except Exception as e:
#         return jsonify({"error": f"An error occurred during logout: {str(e)}"}), 400


from app.model import Users, Sinhvien
from app.database import db, jwt, bcrypt
from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt
import datetime

def register_student(Mssv, Ten_SV, Ma_Lop, Email, Password, NgaySinh, GioiTinh, SDT=None):
    """
    Registers a new student with the given details.
    """
    Email = Email.strip()
    Password = Password.strip()

    existing_student = Sinhvien.query.filter_by(Email=Email).first()
    if existing_student:
        return None, 'Email đã được sử dụng'

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(Password)
    print(f"Hashed Password (register): {hashed_password}")

    new_student = Sinhvien(
        Mssv=Mssv,
        Ten_SV=Ten_SV,
        Ma_Lop=Ma_Lop,
        Email=Email,
        Password=hashed_password,  # Store hashed password
        NgaySinh=NgaySinh,
        GioiTinh=GioiTinh,
        Ma_Quyen='MQSV',
        SDT=SDT
    )

    try:
        db.session.add(new_student)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return None, f"Đã xảy ra lỗi khi lưu thông tin sinh viên: {str(e)}"

    return {
        'message': 'Đăng ký thành công', 
        'student': {
            'Mssv': new_student.Mssv, 
            'Ten_SV': new_student.Ten_SV, 
            'Email': new_student.Email, 
            'Ma_Quyen': new_student.Ma_Quyen
        }
    }, None

def login_service():
    """
    Handles login for both students and users. Authorization based on Ma_Quyen.
    """
    data = request.get_json()
    email = data.get('Email').strip()
    password = data.get('Password').strip()

    if not email or not password:
        return jsonify({"error": "Vui lòng nhập email và mật khẩu"}), 400

    student = Sinhvien.query.filter_by(Email=email).first()
    user = Users.query.filter_by(Email=email).first()

    if student:
        stored_password = student.Password
        is_correct = bcrypt.check_password_hash(stored_password, password)

        if is_correct:
            return generate_token(student.Mssv, student.Email, student.Ma_Quyen)
        else:
            return jsonify({"error": "Sai mật khẩu"}), 401

    elif user:
        stored_password = user.Password
        if bcrypt.check_password_hash(stored_password, password):
            return generate_token(user.Ma_user, user.Email, user.Ma_Quyen)
        else:
            return jsonify({"error": "Sai mật khẩu"}), 401
    else:
        return jsonify({"error": "Không tìm thấy tài khoản"}), 404

def generate_token(user_id, email, ma_quyen):
    """
    Generate JWT token after successful authentication.
    """
    try:
        payload = {
            'user_id': user_id,
            'email': email,
            'ma_quyen': ma_quyen,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = create_access_token(identity=payload)

        return jsonify({
            "message": "Đăng nhập thành công",
            "token": token,
            "ma_quyen": ma_quyen
        }), 200
    except Exception as e:
        return jsonify({"error": f"Đã xảy ra lỗi khi tạo token: {str(e)}"}), 500




# Persistent blacklist for tokens (e.g., in a database or Redis in production)
blacklisted_tokens = set()

def is_token_blacklisted(jti):
    """
    Check if the token's jti (JWT ID) is blacklisted.
    """
    return jti in blacklisted_tokens

def logout_service():
    """
    Handles the logout request by blacklisting the JWT token provided in the request.
    """
    try:
        # Ensure the user is logged in and token is provided
        jwt_data = get_jwt()
        jti = jwt_data['jti']  # JWT ID, unique identifier for the token

        # Add the token's jti to the blacklist
        blacklisted_tokens.add(jti)

        return jsonify({"message": "Logged out successfully!"}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred during logout: {str(e)}"}), 400



