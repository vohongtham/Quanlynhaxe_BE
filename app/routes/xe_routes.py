from flask import Blueprint, jsonify, request
from app.services.xe_services import (
    add_xe_service,
    get_all_xes_service,
    get_xe_by_criteria_service,
    update_xe_service,
    delete_xe_service,
    delete_all_xes_service
)

# Initialize the Blueprint for xe routes
xe_routes = Blueprint("xe_routes", __name__)

# Add xe record
@xe_routes.route("/xe/add", methods=['POST'])
def add_xe():
    try:
        response_message, status_code = add_xe_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get all xe records
@xe_routes.route("/xe/all", methods=['GET'])
def get_all_xes():
    try:
        response_message, status_code = get_all_xes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get xe record by criteria (e.g., BienSoXe, Mssv, SoKhungXe)
@xe_routes.route("/xe/search", methods=['GET'])
def search_xe():
    try:
        BienSoXe = request.args.get('BienSoXe')
        Mssv = request.args.get('Mssv')
        SoKhungXe = request.args.get('SoKhungXe')
        TenChuXe = request.args.get('TenChuXe')
        LoaiXe = request.args.get('LoaiXe')
        NhanHieu = request.args.get('NhanHieu')
        MauXe = request.args.get('MauXe')

        response_message, status_code = get_xe_by_criteria_service(
            BienSoXe=BienSoXe, Mssv=Mssv, SoKhungXe=SoKhungXe, TenChuXe=TenChuXe, LoaiXe=LoaiXe, NhanHieu=NhanHieu, MauXe=MauXe
        )
        
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Update xe record
@xe_routes.route("/xe/update/<BienSoXe>", methods=['PUT'])
def update_xe(BienSoXe):
    try:
        response_message, status_code = update_xe_service(BienSoXe, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete xe record
@xe_routes.route("/xe/delete/<BienSoXe>", methods=['DELETE'])
def delete_xe(BienSoXe):
    try:
        response_message, status_code = delete_xe_service(BienSoXe)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Delete all xe records
# @xe_routes.route("/xe/delete_all", methods=['DELETE'])
# def delete_all_xes():
#     try:
#         response_message, status_code = delete_all_xes_service()
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400



@xe_routes.route("/xe/delete_all", methods=['DELETE'])
def delete_all_xes():
    try:
        confirmation = request.args.get('confirm', '').lower()
        if confirmation != 'true':
            return jsonify({"error": "Confirmation flag required to delete all xe records"}), 400
        
        response_message, status_code = delete_all_xes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
