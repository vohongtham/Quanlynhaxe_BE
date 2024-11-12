from flask import Blueprint, jsonify, request
from app.services.sinhvien_services import add_sv_service   # Ensure the services folder is at the correct level
from app.services.sinhvien_services import get_all_svs_service
from app.services.sinhvien_services import get_sv_by_criteria_service
from app.services.sinhvien_services import update_sv_service
from app.services.sinhvien_services import delete_sv_service
from app.services.sinhvien_services import delete_all_svs_service

# Initialize the Blueprint for sinhvien routes
sv_routes = Blueprint("routes", __name__)

# Add sinh vien
@sv_routes.route("/sv/add", methods=['POST'])
def add_sinhvien():
    """
    Route to add a new student.
    Expects JSON data in the request body.
    Returns a success message or an error.
    """
    try:
        response_message, status_code = add_sv_service(request)  # Pass the request to the service function
        print("Response Message:", response_message)  # Debugging line
        print("Status Code:", status_code)  # Debugging line
        return jsonify(response_message), status_code
    except Exception as e:
        print("Route-level Exception:", str(e))  # Debugging line
        return jsonify({"error": str(e)}), 400
    
# def add_sinhvien():
#     """
#     Route to add a new student.
#     Expects JSON data in the request body.
#     Returns a success message or an error.
#     """
#     try:
#         response_message, status_code = add_sv_service(request)  # Pass the request to the service function
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

    
# Route search sinh vien
@sv_routes.route("/sv/search", methods=['GET'])
def search_sinhvien():
    """
    Route to search for a student by Mssv, name, email, or phone number.
    Returns the student's details or an error message.
    """
    try:
        # Retrieve query parameters from the request
        Mssv = request.args.get('Mssv')
        Ten_SV = request.args.get('Ten_SV')
        Email = request.args.get('Email')
        NgaySinh = request.args.get('NgaySinh')
        GioiTinh = request.args.get('GioiTinh')
        SDT = request.args.get('SDT')

        # Call the service function to search for the student
        response_message, status_code = get_sv_by_criteria_service(Mssv=Mssv, Ten_SV=Ten_SV, Email=Email, NgaySinh=NgaySinh, GioiTinh = GioiTinh, SDT=SDT)
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400

# Route goi tat ca sinh vien
@sv_routes.route("/sv/all", methods=['GET']) 
def get_all_sinhviens():                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    """
    Route to retrieve all students.
    Returns a list of all students' details in JSON format or an error message if something goes wrong.
    """
    try:
        # Call the service function to get all students
        response_message, status_code = get_all_svs_service()
        
        # Return the list of students or an error message with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400

#Route update thong tin sinh vien
@sv_routes.route("/sv/update/<Mssv>", methods=['PUT'])
def update_sinhvien(Mssv):
    """
    Route to update a student's details.
    Expects JSON data in the request body.
    Returns a success message or an error.
    """
    try:
        # Call the update service function, passing the Mssv and request object
        response_message, status_code = update_sv_service(Mssv, request)
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400

# Detele sinh vien 
@sv_routes.route("/sv/delete/<Mssv>", methods=['DELETE'])
def delete_sinhvien(Mssv):
    """
    Route to delete a student.
    Returns a success message or an error.
    """
    try:
        # Call the delete service function, passing the Mssv
        response_message, status_code = delete_sv_service(Mssv)
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400

# Import the service function to delete all students


# Route to delete all students
@sv_routes.route("/sv/delete_all", methods=['DELETE'])
def delete_all_sinhviens():
    """
    Route to delete all students.
    Returns a success message or an error.
    """
    try:
        # Call the delete all service function
        response_message, status_code = delete_all_svs_service()
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400
