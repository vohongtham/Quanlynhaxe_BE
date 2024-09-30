from app.database import db
from app.model import ChiTietRaVao, Xe
from app.app_ma import ChiTietRaVaoSchema
from app.utils.utils import generate
from flask import request
from datetime import datetime
from sqlalchemy import func

ct_rv_schema = ChiTietRaVaoSchema()
ct_rvs_schema = ChiTietRaVaoSchema(many=True)

def add_chitiet_ravao_service(request):
    try:
        # Retrieve data from the request
        data = request.get_json()
        BienSoXe = data.get('BienSoXe')
        Ma_BaiXe = data.get('Ma_BaiXe')

        # Validate required fields
        if not BienSoXe or not Ma_BaiXe:
            return {"error": "Missing required fields: BienSoXe and Ma_BaiXe are required."}, 400

        # Retrieve Mssv from Xe table using BienSoXe
        xe_record = Xe.query.filter_by(BienSoXe=BienSoXe).first()
        if not xe_record:
            return {"error": "BienSoXe does not match any vehicle in the system."}, 400

        Mssv = xe_record.Mssv

        # Check for an existing entry with TG_Ra as NULL for the same vehicle (indicating it's still in the parking lot)
        existing_entry = ChiTietRaVao.query.filter_by(Mssv=Mssv, BienSoXe=BienSoXe, TG_Ra=None).first()

        if existing_entry:
            # Update TG_Ra only, leave TG_Vao unchanged
            existing_entry.TG_Ra = datetime.now()  # Vehicle is exiting
            existing_entry.Gia = 2000  # Fixed fee amount
            db.session.commit()
            return {"message": "Exit time (TG_Ra) recorded successfully!", "Ma_CT": existing_entry.Ma_CT, "Gia": existing_entry.Gia}, 200
        else:
            # Vehicle is entering; create a new record with TG_Vao
            new_ct_ravao = ChiTietRaVao(
                Ma_CT=generate_unique_ma_ct(),  # Generate a unique Ma_CT
                Mssv=Mssv,
                BienSoXe=BienSoXe,
                Ma_BaiXe=Ma_BaiXe,
                TG_Vao=datetime.now(),  # Record the entry time
                TG_Ra=None,  # No exit time yet
                Gia=0  # No fee at entry
            )

            db.session.add(new_ct_ravao)
            db.session.commit()
            return {"message": "Entry time (TG_Vao) recorded successfully!", "Ma_CT": new_ct_ravao.Ma_CT}, 201
    except Exception as e:
        db.session.rollback()
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

# Service: Get ChiTietRaVao by Ma_CT
# def get_chitiet_ravao_by_id_service(Ma_CT):
#     try:
#         # Query the database for ChiTietRaVao by Ma_CT
#         chitiet_ravao = ChiTietRaVao.query.filter_by(Ma_CT=Ma_CT).first()

#         # Check if the entry exists
#         if not chitiet_ravao:
#             return {"error": "ChiTietRaVao not found"}, 404

#         # Serialize the result
#         result = ct_rv_schema.dump(chitiet_ravao)
#         return result, 200
#     except Exception as e:
#         return {"error": str(e)}, 400

def get_chitiet_ravao_by_criteria_service(Ma_CT=None, Mssv=None, BienSoXe=None, Ma_BaiXe=None, TG_Vao=None, TG_Ra=None):
    """
    Service function to retrieve ChiTietRaVao records by various criteria such as Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, and TG_Ra.
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
        if TG_Vao:
            query = query.filter(func.date(ChiTietRaVao.TG_Vao) == TG_Vao)
        if TG_Ra:
            query = query.filter(func.date(ChiTietRaVao.TG_Ra) == TG_Ra)

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
