from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)






# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# # Hash a password (usually done during registration)
# password = 'tham#123'
# hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

# # During login, check if the provided password matches the hashed password
# provided_password = 'tham#12'
# is_correct = bcrypt.check_password_hash(hashed_password, provided_password)

# if is_correct:
#     print("Password is correct!")
# else:
#     print("Password is incorrect.")



# import bcrypt

# # Hash a password (usually done during registration)
# password = 'tham#123'
# # Generate a salt and hash the password
# salt = bcrypt.gensalt()
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

# # During login, check if the provided password matches the hashed password
# provided_password = 'tham#12'
# is_correct = bcrypt.checkpw(provided_password.encode('utf-8'), hashed_password)

# if is_correct:
#     print("Password is correct!")
# else:
#     print("Password is incorrect.")


# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# # Băm mật khẩu
# password = "password123"
# hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# print("Hashed Password:", hashed_password)

# # Xác thực mật khẩu
# is_match = bcrypt.check_password_hash(hashed_password, password)
# print("Password Match:", is_match)



# from app.database import bcrypt

# def verify_password(stored_hashed_password, entered_password):
#     return bcrypt.check_password_hash(stored_hashed_password, entered_password)


# # Example values (replace these with actual values for testing)
# stored_hashed_password = "$2b$12$aV3i.VQbEafnO7ie6iC8dOlj684f1k6J8X9I3yRTkQ2dGuKHoaWYW"
# entered_password = "Tham#1234"

# # Verify password
# password_match = verify_password(stored_hashed_password, entered_password)
# print(f"Password Match: {password_match}")


# from app.database import bcrypt

# def verify_password(stored_hashed_password, entered_password):
#     """
#     Verify that the entered password matches the stored hashed password.
#     """
#     return bcrypt.check_password_hash(stored_hashed_password, entered_password)

# # Giả sử bạn có mật khẩu đã lưu và mật khẩu người dùng nhập vào
# stored_hashed_password = '$2b$12$SKTFFwhG6yIOaO3gRZ5ohOi17nvmUbulmbgXbeMb6H3e0tuFDY7Fy'
# entered_password = 'Tham#1234'

# # Kiểm tra mật khẩu
# if verify_password(stored_hashed_password, entered_password):
#     print("Password Match!")
# else:
#     print("Password Mismatch!")




# from app.database import bcrypt

# # Giả sử bạn có mật khẩu gốc và mật khẩu băm
# password = "Tham#1234"

# # Băm mật khẩu
# hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# print("Hashed Password before storing:", hashed_password)

# # Lưu hashed_password vào cơ sở dữ liệu
# # ...

# # Sau khi đọc hashed_password từ cơ sở dữ liệu
# stored_hashed_password = '$2b$12$KWAhVow242S0YL.i8Ovwf.JwIXJ1JzPBh7PM5GzOfGwx496d2twrq'
# print("Stored Hashed Password:", stored_hashed_password)

# # So sánh mật khẩu nhập vào với mật khẩu băm lưu trữ
# entered_password = "Tham#1234"
# password_match = bcrypt.check_password_hash(stored_hashed_password, entered_password)
# print("Password Match:", password_match)



# from app.database import bcrypt


# password = "Tham#1234"

# # Băm mật khẩu
# hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# print("Hashed Password before storing:", hashed_password)

# # Sau khi lưu hashed_password vào cơ sở dữ liệu, lấy lại để kiểm tra
# stored_hashed_password = 'Mật khẩu băm lưu trữ từ cơ sở dữ liệu'
# print("Stored Hashed Password:", stored_hashed_password)

# entered_password = "Tham#1234"
# password_match = bcrypt.check_password_hash(stored_hashed_password, entered_password)
# print("Password Match:", password_match)
