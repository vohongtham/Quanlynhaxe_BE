# from flask import Blueprint, jsonify, request
# from app.services.loaixe_service import (
#     add_loaixe_service,
#     get_all_loaixes_service,
#     get_loaixe_by_criteria_service,
#     update_loaixe_service,
#     delete_loaixe_service,
#     delete_all_loaixes_service
# )

# # Initialize the Blueprint for loaixe routes
# loaixe_routes = Blueprint("loaixe_routes", __name__)

# # Route to add a new LoaiXe
# @loaixe_routes.route("/loaixe/add", methods=['POST'])
# def add_loaixe():
#     try:
#         response_message, status_code = add_loaixe_service(request)
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # Route to search LoaiXe by criteria
# @loaixe_routes.route("/loaixe/search", methods=['GET'])
# def search_loaixe():
#     try:
#         LoaiXe = request.args.get('LoaiXe')
#         Gia = request.args.get('Gia')

#         response_message, status_code = get_loaixe_by_criteria_service(LoaiXe=LoaiXe, Gia=Gia)
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # Route to get all LoaiXe
# @loaixe_routes.route("/loaixe/all", methods=['GET'])
# def get_all_loaixes():
#     try:
#         response_message, status_code = get_all_loaixes_service()
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # Route to update a LoaiXe
# @loaixe_routes.route("/loaixe/update/<LoaiXe>", methods=['PUT'])
# def update_loaixe(LoaiXe):
#     try:
#         response_message, status_code = update_loaixe_service(LoaiXe, request)
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # Route to delete a specific LoaiXe
# @loaixe_routes.route("/loaixe/delete/<LoaiXe>", methods=['DELETE'])
# def delete_loaixe(LoaiXe):
#     try:
#         response_message, status_code = delete_loaixe_service(LoaiXe)
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# # Route to delete all LoaiXe
# @loaixe_routes.route("/loaixe/delete_all", methods=['DELETE'])
# def delete_all_loaixes():
#     try:
#         response_message, status_code = delete_all_loaixes_service()
#         return jsonify(response_message), status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400


from flask import Blueprint, jsonify, request
from app.services.loaixe_service import (
    add_loaixe_service, 
    get_all_loaixes_service, 
    get_loaixe_by_criteria_service, 
    update_loaixe_service, 
    delete_loaixe_service, 
    delete_all_loaixes_service
)

loaixe_routes = Blueprint("loaixe_routes", __name__)

# Add LoaiXe
@loaixe_routes.route("/loaixe/add", methods=['POST'])
def add_loaixe():
    try:
        response_message, status_code = add_loaixe_service(request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route search LoaiXe
@loaixe_routes.route("/loaixe/search", methods=['GET'])
def search_loaixe():
    try:
        # Get parameters from the query string
        loai_xe_name = request.args.get('LoaiXe')
        gia = request.args.get('Gia')

        # Pass the parameters to the service with correct names
        response_message, status_code = get_loaixe_by_criteria_service(loai_xe_name=loai_xe_name, gia=gia)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route get all LoaiXe
@loaixe_routes.route("/loaixe/all", methods=['GET'])
def get_all_loaixes():
    try:
        response_message, status_code = get_all_loaixes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route update LoaiXe
@loaixe_routes.route("/loaixe/update/<LoaiXe>", methods=['PUT'])
def update_loaixe(LoaiXe):
    try:
        response_message, status_code = update_loaixe_service(LoaiXe, request)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete LoaiXe
@loaixe_routes.route("/loaixe/delete/<LoaiXe>", methods=['DELETE'])
def delete_loaixe(LoaiXe):
    try:
        response_message, status_code = delete_loaixe_service(LoaiXe)
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route delete all LoaiXe
@loaixe_routes.route("/loaixe/delete_all", methods=['DELETE'])
def delete_all_loaixes():
    try:
        response_message, status_code = delete_all_loaixes_service()
        return jsonify(response_message), status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 400
