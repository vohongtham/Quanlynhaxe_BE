
# from flask import Blueprint, request, jsonify
# from app.services.object_tracking_service import ObjectTrackingService
# import cv2
# import numpy as np
# import base64

# tracking_bp = Blueprint('tracking', __name__)

# # Khởi tạo ObjectTrackingService
# tracking_service = ObjectTrackingService()

# @tracking_bp.route('/tracking/track', methods=['POST'])
# def track_objects():
#     try:
#         # Nhận tệp video từ client
#         file = request.files['frame']
#         file_bytes = file.read()

#         # Chuyển đổi bytes thành ảnh CV2
#         np_img = np.frombuffer(file_bytes, np.uint8)
#         frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

#         # Đảm bảo khung hình được đọc đúng
#         if frame is None:
#             return jsonify({"error": "Invalid image data"}), 400

#         # Xử lý khung hình để theo dõi
#         tracking_info = tracking_service.track_objects(frame)

#         # Chuyển đổi hình ảnh đã cắt sang định dạng base64
#         for item in tracking_info:
#             if 'cropped_image' in item:
#                 cropped_image = item['cropped_image']
#                 if cropped_image is not None and cropped_image.shape[0] > 0 and cropped_image.shape[1] > 0:
#                     success, buffer = cv2.imencode('.jpg', cropped_image)  # Mã hóa hình ảnh
#                     if success:
#                         base64_image = base64.b64encode(buffer).decode('utf-8')  # Chuyển đổi sang base64
#                         item['cropped_image'] = base64_image
#                     else:
#                         print(f"Error encoding image for track ID {item['track_id']}.")

#         # Trả về thông tin theo dõi
#         return jsonify({'tracking_info': tracking_info})

#     except Exception as e:
#         print(f"Error in track_objects: {e}")  # Ghi lại lỗi
#         return jsonify({"error": str(e)}), 500



from flask import Blueprint, request, jsonify
from app.services.object_tracking_service import LicensePlateRecognitionService  # Update the import
import cv2
import numpy as np

tracking_bp = Blueprint('tracking', __name__)

# Khởi tạo LicensePlateRecognitionService
tracking_service = LicensePlateRecognitionService()

@tracking_bp.route('/vehicle/identification', methods=['POST'])  # Change endpoint to reflect its function
def recognize_license_plates():
    try:
        # Nhận tệp video từ client
        file = request.files['frame']
        file_bytes = file.read()

        # Chuyển đổi bytes thành ảnh CV2
        np_img = np.frombuffer(file_bytes, np.uint8)
        frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        # Đảm bảo khung hình được đọc đúng
        if frame is None:
            return jsonify({"error": "Invalid image data"}), 400

        # Xử lý khung hình để nhận diện biển số
        license_plate_info = tracking_service.recognize_license_plates(frame)

        # Trả về thông tin nhận diện
        return jsonify({'license_plate_info': license_plate_info})

    except Exception as e:
        print(f"Error in recognize_license_plates: {e}")  # Ghi lại lỗi
        return jsonify({"error": str(e)}), 500
