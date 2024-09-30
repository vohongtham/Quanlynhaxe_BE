from datetime import datetime, timedelta
from sqlalchemy import func
from app.database import db
from app.model import ChiTietRaVao

# Hàm chung để truy vấn thống kê ra/vào và tổng doanh thu
def thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc):
    thong_ke = db.session.query(
        func.count(ChiTietRaVao.Ma_CT).label('so_luot_ra_vao'),
        func.sum(ChiTietRaVao.Gia).label('tong_doanh_thu'),
        func.count(ChiTietRaVao.TG_Ra).label('so_luot_ra'),
        func.count(ChiTietRaVao.TG_Vao).label('so_luot_vao')
    ).filter(
        ChiTietRaVao.TG_Vao >= ngay_bat_dau,
        ChiTietRaVao.TG_Vao <= ngay_ket_thuc
    ).first()

    so_luot_ra_vao = thong_ke.so_luot_ra_vao or 0
    tong_doanh_thu = thong_ke.tong_doanh_thu or 0.0
    so_luot_ra = thong_ke.so_luot_ra or 0
    so_luot_vao = thong_ke.so_luot_vao or 0

    return {
        "ngay_bat_dau": ngay_bat_dau.strftime('%Y-%m-%d'),
        "ngay_ket_thuc": ngay_ket_thuc.strftime('%Y-%m-%d'),
        "so_luot_ra_vao": so_luot_ra_vao,
        "tong_doanh_thu": tong_doanh_thu,
        "so_luot_ra": so_luot_ra,
        "so_luot_vao": so_luot_vao
    }

# Thống kê theo ngày
def thong_ke_theo_ngay(ngay_thong_ke):
    ngay_bat_dau = datetime.strptime(ngay_thong_ke, "%Y-%m-%d")
    ngay_ket_thuc = ngay_bat_dau.replace(hour=23, minute=59, second=59)

    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc)

# Thống kê theo tuần
def thong_ke_theo_tuan(ngay_thong_ke):
    ngay_bat_dau = datetime.strptime(ngay_thong_ke, "%Y-%m-%d")
    ngay_ket_thuc = ngay_bat_dau + timedelta(days=6)

    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc)

# Thống kê theo tháng
def thong_ke_theo_thang(ngay_thong_ke):
    ngay_bat_dau = datetime.strptime(ngay_thong_ke, "%Y-%m-%d").replace(day=1)
    ngay_ket_thuc = (ngay_bat_dau + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc)

# Thống kê theo năm
def thong_ke_theo_nam(ngay_thong_ke):
    ngay_bat_dau = datetime.strptime(ngay_thong_ke, "%Y-%m-%d").replace(month=1, day=1)
    ngay_ket_thuc = ngay_bat_dau.replace(month=12, day=31)

    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc)
