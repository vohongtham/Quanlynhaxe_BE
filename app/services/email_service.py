# from flask_mail import Message
# from app.database import mail

# def send_email(recipient, ma_ct):
#     msg = Message("Mã thẻ xe của bạn",
#                   recipients=[recipient])
#     msg.body = f"Mã xác nhận thẻ xe của bạn là: {ma_ct}"
#     mail.send(msg)


from flask_mail import Message
from app.database import mail, db
from app.model import Sinhvien

def send_email(recipient, ma_ct):
    # Truy vấn cơ sở dữ liệu để lấy Mssv dựa trên email
    sinhvien = Sinhvien.query.filter_by(Email=recipient).first()
    if sinhvien is None:
        raise ValueError("Không tìm thấy sinh viên với email này")

    mssv = sinhvien.Mssv

    # Tạo nội dung email
    msg = Message(f"Mã thẻ xe của sinh viên {mssv}",
                  recipients=[recipient])
    msg.body = f"Mã thẻ xe của sinh viên {mssv} là: {ma_ct}"

    # Gửi email
    mail.send(msg)
