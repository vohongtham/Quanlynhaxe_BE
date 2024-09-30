# from flask import Blueprint, request, jsonify
# from app.services.loggin_services import register_student, logout_service, login_service
# from app.app_ma import SinhvienSchema
# from flask import Blueprint, jsonify
# from app.auth_decorator import token_required, add_to_blacklist, remove_from_blacklist

# loggin_routes = Blueprint('auth', __name__)

# @loggin_routes.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
    
#     result, error = register_student(
#         Mssv=data.get('Mssv'),
#         Ten_SV=data.get('Ten_SV'),
#         Ma_Lop=data.get('Ma_Lop'),
#         Email=data.get('Email'),
#         Password=data.get('Password'),
#         NgaySinh=data.get('NgaySinh'),
#         GioiTinh=data.get('GioiTinh'),
#         SDT=data.get('SDT')
#     )
    
#     if error:
#         return jsonify({"error": error}), 400
    
#     return jsonify(result), 201

# # @loggin_routes.route('/logout', methods=['POST'])
# # def logout():
# #     return logout_service()


# # Route for login (for both Sinhvien and Users)
# @loggin_routes.route('/login', methods=['POST'])
# def login():
#     """
#     Handles login for both Sinhvien and Users. 
#     Returns a JWT token upon successful login.
#     """
#     return login_service()




# # loggin_routes = Blueprint('auth', __name__)

# @loggin_routes.route('/logout', methods=['POST'])
# @token_required
# def logout():
#     token = request.headers.get('Authorization').split(" ")[1]
#     add_to_blacklist(token)
#     return jsonify({"message": "Logged out successfully."}), 200







# from flask import Blueprint, request, jsonify
# from app.services.loggin_services import register_student, login_service
# from app.auth_decorator import token_required, add_to_blacklist

# loggin_routes = Blueprint('auth', __name__)

# @loggin_routes.route('/register', methods=['POST'])
# def register():
#     """
#     Route for student registration.
#     """
#     data = request.get_json()

#     result, error = register_student(
#         Mssv=data.get('Mssv'),
#         Ten_SV=data.get('Ten_SV'),
#         Ma_Lop=data.get('Ma_Lop'),
#         Email=data.get('Email'),
#         Password=data.get('Password'),
#         NgaySinh=data.get('NgaySinh'),
#         GioiTinh=data.get('GioiTinh'),
#         SDT=data.get('SDT')
#     )
    
#     if error:
#         return jsonify({"error": error}), 400

#     return jsonify(result), 201

# @loggin_routes.route('/login', methods=['POST'])
# def login():
#     """
#     Route for login (for both Sinhvien and Users).
#     Returns a JWT token upon successful login.
#     """
#     return login_service()

# @loggin_routes.route('/logout', methods=['POST'])
# @token_required
# def logout():
#     """
#     Route for logging out the user and adding token to the blacklist.
#     """
#     auth_header = request.headers.get('Authorization')
#     if auth_header and auth_header.startswith("Bearer "):
#         token = auth_header.split(" ")[1]
#         add_to_blacklist(token)
#         return jsonify({"message": "Logged out successfully."}), 200
#     else:
#         return jsonify({"error": "Invalid token."}), 401










from flask import Blueprint, request, jsonify
from app.services.loggin_services import register_student, login_service
from app.auth_decorator import token_required, add_to_blacklist

loggin_routes = Blueprint('auth', __name__)

@loggin_routes.route('/register', methods=['POST'])
def register():
    """
    Route for student registration.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ['Mssv', 'Ten_SV', 'Ma_Lop', 'Email', 'Password', 'NgaySinh', 'GioiTinh']
    
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    result, error = register_student(
        Mssv=data.get('Mssv'),
        Ten_SV=data.get('Ten_SV'),
        Ma_Lop=data.get('Ma_Lop'),
        Email=data.get('Email'),
        Password=data.get('Password'),
        NgaySinh=data.get('NgaySinh'),
        GioiTinh=data.get('GioiTinh'),
        SDT=data.get('SDT')  # Optional field
    )
    
    if error:
        return jsonify({"error": error}), 400

    return jsonify(result), 201


@loggin_routes.route('/login', methods=['POST'])
def login():
    """
    Route for login (for both Sinhvien and Users).
    Returns a JWT token upon successful login.
    """
    data = request.get_json()

    if not data or 'Email' not in data or 'Password' not in data:
        return jsonify({"error": "Email and Password are required"}), 400

    return login_service()


@loggin_routes.route('/logout', methods=['POST'])
@token_required
def logout():
    """
    Route for logging out the user and adding the JWT token to the blacklist.
    """
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith("Bearer"):
        token = auth_header.split(" ")[1]
        add_to_blacklist(token)
        return jsonify({"message": "Logged out successfully."}), 200
    else:
        return jsonify({"error": "Invalid token format."}), 401


