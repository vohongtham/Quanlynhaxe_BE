from app.database import db
from app.model import BaiXe
from app.app_ma import BaixeSchema  # Ensure you have imported BaixeSchema correctly
# from app.utils.utils import generate  # Assuming you have a utility function for generating unique IDs

# Initialize the schema for serialization
baixe_schema = BaixeSchema()
baixes_schema = BaixeSchema(many=True)

def add_baixe_service(request):
    try:
        # Lấy dữ liệu từ request
        data = request.get_json()
        print(data)  # In ra dữ liệu nhận được để debug

        # Lấy giá trị từ dữ liệu request
        Ma_BaiXe = data.get('Ma_BaiXe')
        Ma_DV = data.get('Ma_DV')
        Ten_BaiXe = data.get('Ten_BaiXe')
        So_ViTriTong = data.get('So_ViTriTong')
        
        # Kiểm tra các trường bắt buộc
        if not Ma_BaiXe or not Ma_DV or not Ten_BaiXe or So_ViTriTong is None:
            return {"error": "Thiếu thông tin bắt buộc: Ma_BaiXe, Ma_DV, Ten_BaiXe, và So_ViTriTong."}, 400
        
        # Kiểm tra So_ViTriTong có phải là số nguyên dương không
        if not isinstance(So_ViTriTong, int) or So_ViTriTong <= 0:
            return {"error": "So_ViTriTong phải là một số nguyên dương."}, 400

        # Kiểm tra xem Ma_BaiXe đã tồn tại trong cơ sở dữ liệu chưa
        existing_baixe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()
        if existing_baixe:
            return {"error": "Mã bãi xe đã tồn tại."}, 400

        # Tạo bản ghi BaiXe mới (So_ViTriDaDung sẽ tự động là 0 nhờ giá trị mặc định trong model)
        new_baixe = BaiXe(
            Ma_BaiXe=Ma_BaiXe,
            Ma_DV=Ma_DV,
            Ten_BaiXe=Ten_BaiXe,
            So_ViTriTong=So_ViTriTong
            # So_ViTriDaDung không cần phải truyền vì đã có giá trị mặc định là 0
        )
        
        # Thêm bản ghi mới vào cơ sở dữ liệu
        db.session.add(new_baixe)
        db.session.commit()

        # Trả về thông báo thành công
        return {"message": "Bãi xe đã được thêm thành công!"}, 201

    except Exception as e:
        # Rollback trong trường hợp có lỗi
        db.session.rollback()
        print(f"Đã xảy ra lỗi: {str(e)}")  # Log lại lỗi để debug
        return {"error": str(e)}, 500  # Trả về lỗi với mã trạng thái 500






# def get_baixe_by_criteria_service(Ma_BaiXe=None, Ma_DV=None, Ten_BaiXe=None, vi_tri_trong=None ):
#     """
#     Service function to retrieve Baixe records by ID_vitri, Vitri, Trangthai, or UserID.
#     Any combination of these criteria can be used for the search, supporting partial matches.
#     Returns the list of Baixe details in JSON format or an error message if no records are found.
#     """
#     try:
#         # Build the query based on the provided criteria
#         query = BaiXe.query

#         if Ma_BaiXe:
#             query = query.filter(BaiXe.Ma_BaiXe.ilike(f"%{Ma_BaiXe}%"))
#         if Ma_DV:
#             query = query.filter(BaiXe.Ma_DV.ilike(f"%{Ma_DV}%"))
#         if Ten_BaiXe:
#             query = query.filter(BaiXe.Ten_BaiXe.ilike(f"%{Ten_BaiXe}%"))
#         if vi_tri_trong:
#             query = query.filter(Baixe.vi_tri_trong.ilike(f"%{vi_tri_trong}%"))

#         # Execute the query to find the records
#         baixes = query.all()

#         # Check if any records were found
#         if not baixes:
#             return {"message": "No records found matching the criteria"}, 404

#         # Serialize the Baixe data
#         result = baixes_schema.dump(baixes)
#         return result, 200  # Return the serialized data and status code
#     except Exception as e:
#         return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong
def get_baixe_by_criteria_service(Ma_BaiXe=None, Ma_DV=None, Ten_BaiXe=None, vi_tri_trong=None):
    """
    Service function to retrieve BaiXe records by various criteria:
    - Ma_BaiXe: Partial match on the parking lot ID.
    - Ma_DV: Partial match on the DonVi ID (Unit ID).
    - Ten_BaiXe: Partial match on the name of the parking lot.
    - vi_tri_trong: Exact or greater match on available slots (empty parking spots).
    
    Returns a list of BaiXe records in JSON format or an error message if no records are found.
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
        if vi_tri_trong is not None:  # Ensure it's not None to avoid issues with 0 or empty values
            query = query.filter(BaiXe.So_ViTriTong - BaiXe.So_ViTriDaDung >= vi_tri_trong)

        # Execute the query to find matching BaiXe records
        baixes = query.all()

        # Check if any records were found
        if not baixes:
            return {"message": "No records found matching the criteria"}, 404

        # Serialize the BaiXe data
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
        # Lấy dữ liệu từ request
        data = request.get_json()
        Ma_DV = data.get('Ma_DV')
        Ten_BaiXe = data.get('Ten_BaiXe')
        So_ViTriDaDung = data.get('So_ViTriDaDung', 0)  # Mặc định là 0 nếu không có trong dữ liệu
        So_ViTriTong = data.get('So_ViTriTong')

        # Truy vấn bản ghi BaiXe dựa trên Ma_BaiXe
        baixe = BaiXe.query.filter_by(Ma_BaiXe=Ma_BaiXe).first()

        # Kiểm tra nếu bản ghi tồn tại
        if not baixe:
            return {"error": "BaiXe record not found."}, 404

        # Cập nhật các trường của BaiXe
        if Ma_DV is not None:
            baixe.Ma_DV = Ma_DV
        if Ten_BaiXe is not None:
            baixe.Ten_BaiXe = Ten_BaiXe
        if So_ViTriDaDung is not None:
            baixe.So_ViTriDaDung = So_ViTriDaDung
        if So_ViTriTong is not None:
            baixe.So_ViTriTong = So_ViTriTong

        # Commit thay đổi vào database
        db.session.commit()

        # Serialize dữ liệu BaiXe sau khi cập nhật
        result = baixe_schema.dump(baixe)
        return result, 200  # Trả về dữ liệu cập nhật và mã trạng thái 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Trả về thông báo lỗi và mã trạng thái 400 nếu có lỗi

    

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