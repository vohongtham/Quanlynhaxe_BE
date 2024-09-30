from flask import Blueprint, jsonify, request
from app.services.baixe_services import (
    add_baixe_service,
    get_all_baixes_service,
    get_baixe_by_criteria_service,
    update_baixe_service,
    delete_baixe_service,
    delete_all_baixes_service
)

# Initialize the Blueprint for bai_xe routes
baixe_routes = Blueprint("baixe_routes", __name__)

# Add bai_xe record
@baixe_routes.route("/baixe/add", methods=['POST'])
def add_baixe():
    try:
        response_message, status_code = add_baixe_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all bai_xe records
@baixe_routes.route("/baixe/all", methods=['GET'])
def get_all_baixes():
    try:
        response_message, status_code = get_all_baixes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get bai_xe record by criteria (e.g., ID_vitri, Vitri, Trangthai, UserID)
@baixe_routes.route("/baixe/search", methods=['GET'])
def search_baixe():
    try:
        Ma_BaiXe = request.args.get('Ma_BaiXe')
        Ma_DV = request.args.get('Ma_DV')
        Ten_BaiXe = request.args.get('Ten_BaiXe')

        response_message, status_code = get_baixe_by_criteria_service(
            Ma_BaiXe=Ma_BaiXe, Ma_DV=Ma_DV, Ten_BaiXe=Ten_BaiXe
        )
        
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Update bai_xe record
@baixe_routes.route("/baixe/update/<Ma_BaiXe>", methods=['PUT'])
def update_baixe(Ma_BaiXe):
    try:
        response_message, status_code = update_baixe_service(Ma_BaiXe, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete bai_xe record
@baixe_routes.route("/baixe/delete/<Ma_BaiXe>", methods=['DELETE'])
def delete_baixe(Ma_BaiXe):
    try:
        response_message, status_code = delete_baixe_service(Ma_BaiXe)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete all bai_xe records
@baixe_routes.route("/baixe/delete_all", methods=['DELETE'])
def delete_all_baixes():
    try:
        response_message, status_code = delete_all_baixes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
