from flask import Blueprint, jsonify, request
from app.services.nganh_services import add_nganh_service, get_all_nganhs_service, get_nganh_by_criteria_service, update_nganh_service, delete_nganh_service, delete_all_nganhs_service

# Initialize the Blueprint for nganh routes
nganh_routes = Blueprint("nganh_routes", __name__)

# Add nganh
@nganh_routes.route("/nganh/add", methods=['POST'])
def add_nganh():
    try:
        response_message, status_code = add_nganh_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route search nganh
@nganh_routes.route("/nganh/search", methods=['GET'])
def search_nganh():
    try:
        Ma_Nganh = request.args.get('Ma_Nganh')
        TenNganh = request.args.get('TenNganh')

        response_message, status_code = get_nganh_by_criteria_service(Ma_Nganh=Ma_Nganh, TenNganh=TenNganh)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route get all nganhs
@nganh_routes.route("/nganh/all", methods=['GET'])
def get_all_nganhs():
    try:
        response_message, status_code = get_all_nganhs_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route update nganh
@nganh_routes.route("/nganh/update/<Ma_Nganh>", methods=['PUT'])
def update_nganh(Ma_Nganh):
    try:
        response_message, status_code = update_nganh_service(Ma_Nganh, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete nganh
@nganh_routes.route("/nganh/delete/<Ma_Nganh>", methods=['DELETE'])
def delete_nganh(Ma_Nganh):
    try:
        response_message, status_code = delete_nganh_service(Ma_Nganh)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete all nganhs
@nganh_routes.route("/nganh/delete_all", methods=['DELETE'])
def delete_all_nganhs():
    try:
        response_message, status_code = delete_all_nganhs_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
