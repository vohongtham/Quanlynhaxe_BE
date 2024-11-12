################################################################################################################
# Nhận diện với OCR
# import cv2
# import os  # Thêm để sử dụng os.urandom
# import numpy as np
# import base64
# import easyocr
# from yolov9.models.common import DetectMultiBackend, AutoShape

# # Object detection service class
# class LicensePlateRecognitionService:
#     def __init__(self):
#         self.conf_threshold = 0.5  # Confidence threshold for detections
#         self.device = "cpu"  # Use CPU for inference
#         self.model = DetectMultiBackend(weights="yolov9/weights/best.pt", device=self.device, fuse=True)
#         self.model = AutoShape(self.model)  # Prepare the model for inference
#         # self.reader = easyocr.Reader(['en'])  # Initialize the EasyOCR reader for English
#         self.reader = easyocr.Reader(['en'], gpu=True)


#         # Load class names
#         with open("yolov9/data_ext/classes.names") as f:
#             self.class_names = f.read().strip().split('\n')

#     def recognize_license_plates(self, frame):
#         print("Received frame for processing.")

#         if not isinstance(frame, np.ndarray):
#             raise ValueError("Invalid frame format: The frame should be a numpy array.")

#         print(f"Frame shape: {frame.shape}")

#         # Resize the frame to 640x480 resolution
#         frame = cv2.resize(frame, (640, 480))
#         print(f"Resized Frame shape: {frame.shape}")

#         # Detection process
#         results = self.model(frame)
#         print(f"Detection Results: {results.pred[0]}")

#         license_plate_info = []  # To store license plate recognition results

#         for detect_object in results.pred[0]:
#             if len(detect_object) >= 6:
#                 label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
#             else:
#                 continue 

#             x1, y1, x2, y2 = map(int, bbox)
#             class_id = int(label)

#             # We assume the class_id for license plates is known (adjust accordingly)
#             if class_id != 0:  # Replace 0 with the correct class ID for license plates
#                 continue

#             if confidence < self.conf_threshold:
#                 continue

#             # Crop the image of the detected license plate
#             cropped_img = frame[y1:y2, x1:x2]
#             print(f"Cropped image shape: {cropped_img.shape}")

#             if cropped_img.shape[0] > 0 and cropped_img.shape[1] > 0:
#                 ocr_result = self.reader.readtext(cropped_img)
#                 print(f"OCR Result: {ocr_result}")

#                 ocr_text = ' '.join([text for _, text, _ in ocr_result])
#                 print(f"OCR Text: {ocr_text}")

#                 # Thêm một giá trị ngẫu nhiên vào dữ liệu hình ảnh trước khi mã hóa
#                 random_suffix = os.urandom(16)  # Tạo chuỗi ngẫu nhiên
                
#                 # Encode cropped image to base64
#                 success, buffer = cv2.imencode('.jpg', cropped_img)
#                 if success:
#                     # Kết hợp hình ảnh với giá trị ngẫu nhiên
#                     combined_data = buffer.tobytes() + random_suffix
#                     cropped_img_base64 = base64.b64encode(combined_data).decode('utf-8')
#                     # cropped_img_base64 = base64.b64encode(buffer).decode('utf-8')
#                     license_plate_info.append({
#                         'bbox': [x1, y1, x2, y2],
#                         'text': ocr_text,
#                         'cropped_image': cropped_img_base64
#                     })
#                     print(f"Added license plate info: {ocr_text}")
#                 else:
#                     print("Error encoding image.")
#             else:
#                 print("Invalid cropped image.")

#         if not license_plate_info:
#             print("No license plates detected.")
#         else:
#             print(f"Final license plate info: {license_plate_info}")

#         return license_plate_info


import cv2
import numpy as np
import base64
import easyocr
from yolov9.models.common import DetectMultiBackend, AutoShape
import os  # Thêm để sử dụng os.urandom

# Object detection service class
class LicensePlateRecognitionService:
    def __init__(self):
        self.conf_threshold = 0.5  # Confidence threshold for detections
        self.device = "cpu"  # Use CPU for inference
        self.model = DetectMultiBackend(weights="yolov9/weights/best.pt", device=self.device, fuse=True)
        self.model = AutoShape(self.model)  # Prepare the model for inference
        self.reader = easyocr.Reader(['en'], gpu=True)

        # Load class names
        with open("yolov9/data_ext/classes.names") as f:
            self.class_names = f.read().strip().split('\n')

    # def recognize_license_plates(self, frame):
    #     print("Received frame for processing.")

    #     if not isinstance(frame, np.ndarray):
    #         raise ValueError("Invalid frame format: The frame should be a numpy array.")

    #     print(f"Frame shape: {frame.shape}")

    #     # Resize the frame to 640x480 resolution
    #     frame = cv2.resize(frame, (640, 480))
    #     print(f"Resized Frame shape: {frame.shape}")

    #     # Detection process
    #     results = self.model(frame)
    #     print(f"Detection Results: {results.pred[0]}")

    #     license_plate_info = []  # To store license plate recognition results

    #     for detect_object in results.pred[0]:
    #         if len(detect_object) >= 6:
    #             label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
    #         else:
    #             continue 

    #         x1, y1, x2, y2 = map(int, bbox)
    #         class_id = int(label)

    #         # We assume the class_id for license plates is known (adjust accordingly)
    #         if class_id != 0:  # Replace 0 with the correct class ID for license plates
    #             continue

    #         if confidence < self.conf_threshold:
    #             continue

    #         # Crop the image of the detected license plate
    #         cropped_img = frame[y1:y2, x1:x2]
    #         print(f"Cropped image shape: {cropped_img.shape}")

    #         if cropped_img.shape[0] > 0 and cropped_img.shape[1] > 0:
    #             ocr_result = self.reader.readtext(cropped_img)
    #             print(f"OCR Result: {ocr_result}")

    #             ocr_text = ' '.join([text for _, text, _ in ocr_result])
    #             print(f"OCR Text: {ocr_text}")

    #             # Thêm một giá trị ngẫu nhiên vào dữ liệu hình ảnh trước khi mã hóa
    #             random_suffix = os.urandom(16)  # Tạo chuỗi ngẫu nhiên
    #             success, buffer = cv2.imencode('.jpg', cropped_img)
    #             if success:
    #                 # Kết hợp hình ảnh với giá trị ngẫu nhiên
    #                 combined_data = buffer.tobytes() + random_suffix
    #                 cropped_img_base64 = base64.b64encode(combined_data).decode('utf-8')

    #                 license_plate_info.append({
    #                     'bbox': [x1, y1, x2, y2],
    #                     'text': ocr_text,
    #                     'cropped_image': cropped_img_base64
    #                 })
    #                 print(f"Added license plate info: {ocr_text}")
    #             else:
    #                 print("Error encoding image.")
    #         else:
    #             print("Invalid cropped image.")

    #     if not license_plate_info:
    #         print("No license plates detected.")
    #     else:
    #         print(f"Final license plate info: {license_plate_info}")

    #     return license_plate_info
    
    
    
    
    def recognize_license_plates(self, frame):
        print("Received frame for processing.")

        if not isinstance(frame, np.ndarray):
            raise ValueError("Invalid frame format: The frame should be a numpy array.")

        print(f"Frame shape: {frame.shape}")

        # Resize the frame to 640x480 resolution
        frame = cv2.resize(frame, (640, 480))
        print(f"Resized Frame shape: {frame.shape}")

        # Detection process
        results = self.model(frame)
        print(f"Detection Results: {results.pred[0]}")

        license_plate_info = []  # To store license plate recognition results

        for detect_object in results.pred[0]:
            if len(detect_object) >= 6:
                label, confidence, bbox = detect_object[5], detect_object[4], detect_object[:4]
            else:
                continue

            x1, y1, x2, y2 = map(int, bbox)
            class_id = int(label)

            # We assume the class_id for license plates is known (adjust accordingly)
            if class_id != 0:  # Replace 0 with the correct class ID for license plates
                continue

            if confidence < self.conf_threshold:
                continue

            # Crop the image of the detected license plate
            cropped_img = frame[y1:y2, x1:x2]
            print(f"Cropped image shape: {cropped_img.shape}")

            if cropped_img.shape[0] > 0 and cropped_img.shape[1] > 0:
                # Tăng độ nét của ảnh bằng bộ lọc làm sắc nét
                sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
                sharpened_img = cv2.filter2D(cropped_img, -1, sharpen_kernel)

                # Tăng cường độ tương phản bằng cách điều chỉnh giá trị gamma
                gamma = 1.2  # Điều chỉnh gamma để tăng cường độ sáng và độ tương phản
                look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)]).astype("uint8")
                enhanced_img = cv2.LUT(sharpened_img, look_up_table)

                # Nhận diện ký tự với EasyOCR trên ảnh màu đã làm sắc nét
                ocr_result = self.reader.readtext(enhanced_img)
                print(f"OCR Result: {ocr_result}")

                ocr_text = ' '.join([text for _, text, _ in ocr_result])
                print(f"OCR Text: {ocr_text}")

                # Mã hóa ảnh crop đã xử lý
                random_suffix = os.urandom(16)
                success, buffer = cv2.imencode('.jpg', enhanced_img)
                if success:
                    combined_data = buffer.tobytes() + random_suffix
                    cropped_img_base64 = base64.b64encode(combined_data).decode('utf-8')

                    license_plate_info.append({
                        'bbox': [x1, y1, x2, y2],
                        'text': ocr_text,
                        'cropped_image': cropped_img_base64
                    })
                    print(f"Added license plate info: {ocr_text}")
                else:
                    print("Error encoding image.")
            else:
                print("Invalid cropped image.")

        if not license_plate_info:
            print("No license plates detected.")
        else:
            print(f"Final license plate info: {license_plate_info}")

        return license_plate_info


