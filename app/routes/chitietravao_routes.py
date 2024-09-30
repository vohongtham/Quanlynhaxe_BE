from flask import Blueprint, jsonify, request
from app.services.chitietravao_services import (
    add_chitiet_ravao_service,
    get_all_chitiet_ravao_service,
    get_chitiet_ravao_by_criteria_service,
    update_chitiet_ravao_service,
    delete_chitiet_ravao_service,
    delete_all_chitiet_ravao_service
)

# Initialize the Blueprint for ChiTietRaVao routes
chitiet_ravao_routes = Blueprint("chitiet_ravao_routes", __name__)

# Route: Add ChiTietRaVao
@chitiet_ravao_routes.route("/chitietravao/add", methods=['POST'])
def add_chitiet_ravao():
    try:
        response_message, status_code = add_chitiet_ravao_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Get all ChiTietRaVao
@chitiet_ravao_routes.route("/chitietravao/all", methods=['GET'])
def get_all_chitiet_ravao():
    try:
        response_message, status_code = get_all_chitiet_ravao_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Get ChiTietRaVao by Ma_CT
# @chitiet_ravao_routes.route("/chitietravao/<Ma_CT>", methods=['GET'])
# def get_chitiet_ravao_by_id(Ma_CT):
#     try:
#         response_message, status_code = get_chitiet_ravao_by_id_service(Ma_CT)
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# Route: Search ChiTietRaVao
@chitiet_ravao_routes.route("/chitietravao/search", methods=['GET'])
def search_chitiet_ravao():
    """
    Route to search for ChiTietRaVao records by various criteria.
    Returns the details or an error message.
    """
    try:
        # Retrieve query parameters from the request
        Ma_CT = request.args.get('Ma_CT')
        Mssv = request.args.get('Mssv')
        BienSoXe = request.args.get('BiensoXe')
        Ma_BaiXe = request.args.get('Ma_BaiXe')
        TG_Vao = request.args.get('TG_Vao')
        TG_Ra = request.args.get('TG_Ra')

        # Add any other parameters that are relevant for searching

        # Call the service function to search for ChiTietRaVao records
        response_message, status_code = get_chitiet_ravao_by_criteria_service(
            Ma_CT=Ma_CT,
            Mssv=Mssv,
            BienSoXe=BienSoXe,
            Ma_BaiXe=Ma_BaiXe,
            TG_Vao=TG_Vao,
            TG_Ra=TG_Ra
            # Add any other parameters as needed
        )
        
        # Return the response as JSON with the appropriate status code
        return jsonify(response_message), status_code
    except Exception as e:
        # If an unexpected error occurs, return an error message and a 400 status code
        return jsonify({"error": str(e)}), 400


# Route: Update ChiTietRaVao by Ma_CT
@chitiet_ravao_routes.route("/chitietravao/update/<Ma_CT>", methods=['PUT'])
def update_chitiet_ravao(Ma_CT):
    try:
        response_message, status_code = update_chitiet_ravao_service(Ma_CT, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Delete ChiTietRaVao by Ma_CT
@chitiet_ravao_routes.route("/chitietravao/delete/<Ma_CT>", methods=['DELETE'])
def delete_chitiet_ravao(Ma_CT):
    try:
        response_message, status_code = delete_chitiet_ravao_service(Ma_CT)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route: Delete all ChiTietRaVao
@chitiet_ravao_routes.route("/chitietravao/delete_all", methods=['DELETE'])
def delete_all_chitiet_ravao():
    try:
        response_message, status_code = delete_all_chitiet_ravao_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
