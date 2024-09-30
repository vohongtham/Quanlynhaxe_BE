from .database import ma

# class UsersSchema(ma.Schema):
#     class Meta:
#         fields = ('UserID', 'Username', 'Password', 'ChucVu')

# # class SinhvienSchema(ma.Schema):
# #     class Meta:
# #         fields = ('Mssv', 'Ten', 'Email', 'Phone', 'Khoa')

# class XeSchema(ma.Schema):
#     class Meta:
#         fields = ('ID_xe', 'Mssv', 'Biensoxe', 'Tenxe', 'Loaixe')

# class BaixeSchema(ma.Schema):
#     class Meta:
#         fields = ('ID_vitri', 'Vitri', 'Trangthai', 'UserID')

# class LichsuSchema(ma.Schema):
#     class Meta:
#         fields = ('RecordID', 'Mssv', 'ID_xe', 'ID_vitri', 'TG_vao', 'TG_ra', 'UserID')

from marshmallow import Schema, fields

class PhanquyenSchema(Schema):
    Ma_Quyen = fields.Str(required=True)
    TenQuyen = fields.Str(required=True)

class UsersSchema(Schema):
    Ma_user = fields.Str(required=True)
    Ten_user = fields.Str(required=True)
    Email = fields.Email(required=True)
    Password = fields.Str(required=True, load_only=True)
    GioiTinh = fields.Str(required=True)
    NgaySinh = fields.Str(required=True)
    Ma_BaiXe = fields.Str(required=True)  # Mã bãi xe mà người dùng quản lý hoặc liên quan
    Ma_Quyen = fields.Str(required=True)


# Schema for Sinhvien
class SinhvienSchema(Schema):
    Mssv = fields.Str(required=True)
    Ten_SV = fields.Str(required=True)
    Ma_Lop = fields.Str(required=True)  # Added field for Ma_Lop
    Email = fields.Email(required=True)
    Password = fields.Str(required=True, load_only=True)
    NgaySinh = fields.Date(required=True)
    GioiTinh = fields.Str(required=True)
    Ma_Quyen = fields.Str(required=True)
    SDT = fields.Str(allow_none=True)
    

# Schema for Lop
class LopSchema(Schema):
    Ma_Lop = fields.Str(required=True)
    TenLop = fields.Str(required=True)
    Ma_Nganh = fields.Str(required=True)

# Schema for Nganh
class NganhSchema(Schema):
    Ma_Nganh = fields.Str(required=True)
    TenNganh = fields.Str(required=True)
    Ma_DV = fields.Str(required=True)

# Schema for DonVi
class DonViSchema(Schema):
    Ma_DV = fields.Str(required=True)
    TenDV = fields.Str(required=True)

# Schema for Xe
class XeSchema(Schema):
    BienSoXe = fields.Str(required=True)
    Mssv = fields.Str(required=True)
    SoKhungXe = fields.Str(required=True)
    TenChuXe = fields.Str(allow_none=True)
    LoaiXe = fields.Str(allow_none=True)
    DungTich = fields.Str(allow_none=True)
    NhanHieu = fields.Str(allow_none=True)
    MauXe = fields.Str(allow_none=True)

# Schema for BaiXe
class BaixeSchema(Schema):
    Ma_BaiXe = fields.Str(required=True)
    Ma_DV = fields.Str(required=True)
    Ten_BaiXe = fields.Str(required=True)

# Schema for ChiTietRaVao
class ChiTietRaVaoSchema(Schema):
    Ma_CT = fields.Str(required=True)
    Mssv = fields.Str(required=True)
    BienSoXe = fields.Str(required=True)
    Ma_BaiXe = fields.Str(required=True)
    TG_Vao = fields.DateTime(required=True)
    TG_Ra = fields.DateTime(allow_none=True)
    Gia = fields.Float(required=True)



