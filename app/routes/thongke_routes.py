from flask import Blueprint, jsonify, request
from app.services.thongke_service import (
    thong_ke_theo_ngay,  
    thong_ke_theo_thang, 
    thong_ke_theo_nam
)
from datetime import datetime

thongke_bp = Blueprint('thongke', __name__)

# Function to check and parse date from request
def get_valid_date(date_string):
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return None

@thongke_bp.route('/thongke/ngay', methods=['GET'])
def thong_ke_ngay():
    ngay_thong_ke = request.args.get('ngay', default=datetime.today().strftime('%Y-%m-%d'))
    ma_baixe = request.args.get('ma_baixe', type=str)  # Get Ma_BaiXe from query params
    
    valid_date = get_valid_date(ngay_thong_ke)
    if not valid_date:
        return jsonify({"error": "Ngày không hợp lệ, định dạng yêu cầu là YYYY-MM-DD"}), 400
    
    # Check if ma_baixe is None or empty string
    if not ma_baixe:
        return jsonify({"error": "Mã bãi xe không hợp lệ"}), 400

    thong_ke = thong_ke_theo_ngay(ngay_thong_ke, ma_baixe)  # Pass Ma_BaiXe to the function
    return jsonify(thong_ke), 200

@thongke_bp.route('/thongke/thang', methods=['GET'])
def thong_ke_thang():
    thang = request.args.get('thang', type=int)
    nam = request.args.get('nam', type=int)
    ma_baixe = request.args.get('ma_baixe', type=str)

    if not thang or not nam:
        return jsonify({"error": "Missing 'thang' or 'nam' parameter"}), 400

    thong_ke = thong_ke_theo_thang(thang, nam, ma_baixe)  # Pass Ma_BaiXe to the function
    return jsonify(thong_ke), 200

@thongke_bp.route('/thongke/nam', methods=['GET'])
def thong_ke_nam():
    nam = request.args.get('nam', type=int)
    ma_baixe = request.args.get('ma_baixe', type=str)

    if not nam:
        return jsonify({"error": "Missing 'nam' parameter"}), 400

    thong_ke = thong_ke_theo_nam(nam, ma_baixe)  # Pass Ma_BaiXe to the function
    return jsonify(thong_ke), 200

