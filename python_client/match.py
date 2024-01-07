import cv2
import numpy as np

def align_images(image_path, template_path):
    # 读取图像和模板
    img = cv2.imread(image_path)
    template = cv2.imread(template_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 初始化SIFT检测器
    sift = cv2.SIFT_create()

    # 查找关键点和描述符
    kp1, des1 = sift.detectAndCompute(img_gray, None)
    kp2, des2 = sift.detectAndCompute(template_gray, None)

    # 使用FLANN匹配
    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    MIN_MATCH_COUNT = 10
    if len(good_matches) >= MIN_MATCH_COUNT:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        # 计算单应性矩阵
        M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

        # 应用变换
        aligned = cv2.warpPerspective(img, M, (template.shape[1], template.shape[0]))

        return aligned
    else:
        print("Not enough matches are found - {}/{}".format(len(good_matches), MIN_MATCH_COUNT))
        return None

# 使用示例
aligned_image = align_images("test2_t.jpg", "test2.jpg")
if aligned_image is not None:
    cv2.imshow("Aligned Image", aligned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
