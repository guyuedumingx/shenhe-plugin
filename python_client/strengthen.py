import cv2
import numpy as np
import base64
import pytesseract

# extract_text_with_location("test.png")
def extract_text(img, psm_mode):
    # Use pytesseract to do OCR on the image with the chosen psm mode
    custom_config = f'--psm {psm_mode}'
    text_data = pytesseract.image_to_data(img, config=custom_config, lang='chi_sim+eng')

    # Output the recognized text
    print("Recognized Text:")
    print(pytesseract.image_to_string(img, config=custom_config, lang='chi_sim+eng'))

    # Output the text with location
    print("\nText with Location:")
    for count, data in enumerate(text_data.splitlines()):
        if count > 0:  # Skip the first line with column names
            data = data.split()
            if len(data) == 12:  # Valid data line
                text, x, y, width, height = data[11], data[6], data[7], data[8], data[9]
                print(f"Text: {text}, Position: ({x}, {y}), Size: ({width}x{height})")

# base64_image = 'your_base64_string_here'
# image_data = base64.b64decode(base64_image)
# np_array = np.frombuffer(image_data, np.uint8)
# image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
image = cv2.imread("test1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 降噪
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# 或者
# blurred = cv2.medianBlur(gray, 3)

# 锐化
sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened = cv2.filter2D(blurred, -1, sharpen_kernel)

# 二值化
thresh = cv2.threshold(sharpened, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 膨胀
dilate_kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(thresh, dilate_kernel, iterations=1)

# 腐蚀
erode_kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(dilated, erode_kernel, iterations=1)

# text = pytesseract.image_to_string(eroded)

# 边缘检测（可选）
edges = cv2.Canny(eroded, 30, 150)

# 尺度放大（可选）
scaled = cv2.resize(edges, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Example usage with PSM 6
extract_text(scaled, 6)




