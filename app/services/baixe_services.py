from app.database import db
from app.model import BaiXe
from app.app_ma import BaixeSchema  # Ensure you have imported BaixeSchema correctly
from app.utils.utils import generate  # Assuming you have a utility function for generating unique IDs

# Initialize the schema for serialization
baixe_schema = BaixeSchema()
baixes_schema = BaixeSchema(many=True)

def add_baixe_service(request):
    try:
        data = request.get_json()
        print(data)  # Log the received data
        Ma_BaiXe = data.get('Ma_BaiXe')
        Ma_DV = data.get('Ma_DV')
        Ten_BaiXe = data.get('Ten_BaiXe')

        # Validate required fields
        if not Ma_DV or not Ten_BaiXe:
            return {"error": "Missing required fields: ID_vitri, Vitri, and Trangthai are required."}, 400

        # # Generate a unique ID_vitri if not provided
        # if not Ma_BaiXe:
        #     Ma_BaiXe = generate()

        #     # Ensure ID_vitri is unique
        #     while BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first():
        #         Ma_BaiXe = generate()  # Regenerate if collision occurs

        # Check if the ID_vitri already exists
        existing_baixe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()
        if existing_baixe:
            return {"error": "Baixe ID already exists."}, 400

        # Create and add the new Baixe record
        new_baixe = BaiXe(Ma_BaiXe=Ma_BaiXe, Ma_DV=Ma_DV, Ten_BaiXe=Ten_BaiXe)
        db.session.add(new_baixe)
        db.session.commit()

        return {"message": "Added successfully!"}, 201

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400



def get_baixe_by_criteria_service(Ma_BaiXe=None, Ma_DV=None, Ten_BaiXe=None):
    """
    Service function to retrieve Baixe records by ID_vitri, Vitri, Trangthai, or UserID.
    Any combination of these criteria can be used for the search, supporting partial matches.
    Returns the list of Baixe details in JSON format or an error message if no records are found.
    """
    try:
        # Build the query based on the provided criteria
        query = BaiXe.query

        if Ma_BaiXe:
            query = query.filter(BaiXe.Ma_BaiXe.ilike(f"%{Ma_BaiXe}%"))
        if Ma_DV:
            query = query.filter(BaiXe.Ma_DV.ilike(f"%{Ma_DV}%"))
        if Ten_BaiXe:
            query = query.filter(BaiXe.Ten_BaiXe.ilike(f"%{Ten_BaiXe}%"))
        # if UserID:
        #     query = query.filter(Baixe.UserID.ilike(f"%{UserID}%"))

        # Execute the query to find the records
        baixes = query.all()

        # Check if any records were found
        if not baixes:
            return {"message": "No records found matching the criteria"}, 404

        # Serialize the Baixe data
        result = baixes_schema.dump(baixes)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong


def get_all_baixes_service():
    """
    Service function to retrieve all Baixe records from the database.
    Returns the list of Baixe details in JSON format or an error message if something goes wrong.
    """
    try:
        # Query the database for all Baixe records
        baixes = BaiXe.query.all()

        # Check if any records were found
        if not baixes:
            return {"message": "No records found"}, 404

        # Serialize the Baixe data
        result = baixes_schema.dump(baixes)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong
    

def update_baixe_service(Ma_BaiXe, request):

    try:
        # Get the data from the request
        data = request.get_json()
        Ma_DV = data.get('Ma_DV')
        Ten_BaiXe = data.get('Ten_BaiXe')

        # Query the database for the Baixe record with the given ID_vitri
        baixe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()

        # Check if the record exists
        if not baixe:
            return {"error": "Baixe record not found."}, 404

        # Update the fields
        if Ma_DV is not None:
            baixe.Ma_DV = Ma_DV
        if Ten_BaiXe is not None:
            baixe.Ten_BaiXe = Ten_BaiXe

        # Commit the changes to the database
        db.session.commit()

        # Serialize the updated Baixe data
        result = baixe_schema.dump(baixe)
        return result, 200  # Return the updated record and status code

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong
    

def delete_baixe_service(Ma_BaiXe):
    """
    Service function to delete an existing Baixe record.
    Expects the ID_vitri of the Baixe record to delete.
    Returns a success message or an error message if the record is not found.
    """
    try:
        # Query the database for the Baixe record with the given ID_vitri
        baixe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()

        # Check if the record exists
        if not baixe:
            return {"error": "Bai xe record not found."}, 404

        # Delete the record from the database
        db.session.delete(baixe)
        db.session.commit()

        return {"message": "Bai xe deleted successfully!"}, 200  # Return a success message and status code

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong
    

def delete_all_baixes_service():
    """
    Service function to delete all Baixe records from the database.
    Returns a success message or an error message if something goes wrong.
    """
    try:
        # Query the database for all Baixe records
        baixes = BaiXe.query.all()

        # Check if there are any records to delete
        if not baixes:
            return {"message": "No Baixe records found."}, 404

        # Delete all Baixe records from the database
        for baixe in baixes:
            db.session.delete(baixe)
        
        db.session.commit()
        return {"message": "All Baixe records deleted successfully!"}, 200  # Return a success message and status code

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong