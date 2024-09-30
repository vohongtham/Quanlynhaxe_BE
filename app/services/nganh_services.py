from app.database import db
from app.app_ma import NganhSchema
from app.model import Nganh

nganh_schema = NganhSchema()
nganhs_schema = NganhSchema(many=True)

# Add Nganh
def add_nganh_service(request):
    try:
        data = request.get_json()
        Ma_Nganh = data.get('Ma_Nganh')
        TenNganh = data.get('TenNganh')
        Ma_DV = data.get('Ma_DV')

        new_nganh = Nganh(Ma_Nganh=Ma_Nganh, TenNganh=TenNganh, Ma_DV=Ma_DV)

        db.session.add(new_nganh)
        db.session.commit()
        return {"message": "Nganh added successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Get Nganh by criteria
def get_nganh_by_criteria_service(Ma_Nganh=None, TenNganh=None, Ma_DV=None):
    try:
        query = Nganh.query

        if Ma_Nganh:
            query = query.filter_by(Ma_Nganh=Ma_Nganh)
        if TenNganh:
            query = query.filter(Nganh.TenNganh.ilike(f"%{TenNganh}%"))
        if Ma_DV:
            query = query.filter_by(Ma_DV=Ma_DV)

        nganhs = query.all()

        if not nganhs:
            return {"message": "No Nganh found matching the criteria"}, 404

        result = nganhs_schema.dump(nganhs)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Get all Nganh
def get_all_nganhs_service():
    try:
        nganhs = Nganh.query.all()
        result = nganhs_schema.dump(nganhs)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Update Nganh
def update_nganh_service(Ma_Nganh, request):
    try:
        nganh = Nganh.query.filter_by(Ma_Nganh=Ma_Nganh).first()

        if not nganh:
            return {"error": "Nganh not found"}, 404

        data = request.get_json()
        nganh.TenNganh = data.get('TenNganh', nganh.TenNganh)

        db.session.commit()
        return {"message": "Nganh updated successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete Nganh
def delete_nganh_service(Ma_Nganh):
    try:
        nganh = Nganh.query.filter_by(Ma_Nganh=Ma_Nganh).first()

        if not nganh:
            return {"error": "Nganh not found"}, 404

        db.session.delete(nganh)
        db.session.commit()
        return {"message": "Nganh deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete all Nganh
def delete_all_nganhs_service():
    try:
        nganhs = Nganh.query.all()

        if not nganhs:
            return {"message": "No Nganh found"}, 404

        for nganh in nganhs:
            db.session.delete(nganh)

        db.session.commit()
        return {"message": "All Nganhs deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
