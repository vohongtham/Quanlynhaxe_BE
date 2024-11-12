from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from sqlalchemy import func
from app.database import db
from app.model import ChiTietRaVao
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# General statistics query function
def thong_ke_ra_vao(ngay_bat_dau: datetime, ngay_ket_thuc: datetime, ma_baixe: Optional[str] = None) -> Dict[str, Any]:
    logging.info(f"Thực hiện thống kê từ {ngay_bat_dau} đến {ngay_ket_thuc} cho mã bãi xe: {ma_baixe}")

    # Câu truy vấn cơ bản
    query = db.session.query(
        func.count(ChiTietRaVao.Ma_CT).label('so_luot_ra_vao'),
        func.sum(ChiTietRaVao.Gia).label('tong_doanh_thu'),
        func.count(ChiTietRaVao.TG_Ra).label('so_luot_ra'),
        func.count(ChiTietRaVao.TG_Vao).label('so_luot_vao')
    ).filter(
        ChiTietRaVao.TG_Vao >= ngay_bat_dau,
        ChiTietRaVao.TG_Vao <= ngay_ket_thuc
    )

    # Áp dụng bộ lọc bãi xe nếu có
    if ma_baixe:
        query = query.filter(ChiTietRaVao.Ma_BaiXe == ma_baixe)

    try:
        thong_ke = query.first()
    except Exception as e:
        logging.error(f"Lỗi khi thực hiện truy vấn: {e}")
        return {}

    # Kiểm tra nếu không có dữ liệu nào
    if thong_ke is None:
        logging.warning("Không có dữ liệu cho khoảng thời gian này.")
        return {
            "ngay_bat_dau": ngay_bat_dau.strftime('%Y-%m-%d'),
            "ngay_ket_thuc": ngay_ket_thuc.strftime('%Y-%m-%d'),
            "so_luot_ra_vao": 0,
            "tong_doanh_thu": 0.0,
            "so_luot_ra": 0,
            "so_luot_vao": 0,
            "thoi_gian_thuc_hien": datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        }

    # Trích xuất thống kê chung
    so_luot_ra_vao = thong_ke.so_luot_ra_vao or 0
    tong_doanh_thu = thong_ke.tong_doanh_thu or 0.0
    so_luot_ra = thong_ke.so_luot_ra or 0
    so_luot_vao = thong_ke.so_luot_vao or 0
    
    # Thống kê số lượt vào và ra cho ô tô và xe máy
    so_luot_ra_oto = db.session.query(func.count(ChiTietRaVao.TG_Ra), func.sum(ChiTietRaVao.Gia)).filter(
        ChiTietRaVao.LoaiXe == 'Ô tô',
        ChiTietRaVao.TG_Ra >= ngay_bat_dau,
        ChiTietRaVao.TG_Ra <= ngay_ket_thuc,
        ChiTietRaVao.Ma_BaiXe == ma_baixe
    ).first() or (0, 0.0)  # (số lượt ra ô tô, tổng doanh thu ô tô)


    so_luot_vao_oto = db.session.query(func.count(ChiTietRaVao.TG_Vao), func.sum(ChiTietRaVao.Gia)).filter(
        ChiTietRaVao.LoaiXe == 'Ô tô',
        ChiTietRaVao.TG_Vao >= ngay_bat_dau,
        ChiTietRaVao.TG_Vao <= ngay_ket_thuc,
        ChiTietRaVao.Ma_BaiXe == ma_baixe
    ).first()

    so_luot_vao_xemay = db.session.query(func.count(ChiTietRaVao.TG_Vao), func.sum(ChiTietRaVao.Gia)).filter(
        ChiTietRaVao.LoaiXe == 'Xe máy',
        ChiTietRaVao.TG_Vao >= ngay_bat_dau,
        ChiTietRaVao.TG_Vao <= ngay_ket_thuc,
        ChiTietRaVao.Ma_BaiXe == ma_baixe
    ).first()

    so_luot_ra_xemay = db.session.query(func.count(ChiTietRaVao.TG_Ra), func.sum(ChiTietRaVao.Gia)).filter(
        ChiTietRaVao.LoaiXe == 'Xe máy',
        ChiTietRaVao.TG_Ra >= ngay_bat_dau,
        ChiTietRaVao.TG_Ra <= ngay_ket_thuc,
        ChiTietRaVao.Ma_BaiXe == ma_baixe
    ).first() or (0, 0.0)  # (số lượt ra xe máy, tổng doanh thu xe máy)

    # Tính doanh thu
    doanh_thu_oto = so_luot_ra_oto[1] or 0.0  # lấy tổng doanh thu từ ô tô
    doanh_thu_xemay = so_luot_ra_xemay[1] or 0.0  # lấy tổng doanh thu từ xe máy

    tong_doanh_thu = doanh_thu_oto + doanh_thu_xemay

    return {
        "ngay_bat_dau": ngay_bat_dau.strftime('%Y-%m-%d'),
        "ngay_ket_thuc": ngay_ket_thuc.strftime('%Y-%m-%d'),
        "so_luot_ra_vao": so_luot_ra_vao,
        "tong_doanh_thu": tong_doanh_thu,
        "so_luot_ra": so_luot_ra,
        "so_luot_vao": so_luot_vao,
        "so_luot_vao_oto": so_luot_vao_oto[0] or 0,
        "so_luot_ra_oto": so_luot_ra_oto[0] or 0,
        "so_luot_vao_xemay": so_luot_vao_xemay[0] or 0,
        "so_luot_ra_xemay": so_luot_ra_xemay[0] or 0,
        "thoi_gian_thuc_hien_thong_ke": datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    }

def thong_ke_theo_ngay(ngay_thong_ke: str, ma_baixe: Optional[str] = None) -> Dict[str, Any]:
    # Thiết lập ngày bắt đầu và kết thúc
    ngay_bat_dau = datetime.strptime(ngay_thong_ke, "%Y-%m-%d")
    # Thiết lập ngày kết thúc là 23:59:59 của ngày đó
    ngay_ket_thuc = ngay_bat_dau.replace(hour=23, minute=59, second=59)
    
    # Log kiểm tra thời gian đã được xác định đúng
    logging.info(f"Thống kê từ {ngay_bat_dau} đến {ngay_ket_thuc} cho mã bãi xe: {ma_baixe}")
    
    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc, ma_baixe)


def thong_ke_theo_thang(thang: int, nam: int, ma_baixe: Optional[str] = None) -> Dict[str, Any]:
    try:
        # Create the start and end dates for the given month
        ngay_bat_dau = datetime(nam, thang, 1)
        # The end date will be the first day of the next month
        if thang == 12:
            ngay_ket_thuc = datetime(nam + 1, 1, 1)  # January of the next year
        else:
            ngay_ket_thuc = datetime(nam, thang + 1, 1)

        # Call the thong_ke_ra_vao function with the start and end date of the month
        return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc, ma_baixe)
    except Exception as e:
        logging.error(f"Error in thong_ke_theo_thang: {e}")
        return {}


def thong_ke_theo_nam(nam: int, ma_baixe: Optional[str] = None) -> Dict[str, Any]:
    ngay_bat_dau = datetime(nam, 1, 1)
    ngay_ket_thuc = datetime(nam, 12, 31)

    return thong_ke_ra_vao(ngay_bat_dau, ngay_ket_thuc, ma_baixe)

