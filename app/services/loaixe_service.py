# from app.database import db
# from app.app_ma import LoaiXeSchema
# from app.model import LoaiXe
# from flask import request

# loaixe_schema = LoaiXeSchema()
# loaixes_schema = LoaiXeSchema(many=True)

# # Add LoaiXe
# def add_loaixe_service(request):
#     try:
#         # Retrieve data from the request
#         data = request.get_json()
#         LoaiXe = data.get('LoaiXe')
#         Gia = data.get('Gia')

#         # Create a new LoaiXe instance
#         new_loaixe = LoaiXe(LoaiXe=LoaiXe, Gia=Gia)

#         # Add the new LoaiXe to the database
#         db.session.add(new_loaixe)
#         db.session.commit()
#         return {"message": "LoaiXe added successfully!"}, 201
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400

# # Get LoaiXe by criteria
# def get_loaixe_by_criteria_service(LoaiXe=None, Gia=None):
#     try:
#         # Build the query based on provided criteria
#         query = LoaiXe.query
#         if LoaiXe:
#             query = query.filter_by(LoaiXe=LoaiXe)
#         if Gia:
#             query = query.filter_by(Gia=Gia)

#         # Execute the query to find the LoaiXe
#         loaixes = query.all()

#         # Check if any LoaiXe were found
#         if not loaixes:
#             return {"message": "No LoaiXe found matching the criteria"}, 404

#         # Serialize the LoaiXe data
#         result = loaixes_schema.dump(loaixes)
#         return result, 200
#     except Exception as e:
#         return {"error": str(e)}, 400

# # Get all LoaiXe
# def get_all_loaixes_service():
#     try:
#         # Query the database for all LoaiXe
#         loaixes = LoaiXe.query.all()

#         # Serialize the list of LoaiXe
#         result = loaixes_schema.dump(loaixes)
#         return result, 200
#     except Exception as e:
#         return {"error": str(e)}, 400

# # Update LoaiXe
# def update_loaixe_service(LoaiXe, request):
#     try:
#         # Query the database for the LoaiXe with the given identifier
#         loaixe = LoaiXe.query.filter_by(LoaiXe=LoaiXe).first()

#         # Check if the LoaiXe exists
#         if not loaixe:
#             return {"error": "LoaiXe not found"}, 404

#         # Retrieve data from the request and update the LoaiXe details
#         data = request.get_json()
#         loaixe.Gia = data.get('Gia', loaixe.Gia)

#         # Commit the changes to the database
#         db.session.commit()
#         return {"message": "LoaiXe updated successfully!"}, 200
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400

# # Delete LoaiXe
# def delete_loaixe_service(LoaiXe):
#     try:
#         # Query the database for the LoaiXe with the given identifier
#         loaixe = LoaiXe.query.filter_by(LoaiXe=LoaiXe).first()

#         # Check if the LoaiXe exists
#         if not loaixe:
#             return {"error": "LoaiXe not found"}, 404

#         # Delete the LoaiXe from the database
#         db.session.delete(loaixe)
#         db.session.commit()
#         return {"message": "LoaiXe deleted successfully!"}, 200
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400

# # Delete all LoaiXe
# def delete_all_loaixes_service():
#     try:
#         # Query the database for all LoaiXe
#         loaixes = LoaiXe.query.all()

#         # Check if there are any LoaiXe in the database
#         if not loaixes:
#             return {"message": "No LoaiXe found"}, 404

#         # Delete all LoaiXe from the database
#         for loaixe in loaixes:
#             db.session.delete(loaixe)

#         db.session.commit()
#         return {"message": "All LoaiXe deleted successfully!"}, 200
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400



from app.database import db
from app.app_ma import LoaiXeSchema
from app.model import LoaiXe
from flask import request

loaixe_schema = LoaiXeSchema()
loaixes_schema = LoaiXeSchema(many=True)

# Add LoaiXe
def add_loaixe_service(request):
    try:
        # Retrieve data from the request
        data = request.get_json()
        loai_xe_name = data.get('LoaiXe')
        gia = data.get('Gia')

        # Create a new LoaiXe instance
        new_loaixe = LoaiXe(LoaiXe=loai_xe_name, Gia=gia)

        # Add the new LoaiXe to the database
        db.session.add(new_loaixe)
        db.session.commit()
        return {"message": "LoaiXe added successfully!"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Get LoaiXe by criteria
def get_loaixe_by_criteria_service(loai_xe_name=None, gia=None):
    try:
        # Build the query based on provided criteria
        query = LoaiXe.query
        if loai_xe_name:
            query = query.filter_by(LoaiXe=loai_xe_name)
        if gia:
            query = query.filter_by(Gia=gia)

        # Execute the query to find the LoaiXe
        loaixes = query.all()

        # Check if any LoaiXe were found
        if not loaixes:
            return {"message": "No LoaiXe found matching the criteria"}, 404

        # Serialize the LoaiXe data
        result = loaixes_schema.dump(loaixes)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Get all LoaiXe
def get_all_loaixes_service():
    try:
        # Query the database for all LoaiXe
        loaixes = LoaiXe.query.all()

        # Serialize the list of LoaiXe
        result = loaixes_schema.dump(loaixes)
        return result, 200
    except Exception as e:
        return {"error": str(e)}, 400

# Update LoaiXe
def update_loaixe_service(loai_xe_name, request):
    try:
        # Query the database for the LoaiXe with the given identifier
        loaixe = LoaiXe.query.filter_by(LoaiXe=loai_xe_name).first()

        # Check if the LoaiXe exists
        if not loaixe:
            return {"error": "LoaiXe not found"}, 404

        # Retrieve data from the request and update the LoaiXe details
        data = request.get_json()
        loaixe.Gia = data.get('Gia', loaixe.Gia)

        # Commit the changes to the database
        db.session.commit()
        return {"message": "LoaiXe updated successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete LoaiXe
def delete_loaixe_service(loai_xe_name):
    try:
        # Query the database for the LoaiXe with the given identifier
        loaixe = LoaiXe.query.filter_by(LoaiXe=loai_xe_name).first()

        # Check if the LoaiXe exists
        if not loaixe:
            return {"error": "LoaiXe not found"}, 404

        # Delete the LoaiXe from the database
        db.session.delete(loaixe)
        db.session.commit()
        return {"message": "LoaiXe deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400

# Delete all LoaiXe
def delete_all_loaixes_service():
    try:
        # Query the database for all LoaiXe
        loaixes = LoaiXe.query.all()

        # Check if there are any LoaiXe in the database
        if not loaixes:
            return {"message": "No LoaiXe found"}, 404

        # Delete all LoaiXe from the database
        for loaixe in loaixes:
            db.session.delete(loaixe)

        db.session.commit()
        return {"message": "All LoaiXe deleted successfully!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
