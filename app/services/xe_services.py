from app.database import db
from app.utils.utils import generate  # Assuming generate() is a function for generating unique IDs if needed
from app.model import Xe, ChiTietRaVao
from flask import request, jsonify
from app.app_ma import XeSchema

# Initialize schema
xe_schema = XeSchema()
xes_schema = XeSchema(many=True)

def add_xe_service(request):
    try:
        data = request.get_json()
        BienSoXe = data.get('BienSoXe')
        Mssv = data.get('Mssv')
        SoKhungXe = data.get('SoKhungXe')
        TenChuXe = data.get('TenChuXe')
        LoaiXe = data.get('LoaiXe')
        DungTich = data.get('DungTich')
        NhanHieu = data.get('NhanHieu')
        MauXe = data.get('MauXe')

        if not BienSoXe or not Mssv or not SoKhungXe:
            return {"error": "Missing required fields: BienSoXe, Mssv, and SoKhungXe are required."}, 400

        # Check if the BienSoXe or SoKhungXe already exists
        if Xe.query.filter_by(BienSoXe=BienSoXe).first():
            return {"error": " Biển số xe đã tồn tại ."}, 400

        if Xe.query.filter_by(SoKhungXe=SoKhungXe).first():
            return {"error": "Số khung xe đã tồn tại."}, 400

        # Create and add the new vehicle
        new_xe = Xe(
            BienSoXe=BienSoXe,
            Mssv=Mssv,
            SoKhungXe=SoKhungXe,
            TenChuXe=TenChuXe,
            LoaiXe=LoaiXe,
            DungTich=DungTich,
            NhanHieu=NhanHieu,
            MauXe=MauXe
        )
        db.session.add(new_xe)
        db.session.commit()

        return {"message": "Xe added successfully!"}, 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Get Xe by criteria
# def get_xe_by_criteria_service(BienSoXe=None, Mssv=None, SoKhungXe=None, TenChuXe=None, LoaiXe=None, NhanHieu=None, MauXe=None):
#     try:
#         query = Xe.query

#         if BienSoXe:
#             query = query.filter(Xe.BienSoXe.ilike(f"%{BienSoXe}%"))
#         if Mssv:
#             query = query.filter(Xe.Mssv.ilike(f"%{Mssv}%"))
#         if SoKhungXe:
#             query = query.filter(Xe.SoKhungXe.ilike(f"%{SoKhungXe}%"))
#         if TenChuXe:
#             query = query.filter(Xe.TenChuXe.ilike(f"%{TenChuXe}%"))
#         if LoaiXe:
#             query = query.filter(Xe.LoaiXe.ilike(f"%{LoaiXe}%"))
#         if NhanHieu:
#             query = query.filter(Xe.NhanHieu.ilike(f"%{NhanHieu}%"))
#         if MauXe:
#             query = query.filter(Xe.MauXe.ilike(f"%{MauXe}%"))

#         xes = query.all()

#         if not xes:
#             return {"message": "No xe records found matching the criteria"}, 404

#         result = xes_schema.dump(xes)
#         return result, 200

#     except Exception as e:
#         return {"error": str(e)}, 400


def get_xe_by_criteria_service(**criteria):
    try:
        query = Xe.query
        for key, value in criteria.items():
            if value:
                query = query.filter(getattr(Xe, key).ilike(f"%{value}%"))
        xes = query.all()
        if not xes:
            return {"message": "No xe records found matching the criteria"}, 404
        result = xes_schema.dump(xes)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400


def get_all_xes_service():
    try:
        xes = Xe.query.all()
        result = xes_schema.dump(xes)
        return result, 200

    except Exception as e:
        return {"error": str(e)}, 400

def update_xe_service(BienSoXe, request):
    try:
        data = request.get_json()
        xe = Xe.query.filter_by(BienSoXe=BienSoXe).first()

        if not xe:
            return {"error": "Xe not found"}, 404

        xe.Mssv = data.get('Mssv', xe.Mssv)
        xe.SoKhungXe = data.get('SoKhungXe', xe.SoKhungXe)
        xe.TenChuXe = data.get('TenChuXe', xe.TenChuXe)
        xe.LoaiXe = data.get('LoaiXe', xe.LoaiXe)
        xe.DungTich = data.get('DungTich', xe.DungTich)
        xe.NhanHieu = data.get('NhanHieu', xe.NhanHieu)
        xe.MauXe = data.get("MauXe", xe.MauXe)

        db.session.commit()
        return {"message": "Xe updated successfully!"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

def delete_xe_service(BienSoXe):
    try:
        xe = Xe.query.filter_by(BienSoXe=BienSoXe).first()

        if not xe:
            return {"error": "Xe not found"}, 404

        db.session.delete(xe)
        db.session.commit()
        return {"message": "Xe deleted successfully!"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# def delete_xe_service(BienSoXe):
#     try:
#         # Step 1: Delete all related entries in ChiTietRaVao
#         ChiTietRaVao.query.filter_by(BienSoXe=BienSoXe).delete()

#         # Step 2: Delete the vehicle from Xe table
#         vehicle = Xe.query.filter_by(BienSoXe=BienSoXe).first()
#         if vehicle:
#             db.session.delete(vehicle)
#             db.session.commit()
#             return {"message": "Vehicle deleted successfully."}
#         else:
#             return {"error": "Vehicle not found."}
#     except Exception as e:
#         db.session.rollback()  # Rollback the session in case of an error
#         return {"error": str(e)}, 400


def delete_all_xes_service():
    try:
        xes = Xe.query.all()

        if not xes:
            return {"message": "No xe records found"}, 404

        for xe in xes:
            db.session.delete(xe)

        db.session.commit()
        return {"message": "All xe records deleted successfully!"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
