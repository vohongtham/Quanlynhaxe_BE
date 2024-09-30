from app.database import db
from app.app_ma import LopSchema
from app.model import Lop
from flask import request, json

lop_schema = LopSchema()
lops_schema = LopSchema(many=True)

# Add Lop
def add_lop_service(request):
    try:
        data = request.get_json()
        Ma_Lop = data.get('Ma_Lop')
        TenLop = data.get('TenLop')
        Ma_Nganh = data.get('Ma_Nganh')

        new_lop = Lop(Ma_Lop=Ma_Lop, TenLop=TenLop, Ma_Nganh=Ma_Nganh)

        db.session.add(new_lop)
        db.session.commit()
        return {"message": "Lop added successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Get Lop by criteria
def get_lop_by_criteria_service(Ma_Lop=None, TenLop=None, Ma_Nganh=None):
    try:
        query = Lop.query

        if Ma_Lop:
            query = query.filter_by(Ma_Lop=Ma_Lop)
        if TenLop:
            query = query.filter(Lop.TenLop.ilike(f"%{TenLop}%"))
        if Ma_Nganh:
            query = query.filter_by(Ma_Nganh=Ma_Nganh)

        lops = query.all()

        if not lops:
            return {"message": "No Lop found matching the criteria"}, 404

        result = lops_schema.dump(lops)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Get all Lops
def get_all_lops_service():
    try:
        lops = Lop.query.all()
        result = lops_schema.dump(lops)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Update Lop
def update_lop_service(Ma_Lop, request):
    try:
        lop = Lop.query.filter_by(Ma_Lop=Ma_Lop).first()

        if not lop:
            return {"error": "Lop not found"}, 404

        data = request.get_json()
        lop.TenLop = data.get('TenLop', lop.TenLop)
        lop.Ma_Nganh = data.get('Ma_Nganh', lop.Ma_Nganh)

        db.session.commit()
        return {"message": "Lop updated successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete Lop
def delete_lop_service(Ma_Lop):
    try:
        lop = Lop.query.filter_by(Ma_Lop=Ma_Lop).first()

        if not lop:
            return {"error": "Lop not found"}, 404

        db.session.delete(lop)
        db.session.commit()
        return {"message": "Lop deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete all Lops
def delete_all_lops_service():
    try:
        lops = Lop.query.all()

        if not lops:
            return {"message": "No Lops found"}, 404

        for lop in lops:
            db.session.delete(lop)

        db.session.commit()
        return {"message": "All Lops deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
