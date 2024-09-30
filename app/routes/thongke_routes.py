from flask import Blueprint, jsonify, request
from app.services.thongke_service import (
    thong_ke_theo_ngay, 
    thong_ke_theo_tuan, 
    thong_ke_theo_thang, 
    thong_ke_theo_nam
)
from datetime import datetime

thongke_bp = Blueprint('thongke', __name__)

# Route thống kê theo ngày
@thongke_bp.route('/thongke/ngay', methods=['GET'])
def thong_ke_ngay():
    ngay_thong_ke = request.args.get('ngay', default=datetime.today().strftime('%Y-%m-%d'))
    thong_ke = thong_ke_theo_ngay(ngay_thong_ke)
    return jsonify(thong_ke), 200

# Route thống kê theo tuần
@thongke_bp.route('/thongke/tuan', methods=['GET'])
def thong_ke_tuan():
    ngay_thong_ke = request.args.get('ngay', default=datetime.today().strftime('%Y-%m-%d'))
    thong_ke = thong_ke_theo_tuan(ngay_thong_ke)
    return jsonify(thong_ke), 200

# Route thống kê theo tháng
@thongke_bp.route('/thongke/thang', methods=['GET'])
def thong_ke_thang():
    ngay_thong_ke = request.args.get('ngay', default=datetime.today().strftime('%Y-%m-%d'))
    thong_ke = thong_ke_theo_thang(ngay_thong_ke)
    return jsonify(thong_ke), 200

# Route thống kê theo năm
@thongke_bp.route('/thongke/nam', methods=['GET'])
def thong_ke_nam():
    ngay_thong_ke = request.args.get('ngay', default=datetime.today().strftime('%Y-%m-%d'))
    thong_ke = thong_ke_theo_nam(ngay_thong_ke)
    return jsonify(thong_ke), 200
