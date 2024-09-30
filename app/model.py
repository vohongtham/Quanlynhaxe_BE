# from app.database import db, bcrypt

# # Mô hình Phân quyền
# class Phanquyen(db.Model):
#     __tablename__ = 'Phanquyen'

#     Ma_Quyen = db.Column(db.String(10), primary_key=True)
#     TenQuyen = db.Column(db.String(100), nullable=False)

# # # Mô hình User

# from app.database import db, bcrypt

# # Mô hình User
# class Users(db.Model):
#     __tablename__ = 'Users'
    
#     Ma_user = db.Column(db.String(50), primary_key=True)
#     Ten_user = db.Column(db.String(100), nullable=False)
#     Email = db.Column(db.String(50), unique=True, nullable=False)
#     Password = db.Column(db.String(255), nullable=False)
#     GioiTinh = db.Column(db.String(50), nullable=False)
#     NgaySinh = db.Column(db.String(100), nullable=False)
#     Ma_BaiXe = db.Column(db.String(50), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
#     Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)

#     def __init__(self, Ma_user, Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_BaiXe, Ma_Quyen):
#         self.Ma_user = Ma_user
#         self.Ten_user = Ten_user
#         self.Email = Email
#         self.Password = Password
#         self.GioiTinh = GioiTinh
#         self.NgaySinh = NgaySinh
#         self.Ma_BaiXe = Ma_BaiXe
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
#     SDT = db.Column(db.String(20))  # Renamed from SĐT to SDT

#     # Define the one-to-many relationship with the Xe model
#     xe = db.relationship('Xe', backref='sinhvien', cascade="all, delete-orphan")
    
#     def __init__(self, Mssv, Ten_SV, Ma_Lop, Email, Password, NgaySinh, GioiTinh, Ma_Quyen, SDT=None):
#         self.Mssv = Mssv
#         self.Ten_SV = Ten_SV
#         self.Ma_Lop = Ma_Lop
#         self.Email = Email
#         self.Password = Password  # Mã hóa mật khẩu
#         self.NgaySinh = NgaySinh
#         self.GioiTinh = GioiTinh
#         self.Ma_Quyen = Ma_Quyen
#         self.SDT = SDT  # Renamed here as well
      
#     def check_password(self, password):
#         return bcrypt.check_password_hash(self.Password, password)

# # Mô hình Xe
# # class Xe(db.Model):
# #     __tablename__ = 'Xe'
    
# #     BienSoXe = db.Column(db.String(20), primary_key=True)
# #     Mssv = db.Column(db.String(20), db.ForeignKey('Sinhvien.Mssv'), nullable=False)
# #     SoKhungXe = db.Column(db.String(20), unique=True, nullable=False)
# #     TenChuXe = db.Column(db.String(50))
# #     LoaiXe = db.Column(db.String(50))
# #     DungTich = db.Column(db.String(20)) 
# #     NhanHieu = db.Column(db.String(100))
# #     MauXe = db.Column(db.String(50))

# #     def __init__(self, BienSoXe, Mssv, SoKhungXe, TenChuXe=None, LoaiXe=None, DungTich=None, NhanHieu=None, MauXe=None):
# #         self.BienSoXe = BienSoXe
# #         self.Mssv = Mssv
# #         self.SoKhungXe = SoKhungXe
# #         self.TenChuXe = TenChuXe
# #         self.LoaiXe = LoaiXe
# #         self.DungTich = DungTich
# #         self.NhanHieu = NhanHieu
# #         self.MauXe = MauXe

# class Xe(db.Model):
#     __tablename__ = 'Xe'
    
#     BienSoXe = db.Column(db.String(20), primary_key=True)
#     Mssv = db.Column(db.String(20), db.ForeignKey('Sinhvien.Mssv'), nullable=False)
#     SoKhungXe = db.Column(db.String(20), unique=True, nullable=False)
#     TenChuXe = db.Column(db.String(50))
#     LoaiXe = db.Column(db.String(50))
#     DungTich = db.Column(db.String(20))
#     NhanHieu = db.Column(db.String(100))
#     MauXe = db.Column(db.String(50))

#     # Thiết lập quan hệ với bảng ChiTietRaVao
#     # chitietravao = db.relationship('ChiTietRaVao', backref='xe', cascade="all, delete-orphan")
#     # Quan hệ với bảng ChiTietRaVao
#     chitietravao = db.relationship('ChiTietRaVao', backref='xe', lazy=True, 
#                                     foreign_keys='ChiTietRaVao.BienSoXe')

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


# # Mô hình Baixe
# class BaiXe(db.Model):
#     __tablename__ = 'BaiXe'
    
#     Ma_BaiXe = db.Column(db.String(20), primary_key=True)
#     Ma_DV = db.Column(db.String(100), db.ForeignKey('DonVi.Ma_DV'), nullable=False)
#     Ten_BaiXe = db.Column(db.String(100), nullable=False)

#     def __init__(self, Ma_BaiXe, Ma_DV, Ten_BaiXe):
#         self.Ma_BaiXe = Ma_BaiXe
#         self.Ma_DV = Ma_DV
#         self.Ten_BaiXe = Ten_BaiXe

# # Mô hình ChiTietRaVao
# # class ChiTietRaVao(db.Model):
# #     __tablename__ = 'ChiTietRaVao'
    
# #     Ma_CT = db.Column(db.String(20), primary_key=True)
# #     Mssv = db.Column(db.String(20), db.ForeignKey('Xe.Mssv'), nullable=False)
# #     BienSoXe = db.Column(db.String(20), db.ForeignKey('Xe.BienSoXe'), nullable=False)
# #     Ma_BaiXe = db.Column(db.String(20), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
# #     TG_Vao = db.Column(db.DATETIME, nullable=False)
# #     TG_Ra = db.Column(db.DATETIME, nullable=True)
# #     Gia = db.Column(db.Float, nullable=False)

# #     def __init__(self, Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, Gia, TG_Ra=None):
# #         self.Ma_CT = Ma_CT
# #         self.Mssv = Mssv
# #         self.BienSoXe = BienSoXe
# #         self.Ma_BaiXe = Ma_BaiXe
# #         self.TG_Vao = TG_Vao
# #         self.TG_Ra = TG_Ra
# #         self.Gia = Gia



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


from app.database import db, bcrypt

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
    Ma_BaiXe = db.Column(db.String(50), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
    Ma_Quyen = db.Column(db.String(50), db.ForeignKey('Phanquyen.Ma_Quyen'), nullable=False)

    def __init__(self, Ma_user, Ten_user, Email, Password, GioiTinh, NgaySinh, Ma_BaiXe, Ma_Quyen):
        self.Ma_user = Ma_user
        self.Ten_user = Ten_user
        self.Email = Email
        self.Password = Password
        self.GioiTinh = GioiTinh
        self.NgaySinh = NgaySinh
        self.Ma_BaiXe = Ma_BaiXe
        self.Ma_Quyen = Ma_Quyen

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
    SDT = db.Column(db.String(20))  # Renamed from SĐT to SDT

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


# Mô hình Xe
class Xe(db.Model):
    __tablename__ = 'Xe'
    
    BienSoXe = db.Column(db.String(20), primary_key=True)
    Mssv = db.Column(db.String(20), db.ForeignKey('Sinhvien.Mssv'), nullable=False)
    SoKhungXe = db.Column(db.String(20), unique=True, nullable=False)
    TenChuXe = db.Column(db.String(50))
    LoaiXe = db.Column(db.String(50))
    DungTich = db.Column(db.String(20))
    NhanHieu = db.Column(db.String(100))
    MauXe = db.Column(db.String(50))

    # Thiết lập quan hệ với bảng ChiTietRaVao
    # Specify the foreign_keys argument here
    chitietravao = db.relationship(
        'ChiTietRaVao',
        backref='xe',
        lazy=True,
        cascade="all, delete-orphan",
        foreign_keys='ChiTietRaVao.BienSoXe'  # Specify the foreign key
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


# Mô hình Baixe
class BaiXe(db.Model):
    __tablename__ = 'BaiXe'
    
    Ma_BaiXe = db.Column(db.String(20), primary_key=True)
    Ma_DV = db.Column(db.String(100), db.ForeignKey('DonVi.Ma_DV'), nullable=False)
    Ten_BaiXe = db.Column(db.String(100), nullable=False)

    def __init__(self, Ma_BaiXe, Ma_DV, Ten_BaiXe):
        self.Ma_BaiXe = Ma_BaiXe
        self.Ma_DV = Ma_DV
        self.Ten_BaiXe = Ten_BaiXe


# Mô hình ChiTietRaVao
class ChiTietRaVao(db.Model):
    __tablename__ = 'ChiTietRaVao'
    
    Ma_CT = db.Column(db.String(20), primary_key=True)
    Mssv = db.Column(db.String(20), db.ForeignKey('Xe.Mssv'), nullable=False)
    BienSoXe = db.Column(db.String(20), db.ForeignKey('Xe.BienSoXe'), nullable=False)
    Ma_BaiXe = db.Column(db.String(20), db.ForeignKey('BaiXe.Ma_BaiXe'), nullable=False)
    TG_Vao = db.Column(db.DATETIME, nullable=False)
    TG_Ra = db.Column(db.DATETIME, nullable=True)
    Gia = db.Column(db.Float, nullable=False)

    # Khai báo relationship
    # xe = db.relationship('Xe', backref='chitietravao', lazy=True)

    def __init__(self, Ma_CT, Mssv, BienSoXe, Ma_BaiXe, TG_Vao, Gia, TG_Ra=None):
        self.Ma_CT = Ma_CT
        self.Mssv = Mssv
        self.BienSoXe = BienSoXe
        self.Ma_BaiXe = Ma_BaiXe
        self.TG_Vao = TG_Vao
        self.TG_Ra = TG_Ra
        self.Gia = Gia
