from app.database import db
from app.app_ma import PhanquyenSchema
from app.model import Phanquyen
from flask import request

phanquyen_schema = PhanquyenSchema()
phanquyens_schema = PhanquyenSchema(many=True)

# Add Phanquyen
def add_phanquyen_service(request):
    try:
        data = request.get_json()
        Ma_Quyen = data.get('Ma_Quyen')
        TenQuyen = data.get('TenQuyen')

        new_phanquyen = Phanquyen(Ma_Quyen=Ma_Quyen, TenQuyen=TenQuyen)

        db.session.add(new_phanquyen)
        db.session.commit()
        return {"message": "Phanquyen added successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Get Phanquyen by criteria
def get_phanquyen_by_criteria_service(Ma_Quyen=None, TenQuyen=None):
    try:
        query = Phanquyen.query

        if Ma_Quyen:
            query = query.filter_by(Ma_Quyen=Ma_Quyen)
        if TenQuyen:
            query = query.filter(Phanquyen.TenQuyen.ilike(f"%{TenQuyen}%"))

        phanquyens = query.all()

        if not phanquyens:
            return {"message": "No Phanquyen found matching the criteria"}, 404

        result = phanquyens_schema.dump(phanquyens)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Get all Phanquyens
def get_all_phanquyens_service():
    try:
        phanquyens = Phanquyen.query.all()
        result = phanquyens_schema.dump(phanquyens)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Update Phanquyen
def update_phanquyen_service(Ma_Quyen, request):
    try:
        phanquyen = Phanquyen.query.filter_by(Ma_Quyen=Ma_Quyen).first()

        if not phanquyen:
            return {"error": "Phanquyen not found"}, 404

        data = request.get_json()
        phanquyen.TenQuyen = data.get('TenQuyen', phanquyen.TenQuyen)

        db.session.commit()
        return {"message": "Phanquyen updated successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete Phanquyen
def delete_phanquyen_service(Ma_Quyen):
    try:
        phanquyen = Phanquyen.query.filter_by(Ma_Quyen=Ma_Quyen).first()

        if not phanquyen:
            return {"error": "Phanquyen not found"}, 404

        db.session.delete(phanquyen)
        db.session.commit()
        return {"message": "Phanquyen deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete all Phanquyens
def delete_all_phanquyens_service():
    try:
        phanquyens = Phanquyen.query.all()

        if not phanquyens:
            return {"message": "No Phanquyens found"}, 404

        for phanquyen in phanquyens:
            db.session.delete(phanquyen)

        db.session.commit()
        return {"message": "All Phanquyens deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

