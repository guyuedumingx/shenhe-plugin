import asyncio
import json
import cv2
import numpy as np
import websockets
from PIL import Image
from io import BytesIO
import base64

# sample
{
    "action": "to_gray",
    "data": {},
    "args": {}
}

def one_to_gray(img_base64):
    if not img_base64.startswith("data:"):
        print("The picture is not a base64 string")
        return
    # 将Base64编码的图片转换为OpenCV图像
    img_data = base64.b64decode(img_base64.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 将图片转换为灰度图
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 进行二值化处理
    _, binary_img = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)

    # 使用Pillow显示处理后的图片
    img_pil = Image.fromarray(binary_img)
    img_pil.show()

def all_to_gray(images):
    imgs = list(filter(lambda x: x.startswith("data:"), images))
    for img_base64 in imgs:
        one_to_gray(img_base64)

async def process_image(websocket, path):
    async for message in websocket:
        # 解析收到的数据
        req = json.loads(message)
        if req['action'] == "all_to_gray":
            all_to_gray(req['data'])
        elif req['action'] == "one_to_gray":
            one_to_gray(req['data'])
            


start_server = websockets.serve(process_image, "localhost", 8889)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
