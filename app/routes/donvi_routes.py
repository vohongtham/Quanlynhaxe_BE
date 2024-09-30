from flask import Blueprint, jsonify, request
from app.services.donvi_services import add_dv_service, get_all_dvs_service, get_dv_by_criteria_service, update_dv_service, delete_dv_service, delete_all_dvs_service

# Initialize the Blueprint for donvi routes
donvi_routes = Blueprint("donvi_routes", __name__)

# Add don vi
@donvi_routes.route("/donvi/add", methods=['POST'])
def add_donvi():
    try:
        response_message, status_code = add_dv_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route search don vi
@donvi_routes.route("/donvi/search", methods=['GET'])
def search_donvi():
    try:
        Ma_DV = request.args.get('Ma_DV')
        TenDV = request.args.get('TenDV')

        response_message, status_code = get_dv_by_criteria_service(Ma_DV=Ma_DV, TenDV=TenDV)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route get all don vis
@donvi_routes.route("/donvi/all", methods=['GET'])
def get_all_donvis():
    try:
        response_message, status_code = get_all_dvs_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route update don vi
@donvi_routes.route("/donvi/update/<Ma_DV>", methods=['PUT'])
def update_donvi(Ma_DV):
    try:
        response_message, status_code = update_dv_service(Ma_DV, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete don vi
@donvi_routes.route("/donvi/delete/<Ma_DV>", methods=['DELETE'])
def delete_donvi(Ma_DV):
    try:
        response_message, status_code = delete_dv_service(Ma_DV)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete all don vis
@donvi_routes.route("/donvi/delete_all", methods=['DELETE'])
def delete_all_donvis():
    try:
        response_message, status_code = delete_all_dvs_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
