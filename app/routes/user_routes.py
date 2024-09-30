from flask import Blueprint, jsonify, request
from app.services.user_services import (
    add_user_service,
    get_all_users_service,
    get_user_by_criteria_service,
    update_user_service,
    delete_user_service, 
    delete_all_users_service
)

# Initialize the Blueprint for user routes
user_routes = Blueprint("user_routes", __name__)

# Add user
@user_routes.route("/user/add", methods=['POST'])
def add_user():
    """
    Route to add a new user.
    Expects JSON data in the request body.
    Returns a success message or an error.
    """
    try:
        response_message, status_code = add_user_service(request)  # Pass the request to the service function
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all users
@user_routes.route("/user/all", methods=['GET'])
def get_all_users():
    """
    Route to get all users.
    Returns a list of users or an error message.
    """
    try:
        response_message, status_code = get_all_users_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get user by criteria (e.g., Ten_user, Email, VaiTro)
@user_routes.route("/user/search", methods=['GET'])
def search_user():
    """
    Route to search for a user by name, email, or role.
    Returns the user's details or an error message.
    """
    try:
        # Retrieve query parameters from the request
        Ten_user = request.args.get('Ten_user')
        Email = request.args.get('Email')
        Ma_Quyen = request.args.get('Ma_Quyen')

        # Call the service function to search for the user
        response_message, status_code = get_user_by_criteria_service(
            Ten_user=Ten_user, Email=Email, Ma_Quyen=Ma_Quyen
        )
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400

# Update user
@user_routes.route("/user/update/<Ma_user>", methods=['PUT'])
def update_user(Ma_user):
    """
    Route to update an existing user's details.
    Expects JSON data in the request body.
    Returns a success message or an error message if the user is not found.
    """
    try:
        # Call the service function to update the user
        response_message, status_code = update_user_service(Ma_user, request)
        return jsonify(response_message), status_code
    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({"error": str(e)}), 400

# Delete user
@user_routes.route("/user/delete/<Ma_user>", methods=['DELETE'])
def delete_user(Ma_user):
    """
    Route to delete an existing user by Ma_user.
    Returns a success message or an error message if the user is not found.
    """
    try:
        # Call the service function to delete the user
        response_message, status_code = delete_user_service(Ma_user)
        return jsonify(response_message), status_code
    except Exception as e:
        # Return error message if an exception occurs
        return jsonify({"error": str(e)}), 400

# Delete all users
@user_routes.route("/user/delete_all", methods=['DELETE'])
def delete_all_users():
    """
    Route to delete all users from the database.
    Returns a success message or an error message if something goes wrong.
    """
    try:
        response_message, status_code = delete_all_users_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400



# app/routes/user_routes.py

from flask import Blueprint, jsonify
from app.auth_decorator import token_required

# user_bp = Blueprint('user', __name__)

@user_routes.route('/protected-route', methods=['GET'])
@token_required
def protected_route():
    return jsonify({"message": "This is a protected route."}), 200
