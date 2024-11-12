from app.database import db
from app.model import ChiTietRaVao, Xe, BaiXe, Sinhvien, LoaiXe
from app.app_ma import ChiTietRaVaoSchema
from app.utils.utils import generate
from flask import request
from datetime import datetime
from sqlalchemy import func
from app.services.email_service import send_email  # Import hàm send_email từ service # Import hàm send_email

ct_rv_schema = ChiTietRaVaoSchema()
ct_rvs_schema = ChiTietRaVaoSchema(many=True)

# def add_chitiet_ravao_service(request):
#     try:
#         data = request.get_json()
#         print("Received data:", data)  # Log the incoming data
#         BienSoXe = data.get('BienSoXe')
#         Ma_BaiXe = data.get('Ma_BaiXe')
#         AnhBienSo = data.get('AnhBienSo')

#         if not BienSoXe or not Ma_BaiXe:
#             return {"error": "Thiếu trường bắt buộc: BienSoXe và Ma_BaiXe là cần thiết."}, 400

#         xe_record = Xe.query.filter_by(BienSoXe=BienSoXe).first()
#         if not xe_record:
#             return {"error": "Biển số xe không khớp với bất kỳ xe nào trong hệ thống."}, 400

#         Mssv = xe_record.Mssv
#         sinh_vien_record = Sinhvien.query.filter_by(Mssv=Mssv).first()
#         if not sinh_vien_record:
#             return {"error": "MSSV không khớp với bất kỳ sinh viên nào trong hệ thống."}, 400

#         email_recipient = sinh_vien_record.Email
#         existing_entry = ChiTietRaVao.query.filter_by(Mssv=Mssv, BienSoXe=BienSoXe, TG_Ra=None).first()

#         bai_xe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()
#         if not bai_xe:
#             return {"error": "Bãi xe không tìm thấy."}, 400

#         if existing_entry:
#             if existing_entry.Ma_BaiXe != Ma_BaiXe:
#                 return {"error": "Mã bãi xe không khớp với mã đã sử dụng khi vào."}, 400
            
#             # Set exit time
#             existing_entry.TG_Ra = datetime.now()

#             # Get the price based solely on the vehicle type
#             loai_xe_record = LoaiXe.query.filter_by(LoaiXe=xe_record.LoaiXe).first()
#             if not loai_xe_record:
#                 return {"error": "Loại xe không tìm thấy."}, 400
            
#             # Use the price from LoaiXe as the exit fee
#             existing_entry.Gia = loai_xe_record.Gia  # Use the price from LoaiXe directly

#             bai_xe.So_ViTriDaDung = max(bai_xe.So_ViTriDaDung - 1, 0)
#             db.session.commit()

#             return {
#                 "message": "Thời gian ra (TG_Ra) đã được ghi nhận thành công!",
#                 "status": "exit",
#                 "Ma_CT": existing_entry.Ma_CT,
#                 "Gia": existing_entry.Gia,
#                 "TG_Vao": existing_entry.TG_Vao,
#                 "TG_Ra": existing_entry.TG_Ra,
#                 "So_ViTriTrong": bai_xe.So_ViTriTong - bai_xe.So_ViTriDaDung
#             }, 200
#         else:
#             # Retrieve the vehicle type from xe_record
#             loai_xe = xe_record.LoaiXe  # Assuming LoaiXe is an attribute of xe_record

#             new_ct_ravao = ChiTietRaVao(
#                 Ma_CT=generate_unique_ma_ct(),
#                 Mssv=Mssv,
#                 BienSoXe=BienSoXe,
#                 Ma_BaiXe=Ma_BaiXe,
#                 TG_Vao=datetime.now(),
#                 TG_Ra=None,
#                 Gia=0,  # Initially set to 0
#                 AnhBienSo=AnhBienSo,
#                 LoaiXe=loai_xe  # Include LoaiXe
#             )

#             db.session.add(new_ct_ravao)
#             bai_xe.So_ViTriDaDung += 1
#             db.session.commit()

#             send_email(email_recipient, new_ct_ravao.Ma_CT)

#             return {
#                 "message": "Thời gian vào (TG_Vao) đã được ghi nhận thành công và email đã được gửi!",
#                 "status": "entry",
#                 "Ma_CT": new_ct_ravao.Ma_CT,
#                 "TG_Vao": new_ct_ravao.TG_Vao,
#                 "So_ViTriTrong": bai_xe.So_ViTriTong - bai_xe.So_ViTriDaDung
#             }, 201
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400

def add_chitiet_ravao_service(request):
    try:
        data = request.get_json()
        print("Received data:", data)
        BienSoXe = data.get('BienSoXe')
        Ma_BaiXe = data.get('Ma_BaiXe')
        AnhBienSo = data.get('AnhBienSo')
        Ma_CT_input = data.get('Ma_CT')  # Lấy Ma_CT từ yêu cầu (nếu có)

        if not BienSoXe or not Ma_BaiXe:
            return {"error": "Thiếu trường bắt buộc: BienSoXe và Ma_BaiXe là cần thiết."}, 400

        xe_record = Xe.query.filter_by(BienSoXe=BienSoXe).first()
        if not xe_record:
            return {"error": "Biển số xe không khớp với bất kỳ xe nào trong hệ thống."}, 400

        Mssv = xe_record.Mssv
        sinh_vien_record = Sinhvien.query.filter_by(Mssv=Mssv).first()
        if not sinh_vien_record:
            return {"error": "MSSV không khớp với bất kỳ sinh viên nào trong hệ thống."}, 400

        # Kiểm tra xe đang ở trong bãi (TG_Ra = None)
        existing_entry = ChiTietRaVao.query.filter_by(Mssv=Mssv, BienSoXe=BienSoXe, TG_Ra=None).first()
        if existing_entry:
            # Nếu xe đang ở trong bãi nhưng không có Ma_CT, yêu cầu cung cấp Ma_CT để ra
            if not Ma_CT_input:
                return {
                    "warn": "Vui lòng cung cấp mã thẻ xe để xác nhận xe ra.",
                    "status": "need_Ma_CT"
                }, 200  # Thay đổi từ 400 thành 200
                
            if existing_entry.Ma_BaiXe != Ma_BaiXe:
                return {"error": "Mã bãi xe không khớp với mã đã sử dụng khi vào."}, 400
            
            # Nếu Ma_CT được cung cấp, kiểm tra tính hợp lệ của Ma_CT
            if existing_entry.Ma_CT != Ma_CT_input:
                return {
                    # "error": "Mã thẻ xe không khớp.",
                    "status": "Mã thẻ xe không khớp"
                }, 200

            # Xử lý xác nhận ra
            existing_entry.TG_Ra = datetime.now()
            loai_xe_record = LoaiXe.query.filter_by(LoaiXe=xe_record.LoaiXe).first()
            if not loai_xe_record:
                return {"error": "Loại xe không tìm thấy."}, 400

            existing_entry.Gia = loai_xe_record.Gia
            bai_xe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()
            bai_xe.So_ViTriDaDung = max(bai_xe.So_ViTriDaDung - 1, 0)
            db.session.commit()

            return {
                "message": "Thời gian ra (TG_Ra) đã được ghi nhận thành công!",
                "status": "exit",
                "Ma_CT": existing_entry.Ma_CT,
                "Gia": existing_entry.Gia,
                "TG_Vao": existing_entry.TG_Vao,
                "TG_Ra": existing_entry.TG_Ra,
                "So_ViTriTrong": bai_xe.So_ViTriTong - bai_xe.So_ViTriDaDung
            }, 200

        else:
            # Nếu xe không ở trong bãi, xử lý ghi nhận xe vào
            loai_xe = xe_record.LoaiXe
            new_ct_ravao = ChiTietRaVao(
                Ma_CT=generate_unique_ma_ct(),
                Mssv=Mssv,
                BienSoXe=BienSoXe,
                Ma_BaiXe=Ma_BaiXe,
                TG_Vao=datetime.now(),
                TG_Ra=None,
                Gia=0,  # Giá ban đầu bằng 0
                AnhBienSo=AnhBienSo,
                LoaiXe=loai_xe
            )

            db.session.add(new_ct_ravao)
            bai_xe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()
            bai_xe.So_ViTriDaDung += 1
            db.session.commit()

            send_email(sinh_vien_record.Email, new_ct_ravao.Ma_CT)

            return {
                "message": "Thời gian vào (TG_Vao) đã được ghi nhận thành công và email đã được gửi!",
                "status": "entry",
                "Ma_CT": new_ct_ravao.Ma_CT,
                "TG_Vao": new_ct_ravao.TG_Vao,
                "So_ViTriTrong": bai_xe.So_ViTriTong - bai_xe.So_ViTriDaDung
            }, 201

    except Exception as e:
        db.session.rollback()
        print(f"Error: {e}")  # Ghi log chi tiết lỗi
        return {"error": str(e)}, 400


def generate_unique_ma_ct():
    # Generate a unique Ma_CT and ensure it doesn't collide with existing records
    while True:
        Ma_CT = generate()  # Ensure the generate function provides a unique identifier
        if not ChiTietRaVao.query.filter_by(Ma_CT=Ma_CT).first():
            return Ma_CT


# Service: Get all ChiTietRaVao
def get_all_chitiet_ravao_service():
    try:
        # Query the database for all ChiTietRaVao
        chitiet_ravao = ChiTietRaVao.query.all()

        # Serialize the result
        result = ct_rvs_schema.dump(chitiet_ravao)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# def get_chitiet_ravao_by_criteria_service(Ma_CT=None, Mssv=None, BienSoXe=None, Ma_BaiXe=None, TG_Vao=None, TG_Ra=None, LoaiXe=None, AnhBienSo=None):
#     """
#     Service function to retrieve ChiTietRaVao records by various criteria such as Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, TG_Ra, LoaiXe, and AnhBienSo.
#     Supports partial matches and any combination of these criteria.
#     Returns the list of ChiTietRaVao details in JSON format or an error message if no records are found.
#     """
#     try:
#         # Build the query based on the provided criteria
#         query = ChiTietRaVao.query

#         if Ma_CT:
#             query = query.filter_by(Ma_CT=Ma_CT)
#         if Mssv:
#             query = query.filter_by(Mssv=Mssv)
#         if BienSoXe:
#             query = query.filter(ChiTietRaVao.BienSoXe.ilike(f"%{BienSoXe}%"))
#         if Ma_BaiXe:
#             query = query.filter_by(Ma_BaiXe=Ma_BaiXe)
#         if TG_Vao:
#             query = query.filter(func.date(ChiTietRaVao.TG_Vao) == TG_Vao)
#         if TG_Ra:
#             query = query.filter(func.date(ChiTietRaVao.TG_Ra) == TG_Ra)
#         if LoaiXe:
#             query = query.filter(ChiTietRaVao.LoaiXe.ilike(f"%{LoaiXe}%"))
#         if AnhBienSo:
#             query = query.filter(AnhBienSo=AnhBienSo)

#         # Execute the query to find matching records
#         chitiet_ravao_list = query.all()

#         # Check if any records were found
#         if not chitiet_ravao_list:
#             return {"message": "No ChiTietRaVao records found matching the criteria"}, 404

#         # Serialize the result data
#         result = ct_rv_schema.dump(chitiet_ravao_list, many=True)
#         return result, 200  # Return the serialized data and status code
#     except Exception as e:
#         return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong


def get_chitiet_ravao_by_criteria_service(Ma_CT=None, Mssv=None, BienSoXe=None, Ma_BaiXe=None, TG_Vao=None, TG_Ra=None, LoaiXe=None, AnhBienSo=None):
    """
    Service function to retrieve ChiTietRaVao records by various criteria such as Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, TG_Ra, LoaiXe, and AnhBienSo.
    Supports partial matches and any combination of these criteria.
    Returns the list of ChiTietRaVao details in JSON format or an error message if no records are found.
    """
    try:
        # Build the query based on the provided criteria
        query = ChiTietRaVao.query

        if Ma_CT:
            query = query.filter_by(Ma_CT=Ma_CT)
        if Mssv:
            query = query.filter_by(Mssv=Mssv)
        if BienSoXe:
            query = query.filter(ChiTietRaVao.BienSoXe.ilike(f"%{BienSoXe}%"))
        if Ma_BaiXe:
            query = query.filter_by(Ma_BaiXe=Ma_BaiXe)
        
        # Tìm kiếm theo TG_Vao với cả thời gian đầy đủ và chỉ ngày
        if TG_Vao:
            if len(TG_Vao) == 10:  # Định dạng yyyy-mm-dd
                query = query.filter(func.date(ChiTietRaVao.TG_Vao) == TG_Vao)
            else:  # Định dạng yyyy-mm-dd hh:mm:ss
                query = query.filter(ChiTietRaVao.TG_Vao == TG_Vao)
        
        # Tìm kiếm theo TG_Ra với cả thời gian đầy đủ và chỉ ngày
        if TG_Ra:
            if len(TG_Ra) == 10:  # Định dạng yyyy-mm-dd
                query = query.filter(func.date(ChiTietRaVao.TG_Ra) == TG_Ra)
            else:  # Định dạng yyyy-mm-dd hh:mm:ss
                query = query.filter(ChiTietRaVao.TG_Ra == TG_Ra)

        if LoaiXe:
            query = query.filter(ChiTietRaVao.LoaiXe.ilike(f"%{LoaiXe}%"))
        if AnhBienSo:
            query = query.filter(ChiTietRaVao.AnhBienSo == AnhBienSo)

        # Execute the query to find matching records
        chitiet_ravao_list = query.all()

        # Check if any records were found
        if not chitiet_ravao_list:
            return {"message": "No ChiTietRaVao records found matching the criteria"}, 404

        # Serialize the result data
        result = ct_rv_schema.dump(chitiet_ravao_list, many=True)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong


# Service: Update ChiTietRaVao
def update_chitiet_ravao_service(Ma_CT, request):
    try:
        # Query the database for ChiTietRaVao by Ma_CT
        chitiet_ravao = ChiTietRaVao.query.filter_by(Ma_CT=Ma_CT).first()

        # Check if the entry exists
        if not chitiet_ravao:
            return {"error": "ChiTietRaVao not found"}, 404

        # Retrieve data from the request and update the fields
        data = request.get_json()
        chitiet_ravao.Mssv = data.get('Mssv', chitiet_ravao.Mssv)
        chitiet_ravao.BienSoXe = data.get('BienSoXe', chitiet_ravao.BienSoXe)
        chitiet_ravao.Ma_BaiXe = data.get('Ma_BaiXe', chitiet_ravao.Ma_BaiXe)
        chitiet_ravao.TG_Vao = data.get('TG_Vao', chitiet_ravao.TG_Vao)
        chitiet_ravao.TG_Ra = data.get('TG_Ra', chitiet_ravao.TG_Ra)
        chitiet_ravao.Gia = data.get('Gia', chitiet_ravao.Gia)

        # Commit the changes to the database
        db.session.commit()
        return {"message": "ChiTietRaVao updated successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Service: Delete ChiTietRaVao by Ma_CT
def delete_chitiet_ravao_service(Ma_CT):
    try:
        # Query the database for ChiTietRaVao by Ma_CT
        chitiet_ravao = ChiTietRaVao.query.filter_by(Ma_CT=Ma_CT).first()

        # Check if the entry exists
        if not chitiet_ravao:
            return {"error": "ChiTietRaVao not found"}, 404

        # Delete the entry from the database
        db.session.delete(chitiet_ravao)
        db.session.commit()
        return {"message": "ChiTietRaVao deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400


# Service: Delete all ChiTietRaVao records
def delete_all_chitiet_ravao_service():
    try:
        # Query the database to get all ChiTietRaVao records
        chitiet_ravao_records = ChiTietRaVao.query.all()

        # Check if there are any records to delete
        if not chitiet_ravao_records:
            return {"error": "No ChiTietRaVao records found"}, 404

        # Loop through each record and delete it
        for record in chitiet_ravao_records:
            db.session.delete(record)

        # Commit the changes to the database
        db.session.commit()

        return {"message": "All ChiTietRaVao records deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
