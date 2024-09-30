from flask import Blueprint, jsonify, request
from app.services.lop_services import add_lop_service, get_all_lops_service, get_lop_by_criteria_service, update_lop_service, delete_lop_service, delete_all_lops_service

# Initialize the Blueprint for lop routes
lop_routes = Blueprint("lop_routes", __name__)

# Add lop
@lop_routes.route("/lop/add", methods=['POST'])
def add_lop():
    try:
        response_message, status_code = add_lop_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route search lop
@lop_routes.route("/lop/search", methods=['GET'])
def search_lop():
    try:
        Ma_Lop = request.args.get('Ma_Lop')
        TenLop = request.args.get('TenLop')
        Ma_Nganh = request.args.get('Ma_Nganh')

        response_message, status_code = get_lop_by_criteria_service(Ma_Lop=Ma_Lop, TenLop=TenLop, Ma_Nganh=Ma_Nganh)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route get all lops
@lop_routes.route("/lop/all", methods=['GET'])
def get_all_lops():
    try:
        response_message, status_code = get_all_lops_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route update lop
@lop_routes.route("/lop/update/<Ma_Lop>", methods=['PUT'])
def update_lop(Ma_Lop):
    try:
        response_message, status_code = update_lop_service(Ma_Lop, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete lop
@lop_routes.route("/lop/delete/<Ma_Lop>", methods=['DELETE'])
def delete_lop(Ma_Lop):
    try:
        response_message, status_code = delete_lop_service(Ma_Lop)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete all lops
@lop_routes.route("/lop/delete_all", methods=['DELETE'])
def delete_all_lops():
    try:
        response_message, status_code = delete_all_lops_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
