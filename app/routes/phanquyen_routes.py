from flask import Blueprint, jsonify, request
from app.services.phanquyen_services import (
    add_phanquyen_service,
    get_all_phanquyens_service,
    get_phanquyen_by_criteria_service,
    update_phanquyen_service,
    delete_phanquyen_service,
    delete_all_phanquyens_service
)

# Initialize the Blueprint for phanquyen routes
phanquyen_routes = Blueprint("phanquyen_routes", __name__)

# Add Phanquyen
@phanquyen_routes.route("/phanquyen/add", methods=['POST'])
def add_phanquyen():
    try:
        response_message, status_code = add_phanquyen_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route search Phanquyen
@phanquyen_routes.route("/phanquyen/search", methods=['GET'])
def search_phanquyen():
    try:
        Ma_Quyen = request.args.get('Ma_Quyen')
        TenQuyen = request.args.get('TenQuyen')

        response_message, status_code = get_phanquyen_by_criteria_service(Ma_Quyen=Ma_Quyen, TenQuyen=TenQuyen)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route get all Phanquyens
@phanquyen_routes.route("/phanquyen/all", methods=['GET'])
def get_all_phanquyens():
    try:
        response_message, status_code = get_all_phanquyens_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route update Phanquyen
@phanquyen_routes.route("/phanquyen/update/<Ma_Quyen>", methods=['PUT'])
def update_phanquyen(Ma_Quyen):
    try:
        response_message, status_code = update_phanquyen_service(Ma_Quyen, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete Phanquyen
@phanquyen_routes.route("/phanquyen/delete/<Ma_Quyen>", methods=['DELETE'])
def delete_phanquyen(Ma_Quyen):
    try:
        response_message, status_code = delete_phanquyen_service(Ma_Quyen)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete all Phanquyens
@phanquyen_routes.route("/phanquyen/delete_all", methods=['DELETE'])
def delete_all_phanquyens():
    try:
        response_message, status_code = delete_all_phanquyens_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
