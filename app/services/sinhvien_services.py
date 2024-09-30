from app.database import db
from app.app_ma import SinhvienSchema
from app.model import Sinhvien
from flask import request, json
from sqlalchemy import func
from flask_bcrypt import Bcrypt
# import bcrypt

# Initialize bcrypt
bcrypt = Bcrypt()

sinhvien_schema = SinhvienSchema()
sinhviens_schema = SinhvienSchema(many=True)

# Add sinh viên
def add_sv_service(request):
    try:
        # Retrieve data from the request
        data = request.get_json()
        Mssv = data.get('Mssv')
        Ten_SV = data.get('Ten_SV')
        Ma_Lop = data.get('Ma_Lop')
        Email = data.get('Email')
        Password = data.get('Password')
        NgaySinh = data.get('NgaySinh')
        GioiTinh = data.get('GioiTinh')
        SDT = data.get('SDT')

        # Check if the email is already in use
        existing_student = Sinhvien.query.filter_by(Email=Email).first()
        if existing_student:
            return {"error": "Email đã được sử dụng"}, 400

        # Hash the password using bcrypt
        hashed_password = bcrypt.generate_password_hash(Password).decode('utf-8')

        print("Hashed Password:", hashed_password)

        # Create a new Sinhvien instance with the hashed password
        new_sinhvien = Sinhvien(
            Mssv=Mssv,
            Ten_SV=Ten_SV,
            Ma_Lop=Ma_Lop,
            Email=Email,
            Password=hashed_password,
            NgaySinh=NgaySinh,
            GioiTinh=GioiTinh,
            Ma_Quyen='MQSV',  # Default student role
            SDT=SDT
        )
        
        # Add the new student to the database
        db.session.add(new_sinhvien)
        db.session.commit()

        return {"message": "Add success!"}, 201  # Return a success message and status code

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code


#Get thong tin sinh vien 
def get_sv_by_criteria_service(Mssv=None, Ten_SV=None, Ma_Lop=None, Email=None, NgaySinh=None, GioiTinh=None, SDT=None):
    """
    Service function to retrieve students by their Mssv, name, email, or phone number.
    Any combination of these criteria can be used for the search, supporting partial matches.
    Returns the list of students' details in JSON format or an error message if no students are found.
    """
    try:
        # Build the query based on the provided criteria
        query = Sinhvien.query

        if Mssv:
            query = query.filter_by(Mssv=Mssv)
        if Ten_SV:
            query = query.filter(Sinhvien.Ten_SV.ilike(f"%{Ten_SV}%"))
        if Email:
            query = query.filter_by(Email=Email)
        if NgaySinh:
            query = query.filter(Sinhvien.NgaySinh.ilike(f"%{NgaySinh}%"))
        if GioiTinh: 
            query = query.filter(Sinhvien.GioiTinh.ilike(f"%{GioiTinh}%"))
        if SDT:
            query = query.filter(Sinhvien.SDT.ilike(f"%{SDT}"))

        # Execute the query to find the students
        sinhviens = query.all()

        # Check if any students were found
        if not sinhviens:
            return {"message": "No students found matching the criteria"}, 404

        # Serialize the student data
        result = sinhviens_schema.dump(sinhviens)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong

# Get tat ca sinh vien
def get_all_svs_service():
    try:
        # Query the database for all students
        sinhviens = Sinhvien.query.all()

        # Serialize the list of students
        result = sinhviens_schema.dump(sinhviens)
        return result, 200  # Return the serialized data and status code
    except Exception as e:
        return {"error": str(e)}, 400  # Return an error message and status code

# Update sinh vien
# def update_sv_service(Mssv, request):
#     try:
#         sinhvien = Sinhvien.query.filter_by(Mssv=Mssv).first()

#         if not sinhvien:
#             return {"error": "Student not found"}, 404

#         data = request.get_json()
#         sinhvien.Ten_SV = data.get('Ten_SV', sinhvien.Ten_SV)
#         sinhvien.Ma_Lop = data.get('Ma_Lop', sinhvien.Ma_Lop)
#         sinhvien.Email = data.get('Email', sinhvien.Email)
#         if 'Password' in data:
#             # Hash the new password using bcrypt
#             sinhvien.Password = bcrypt.generate_password_hash(data['Password']).decode('utf-8')
#         sinhvien.NgaySinh = data.get('NgaySinh', sinhvien.NgaySinh)
#         sinhvien.GioiTinh = data.get('GioiTinh', sinhvien.GioiTinh)
#         sinhvien.SDT = data.get('SDT', sinhvien.SDT)

#         db.session.commit()
#         return {"message": "Update success!"}, 200
#     except Exception as e:
#         db.session.rollback()
#         return {"error": str(e)}, 400

    
# Delete 1 sinh vien 
def delete_sv_service(Mssv):
    """
    Service function to delete an existing student.
    Expects the Mssv of the student to delete.
    Returns a success message or an error message if the student is not found.
    """
    try:
        # Query the database for the student with the given Mssv
        sinhvien = Sinhvien.query.filter_by(Mssv=Mssv).first()

        # Check if the student exists
        if not sinhvien:
            return {"error": "Student not found"}, 404

        # Delete the student from the database
        db.session.delete(sinhvien)
        db.session.commit()
        return {"message": "Delete success!"}, 200  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong

# Delete all sinh viên
def delete_all_svs_service():
    """
    Service function to delete all students from the database.
    Returns a success message or an error message if something goes wrong.
    """
    try:
        # Query the database for all students
        sinhviens = Sinhvien.query.all()

        # Check if there are any students in the database
        if not sinhviens:
            return {"message": "No students found"}, 404

        # Delete all students from the database
        for sinhvien in sinhviens:
            db.session.delete(sinhvien)
        
        db.session.commit()
        return {"message": "All students deleted successfully!"}, 200  # Return a success message and status code
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400  # Return an error message and status code if something goes wrong



def update_sv_service(Mssv, request):
    try:
        sinhvien = Sinhvien.query.filter_by(Mssv=Mssv).first()

        if not sinhvien:
            return {"error": "Student not found"}, 404

        data = request.get_json()
        
        # Kiểm tra mật khẩu hiện tại
        if 'currentPassword' in data:
            if not bcrypt.check_password_hash(sinhvien.Password, data['currentPassword']):
                return {"error": "Mật khẩu hiện tại không đúng"}, 401
        
        # Cập nhật thông tin sinh viên
        sinhvien.Ten_SV = data.get('Ten_SV', sinhvien.Ten_SV)
        sinhvien.Ma_Lop = data.get('Ma_Lop', sinhvien.Ma_Lop)
        sinhvien.Email = data.get('Email', sinhvien.Email)
        
        if 'Password' in data:
            sinhvien.Password = bcrypt.generate_password_hash(data['Password']).decode('utf-8')
        
        sinhvien.NgaySinh = data.get('NgaySinh', sinhvien.NgaySinh)
        sinhvien.GioiTinh = data.get('GioiTinh', sinhvien.GioiTinh)
        sinhvien.SDT = data.get('SDT', sinhvien.SDT)

        db.session.commit()
        return {"message": "Cập nhật thành công!"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400
