from app.database import db
from app.app_ma import DonViSchema
from app.model import DonVi
from flask import request, json

donvi_schema = DonViSchema()
donvis_schema = DonViSchema(many=True)

# Add DonVi
def add_dv_service(request):
    try:
        # Retrieve data from the request
        data = request.get_json()
        Ma_DV = data.get('Ma_DV')
        TenDV = data.get('TenDV')

        # Create a new DonVi instance
        new_donvi = DonVi(Ma_DV=Ma_DV, TenDV=TenDV)

        # Add the new DonVi to the database
        db.session.add(new_donvi)
        db.session.commit()
        return {"message": "DonVi added successfully!"}, 201  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code

# Get DonVi by criteria
def get_dv_by_criteria_service(Ma_DV=None, TenDV=None):
    """
    Service function to retrieve DonVi by their Ma_DV or TenDV.
    Any combination of these criteria can be used for the search, supporting partial matches.
    Returns the list of DonVi details in JSON format or an error message if no DonVi is found.
    """
    try:
        # Build the query based on the provided criteria
        query = DonVi.query

        if Ma_DV:
            query = query.filter_by(Ma_DV=Ma_DV)
        if TenDV:
            query = query.filter(DonVi.TenDV.ilike(f"%{TenDV}%"))

        # Execute the query to find the DonVi
        donvis = query.all()

        # Check if any DonVi were found
        if not donvis:
            return {"message": "No DonVi found matching the criteria"}, 404

        # Serialize the DonVi data
        result = donvis_schema.dump(donvis)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong

# Get all DonVi
def get_all_dvs_service():
    try:
        # Query the database for all DonVi
        donvis = DonVi.query.all()

        # Serialize the list of DonVi
        result = donvis_schema.dump(donvis)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code

# Update DonVi
def update_dv_service(Ma_DV, request):
    """
    Service function to update an existing DonVi's details.
    Expects the Ma_DV of the DonVi to update and JSON data in the request body.
    Returns a success message or an error message if the DonVi is not found.
    """
    try:
        # Query the database for the DonVi with the given Ma_DV
        donvi = DonVi.query.filter_by(Ma_DV=Ma_DV).first()

        # Check if the DonVi exists
        if not donvi:
            return {"error": "DonVi not found"}, 404

        # Retrieve data from the request and update the DonVi's details
        data = request.get_json()
        donvi.TenDV = data.get('TenDV', donvi.TenDV)

        # Commit the changes to the database
        db.session.commit()
        return {"message": "DonVi updated successfully!"}, 200  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong

# Delete DonVi
def delete_dv_service(Ma_DV):
    """
    Service function to delete an existing DonVi.
    Expects the Ma_DV of the DonVi to delete.
    Returns a success message or an error message if the DonVi is not found.
    """
    try:
        # Query the database for the DonVi with the given Ma_DV
        donvi = DonVi.query.filter_by(Ma_DV=Ma_DV).first()

        # Check if the DonVi exists
        if not donvi:
            return {"error": "DonVi not found"}, 404

        # Delete the DonVi from the database
        db.session.delete(donvi)
        db.session.commit()
        return {"message": "DonVi deleted successfully!"}, 200  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong

# Delete all DonVi
def delete_all_dvs_service():
    """
    Service function to delete all DonVi from the database.
    Returns a success message or an error message if something goes wrong.
    """
    try:
        # Query the database for all DonVi
        donvis = DonVi.query.all()

        # Check if there are any DonVi in the database
        if not donvis:
            return {"message": "No DonVi found"}, 404

        # Delete all DonVi from the database
        for donvi in donvis:
            db.session.delete(donvi)

        db.session.commit()
        return {"message": "All DonVi deleted successfully!"}, 200  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong
