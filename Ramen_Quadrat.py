# ラーメンコドラート用スクリプト
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

# 画像をインポート
path = "./data/ramen.jpg"
img = Image.open(path)

# img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, dp = 0.5, minDist=20, param1=100, param2=60, minRadius=0, maxRadius=0)

# img = cv2.imread(path)

# for circle in circles[0]:
#     x = int(circle[0])
#     y = int(circle[1])
#     r = int(circle[2])
#     cv2.circle(img, center=(x, y), radius=r, color=(0, 0, 0), thickness=5, lineType=cv2.LINE_4, shift=0)

# cv2.imwrite("circle7-3.jpg", img)

fig, ax = plt.subplots()

ax.imshow(img)

width, height = img.size

random_x = [random.randint(1,width) for i in range(10)]
random_y = [random.randint(1,height)for i in range(10)]

# プロットする座標
ax.scatter(random_x,random_y,c = 'black', s = 20)

# 画像を出力
plt.show()

