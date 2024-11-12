
from app.database import db, bcrypt, mail

# # Mô hình Phân quyền
# class Phanquyen(db.Model):
#     __tablename__ = 'Phanquyen'

#     Ma_Quyen = db.Column(db.String(10), primary_key=True)
#     TenQuyen = db.Column(db.String(100), nullable=False)

# class Users(db.Model):
#     __tablename__ = 'Users'
    
#     Ma_user = db.Column(db.String(50), primary_key=True)
#     Ten_user = db.Column(db.String(100), nullable=False)
#     Email = db.Column(db.String(50), unique=True, nullable=False)
#     Password = db.Column(db.String(255), nullable=False)
#     GioiTinh = db.Column(db.String(50), nullable=False)
#     NgaySinh = db.Column(db.String(100), nullable=False)
#     Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)

#     def __init__(self, Ma_user, Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_Quyen):
#         self.Ma_user = Ma_user
#         self.Ten_user = Ten_user
#         self.Email = Email
#         self.Password = Password
#         self.GioiTinh = GioiTinh
#         self.NgaySinh = NgaySinh
#         self.Ma_Quyen = Ma_Quyen

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.Password, password)


# # Mô hình Sinhvien
# class Sinhvien(db.Model):
#     __tablename__ = 'Sinhvien'
    
#     Mssv = db.Column(db.String(20), primary_key=True)
#     Ten_SV = db.Column(db.String(100), nullable=False)
#     Ma_Lop = db.Column(db.String(50), db.ForeignKey('Lop.Ma_Lop'), nullable=False)
#     Email = db.Column(db.String(100), unique=True, nullable=False)
#     Password = db.Column(db.String(255), nullable=False)
#     NgaySinh = db.Column(db.Date, nullable=False)
#     GioiTinh = db.Column(db.String(50), nullable=False)
#     Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)
#     SDT = db.Column(db.String(20), nullable=False)  # Renamed from SĐT to SDT

#     # Define the one-to-many relationship with the Xe model
#     xe = db.relationship('Xe', backref='sinhvien', cascade="all, delete-orphan")
    
#     def __init__(self, Mssv, Ten_SV, Ma_Lop, Email, Password, NgaySinh, GioiTinh, Ma_Quyen, SDT=None):
#         self.Mssv = Mssv
#         self.Ten_SV = Ten_SV
#         self.Ma_Lop = Ma_Lop
#         self.Email = Email
#         self.Password = Password
#         self.NgaySinh = NgaySinh
#         self.GioiTinh = GioiTinh
#         self.Ma_Quyen = Ma_Quyen
#         self.SDT = SDT  # Renamed here as well
      
#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.Password, password)


# # Mô hình Xe
# class Xe(db.Model):
#     __tablename__ = 'Xe'
    
#     BienSoXe = db.Column(db.String(20), primary_key=True)
#     Mssv = db.Column(db.String(20), db.ForeignKey('Sinhvien.Mssv'), nullable=False)
#     SoKhungXe = db.Column(db.String(20), unique=True, nullable=False)
#     TenChuXe = db.Column(db.String(50), nullable=False)
#     LoaiXe = db.Column(db.String(50), nullable=False)
#     DungTich = db.Column(db.String(20), nullable=False)
#     NhanHieu = db.Column(db.String(100), nullable=False)
#     MauXe = db.Column(db.String(50), nullable=False)

#     # Thiết lập quan hệ với bảng ChiTietRaVao
#     # Specify the foreign_keys argument here
#     chitietravao = db.relationship(
#         'ChiTietRaVao',
#         backref='xe',
#         lazy=True,
#         cascade="all, delete-orphan",
#         foreign_keys='ChiTietRaVao.BienSoXe'  # Specify the foreign key
#     )

#     def __init__(self, BienSoXe, Mssv, SoKhungXe, TenChuXe=None, LoaiXe=None, DungTich=None, NhanHieu=None, MauXe=None):
#         self.BienSoXe = BienSoXe
#         self.Mssv = Mssv
#         self.SoKhungXe = SoKhungXe
#         self.TenChuXe = TenChuXe
#         self.LoaiXe = LoaiXe
#         self.DungTich = DungTich
#         self.NhanHieu = NhanHieu
#         self.MauXe = MauXe


# # Mô hình Lớp
# class Lop(db.Model):
#     __tablename__ = 'Lop'

#     Ma_Lop = db.Column(db.String(20), primary_key=True)
#     TenLop = db.Column(db.String(100), nullable=False)
#     Ma_Nganh = db.Column(db.String(20), db.ForeignKey('Nganh.Ma_Nganh'), nullable=False)

#     def __init__(self, Ma_Lop, TenLop, Ma_Nganh):
#         self.Ma_Lop = Ma_Lop
#         self.TenLop = TenLop
#         self.Ma_Nganh = Ma_Nganh


# # Mô hình Ngành
# class Nganh(db.Model):
#     __tablename__ = 'Nganh'

#     Ma_Nganh = db.Column(db.String(20), primary_key=True)
#     TenNganh = db.Column(db.String(100), nullable=False)
#     Ma_DV = db.Column(db.String(50), db.ForeignKey('DonVi.Ma_DV'), nullable=False)

#     def __init__(self, Ma_Nganh, TenNganh, Ma_DV):
#         self.Ma_Nganh = Ma_Nganh
#         self.TenNganh = TenNganh
#         self.Ma_DV = Ma_DV


# # Mô hình Đơn vị 
# class DonVi(db.Model):
#     __tablename__ = 'DonVi'

#     Ma_DV = db.Column(db.String(20), primary_key=True)
#     TenDV = db.Column(db.String(100), nullable=False)

#     def __init__(self, Ma_DV, TenDV):
#         self.Ma_DV = Ma_DV
#         self.TenDV = TenDV


# class BaiXe(db.Model):
#     __tablename__ = 'BaiXe'
    
#     Ma_BaiXe = db.Column(db.String(20), primary_key=True)
#     Ma_DV = db.Column(db.String(100), db.ForeignKey('DonVi.Ma_DV'), nullable=False)
#     Ten_BaiXe = db.Column(db.String(100), nullable=False)
#     So_ViTriDaDung = db.Column(db.Integer, nullable=False, default=0)  # Số vị trí đã được sử dụng
#     So_ViTriTong = db.Column(db.Integer, nullable=False)  # Tổng số vị trí

#     # user = db.relationship('Users', backref='baixe', cascade="all, delete-orphan")

#     def __init__(self, Ma_BaiXe, Ma_DV, Ten_BaiXe, So_ViTriTong, So_ViTriDaDung=0):
#         self.Ma_BaiXe = Ma_BaiXe
#         self.Ma_DV = Ma_DV
#         self.Ten_BaiXe = Ten_BaiXe
#         self.So_ViTriTong = So_ViTriTong
#         self.So_ViTriDaDung = So_ViTriDaDung


#     @property
#     def vi_tri_trong(self):
#         so_vi_tri_trong = self.So_ViTriTong - self.So_ViTriDaDung
#         return so_vi_tri_trong



# # Mô hình ChiTietRaVao
# class ChiTietRaVao(db.Model):
#     __tablename__ = 'ChiTietRaVao'
    
#     Ma_CT = db.Column(db.String(20), primary_key=True)
#     Mssv = db.Column(db.String(20), db.ForeignKey('Xe.Mssv'), nullable=False)
#     # BienSoXe = db.Column(db.String(20), nullable=False)
#     BienSoXe = db.Column(db.String(20), db.ForeignKey('Xe.BienSoXe'), nullable=False)
#     Ma_BaiXe = db.Column(db.String(20), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
#     TG_Vao = db.Column(db.DATETIME, nullable=False)
#     TG_Ra = db.Column(db.DATETIME, nullable=True)
#     Gia = db.Column(db.Float, nullable=False)

#     # Khai báo relationship
#     # xe = db.relationship('Xe', backref='chitietravao', lazy=True)

#     def __init__(self, Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, Gia, TG_Ra=None):
#         self.Ma_CT = Ma_CT
#         self.Mssv = Mssv
#         self.BienSoXe = BienSoXe
#         self.Ma_BaiXe = Ma_BaiXe
#         self.TG_Vao = TG_Vao
#         self.TG_Ra = TG_Ra
#         self.Gia = Gia




# from flask_mail import Mail, Message
# # from app.database import db, bcrypt
# # from datetime import datetime
# # from flask import current_app as app

# # # Initialize Flask-Mail (this should be in your app setup code)
# # mail = Mail(app)

# # Your model definitions...

# class ChiTietRaVao(db.Model):
#     __tablename__ = 'ChiTietRaVao'
    
#     Ma_CT = db.Column(db.String(20), primary_key=True)
#     Mssv = db.Column(db.String(20), db.ForeignKey('Xe.Mssv'), nullable=False)
#     BienSoXe = db.Column(db.String(20), db.ForeignKey('Xe.BienSoXe'), nullable=False)
#     Ma_BaiXe = db.Column(db.String(20), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
#     TG_Vao = db.Column(db.DATETIME, nullable=False)
#     TG_Ra = db.Column(db.DATETIME, nullable=True)
#     Gia = db.Column(db.Float, nullable=False)

#     def __init__(self, Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, Gia, TG_Ra=None):
#         self.Ma_CT = Ma_CT
#         self.Mssv = Mssv
#         self.BienSoXe = BienSoXe
#         self.Ma_BaiXe = Ma_BaiXe
#         self.TG_Vao = TG_Vao
#         self.TG_Ra = TG_Ra
#         self.Gia = Gia
    
#     def send_ma_ct_email(self):
#         # Retrieve the student's email based on Mssv
#         sinhvien = Sinhvien.query.filter_by(Mssv=self.Mssv).first()
#         if sinhvien and sinhvien.Email:
#             email = sinhvien.Email
#             msg = Message(
#                 subject="Mã thẻ xe của bạn",
#                 sender=app.config['MAIL_USERNAME'],
#                 recipients=[email]
#             )
#             msg.body = f"Chào {sinhvien.Ten_SV}, mã thẻ xe của bạn là: {self.Ma_CT}. Vui lòng sử dụng mã này khi ra vào bãi đỗ."
#             mail.send(msg)
#         else:
#             print("Email not found for Mssv:", self.Mssv)

# # Service function to add a vehicle entry and send Ma_CT
# def create_vehicle_entry(ma_ct, mssv, bien_so_xe, ma_bai_xe, gia):
#     entry = ChiTietRaVao(
#         Ma_CT=ma_ct,
#         Mssv=mssv,
#         BienSoXe=bien_so_xe,
#         Ma_BaiXe=ma_bai_xe,
#         TG_Vao=datetime.utcnow(),
#         Gia=gia
#     )
#     db.session.add(entry)
#     db.session.commit()
    
#     # Send the Ma_CT to student's email
#     entry.send_ma_ct_email()
#     return entry


from app.database import db, bcrypt, mail
from flask_mail import Mail, Message
from datetime import datetime
# from app.services.email_service import send_email
from sqlalchemy.orm import relationship

# Mô hình Phân quyền
class Phanquyen(db.Model):
    __tablename__ = 'Phanquyen'

    Ma_Quyen = db.Column(db.String(10), primary_key=True)
    TenQuyen = db.Column(db.String(100), nullable=False)

# Mô hình User
class Users(db.Model):
    __tablename__ = 'Users'
    
    Ma_user = db.Column(db.String(50), primary_key=True)
    Ten_user = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(50), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    GioiTinh = db.Column(db.String(50), nullable=False)
    NgaySinh = db.Column(db.String(100), nullable=False)
    Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)
    SDT = db.Column(db.String(20), nullable=False) 

    def __init__(self, Ma_user, Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_Quyen, SDT=None):
        self.Ma_user = Ma_user
        self.Ten_user = Ten_user
        self.Email = Email
        self.Password = Password
        self.GioiTinh = GioiTinh
        self.NgaySinh = NgaySinh
        self.Ma_Quyen = Ma_Quyen
        self.SDT = SDT  # Renamed here as well

    def check_password(self, password):
        return bcrypt.check_password_hash(self.Password, password)

# Mô hình Sinhvien
class Sinhvien(db.Model):
    __tablename__ = 'Sinhvien'
    
    Mssv = db.Column(db.String(20), primary_key=True)
    Ten_SV = db.Column(db.String(100), nullable=False)
    Ma_Lop = db.Column(db.String(50), db.ForeignKey('Lop.Ma_Lop'), nullable=False)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)
    NgaySinh = db.Column(db.Date, nullable=False)
    GioiTinh = db.Column(db.String(50), nullable=False)
    Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)
    SDT = db.Column(db.String(20), nullable=False)  # Renamed from SĐT to SDT

    # Define the one-to-many relationship with the Xe model
    xe = db.relationship('Xe', backref='sinhvien', cascade="all, delete-orphan")
    
    def __init__(self, Mssv, Ten_SV, Ma_Lop, Email, Password, NgaySinh, GioiTinh, Ma_Quyen, SDT=None):
        self.Mssv = Mssv
        self.Ten_SV = Ten_SV
        self.Ma_Lop = Ma_Lop
        self.Email = Email
        self.Password = Password
        self.NgaySinh = NgaySinh
        self.GioiTinh = GioiTinh
        self.Ma_Quyen = Ma_Quyen
        self.SDT = SDT  # Renamed here as well
      
    def check_password(self, password):
        return bcrypt.check_password_hash(self.Password, password)


# Mô hình Lớp
class Lop(db.Model):
    __tablename__ = 'Lop'

    Ma_Lop = db.Column(db.String(20), primary_key=True)
    TenLop = db.Column(db.String(100), nullable=False)
    Ma_Nganh = db.Column(db.String(20), db.ForeignKey('Nganh.Ma_Nganh'), nullable=False)

    def __init__(self, Ma_Lop, TenLop, Ma_Nganh):
        self.Ma_Lop = Ma_Lop
        self.TenLop = TenLop
        self.Ma_Nganh = Ma_Nganh

# Mô hình Ngành
class Nganh(db.Model):
    __tablename__ = 'Nganh'

    Ma_Nganh = db.Column(db.String(20), primary_key=True)
    TenNganh = db.Column(db.String(100), nullable=False)
    Ma_DV = db.Column(db.String(50), db.ForeignKey('DonVi.Ma_DV'), nullable=False)

    def __init__(self, Ma_Nganh, TenNganh, Ma_DV):
        self.Ma_Nganh = Ma_Nganh
        self.TenNganh = TenNganh
        self.Ma_DV = Ma_DV

# Mô hình Đơn vị 
class DonVi(db.Model):
    __tablename__ = 'DonVi'

    Ma_DV = db.Column(db.String(20), primary_key=True)
    TenDV = db.Column(db.String(100), nullable=False)

    def __init__(self, Ma_DV, TenDV):
        self.Ma_DV = Ma_DV
        self.TenDV = TenDV

# Mô hình Bãi đỗ
class BaiXe(db.Model):
    __tablename__ = 'BaiXe'
    
    Ma_BaiXe = db.Column(db.String(20), primary_key=True)
    Ma_DV = db.Column(db.String(100), db.ForeignKey('DonVi.Ma_DV'), nullable=False)
    Ten_BaiXe = db.Column(db.String(100), nullable=False)
    So_ViTriDaDung = db.Column(db.Integer, nullable=False, default=0)  # Số vị trí đã được sử dụng
    So_ViTriTong = db.Column(db.Integer, nullable=False)  # Tổng số vị trí

    def __init__(self, Ma_BaiXe, Ma_DV, Ten_BaiXe, So_ViTriTong, So_ViTriDaDung=0):
        self.Ma_BaiXe = Ma_BaiXe
        self.Ma_DV = Ma_DV
        self.Ten_BaiXe = Ten_BaiXe
        self.So_ViTriTong = So_ViTriTong
        self.So_ViTriDaDung = So_ViTriDaDung

    @property
    def vi_tri_trong(self):
        return self.So_ViTriTong - self.So_ViTriDaDung

# Mô hình Xe
class Xe(db.Model):
    __tablename__ = 'Xe'
    
    BienSoXe = db.Column(db.String(20), primary_key=True)
    Mssv = db.Column(db.String(20), db.ForeignKey('Sinhvien.Mssv'), nullable=False)
    SoKhungXe = db.Column(db.String(20), unique=True, nullable=False)
    TenChuXe = db.Column(db.String(50), nullable=False)
    # LoaiXe = db.Column(db.String(50), nullable=False)
    LoaiXe = db.Column(db.String(50), db.ForeignKey('LoaiXe.LoaiXe'), nullable=False)
    DungTich = db.Column(db.String(20), nullable=False)
    NhanHieu = db.Column(db.String(100), nullable=False)
    MauXe = db.Column(db.String(50), nullable=False)

    # Thiết lập quan hệ với bảng ChiTietRaVao
    chitietravao = db.relationship(
        'ChiTietRaVao',
        backref='xe',
        lazy=True,
        cascade="all, delete-orphan",
        foreign_keys='ChiTietRaVao.BienSoXe'
    )

    def __init__(self, BienSoXe, Mssv, SoKhungXe, TenChuXe=None, LoaiXe=None, DungTich=None, NhanHieu=None, MauXe=None):
        self.BienSoXe = BienSoXe
        self.Mssv = Mssv
        self.SoKhungXe = SoKhungXe
        self.TenChuXe = TenChuXe
        self.LoaiXe = LoaiXe
        self.DungTich = DungTich
        self.NhanHieu = NhanHieu
        self.MauXe = MauXe
        
# Mô hình Chi tiết ra vào
class ChiTietRaVao(db.Model):
    __tablename__ = 'ChiTietRaVao'
    
    Ma_CT = db.Column(db.String(20), primary_key=True)
    Mssv = db.Column(db.String(20), db.ForeignKey('Xe.Mssv'), nullable=False)
    BienSoXe = db.Column(db.String(20), db.ForeignKey('Xe.BienSoXe'), nullable=False)
    Ma_BaiXe = db.Column(db.String(20), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
    TG_Vao = db.Column(db.DateTime, nullable=False)
    TG_Ra = db.Column(db.DateTime, nullable=True)
    Gia = db.Column(db.Float, nullable=False)
    AnhBienSo = db.Column(db.Text, nullable=True)  # Cột mới để lưu ảnh biển số xe
    LoaiXe = db.Column(db.String(50), db.ForeignKey('LoaiXe.LoaiXe'), nullable=False)  # Liên kết với bảng LoaiXe

    # Tạo quan hệ với LoaiXe để lấy thông tin giá tiền
    loai_xe = relationship('LoaiXe', backref='chitietravao', lazy=True)

    def __init__(self, Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, LoaiXe, Gia, AnhBienSo=None , TG_Ra=None):
        self.Ma_CT = Ma_CT
        self.Mssv = Mssv
        self.BienSoXe = BienSoXe
        self.Ma_BaiXe = Ma_BaiXe
        self.TG_Vao = TG_Vao
        self.TG_Ra = TG_Ra
        self.Gia = Gia
        self.AnhBienSo = AnhBienSo  # Khởi tạo cột AnhBienSo
        self.LoaiXe = LoaiXe

    def send_ma_ct_email(self, recipient_email):
        """
        Gửi mã xác nhận (Ma_CT) qua email cho sinh viên.

        :param recipient_email: Địa chỉ email của sinh viên
        """
        send_email(recipient_email, self.Ma_CT)

class LoaiXe(db.Model):
    __tablename__ = 'LoaiXe'
    
    LoaiXe = db.Column(db.String(50), primary_key=True)  # Dùng LoaiXe làm khóa chính
    Gia = db.Column(db.Float, nullable=False)  # Giá tiền tương ứng với loại xe

    def __init__(self, LoaiXe, Gia):
        self.LoaiXe = LoaiXe
        self.Gia = Gia
