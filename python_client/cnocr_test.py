import cv2
import numpy as np
from cnocr import CnOcr

img_fp = 'template/test1.jpg'
ocr = CnOcr(
    rec_root="./rec",
    det_root="./det",
    det_model_name="ch_PP-OCRv3_det",
    rec_model_name="ch_PP-OCRv3"
)
out = ocr.ocr(img_fp)

print(out)

# image = cv2.imread("test1.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 降噪
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# # 或者
# # blurred = cv2.medianBlur(gray, 3)

# # 锐化
# sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# sharpened = cv2.filter2D(blurred, -1, sharpen_kernel)

# # 二值化
# thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# # 膨胀
# dilate_kernel = np.ones((5, 5), np.uint8)
# dilated = cv2.dilate(thresh, dilate_kernel, iterations=1)

# # 腐蚀
# erode_kernel = np.ones((5, 5), np.uint8)
# eroded = cv2.erode(dilated, erode_kernel, iterations=1)

# # text = pytesseract.image_to_string(eroded)

# # 边缘检测（可选）
# edges = cv2.Canny(eroded, 30, 150)

# # 尺度放大（可选）
# scaled = cv2.resize(edges, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)