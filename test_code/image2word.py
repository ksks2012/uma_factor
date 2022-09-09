from PIL import Image
import pytesseract
import cv2
import numpy as np

user_tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = user_tesseract_cmd

def white_to_black(img):
    
    ret, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

    img[thresh == 255] = 0

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    erosion = cv2.erode(img, kernel, iterations = 1)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cv2.imshow("image", erosion)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

def get_mode(img):
    # 閾值取眾數
    # bincount（）：統計非負整數的個數，不能統計浮點數
    counts = np.bincount(img.flatten())
    # counts的index代表出現的數，counts[index]代表出現數的次數
    # 今要求counts[index] 排序後最大跟第二大的counts的index(代表眾數跟出現第二多次的數)
    # 最後一個元素是counts最大值的index ，倒數第二是二大
    counts_sort = np.argsort(counts)
    index = counts_sort[-1]
    # 以防圖片出現大量黑色面積
    # 出現大量黑色區塊的話，取第二多數
    if index <= 100:
        index = counts_sort[-2]
        return index
    # 否則就return原本的眾數
    return index


def two_val(image):
    blur = cv2.GaussianBlur(image, (3, 3), 0)
    c = get_mode(blur) * 0.7
    # 二值化
    ret, thresh1 = cv2.threshold(image, c, 255, cv2.THRESH_BINARY)

    # thresh1 = cv2.resize(thresh1, (160, 120))
    cv2.imshow('binary', thresh1)
    cv2.waitKey()

    text = pytesseract.image_to_string(thresh1, lang='chi_tra')
    print(text)


# img = Image.open('./fullscreen.png')
# img = Image.open('./Screenshot_20220813-055828.png')
img = cv2.imread('./Screenshot_20220813-055828.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# white_to_black(img)
two_val(img)

cv2.imshow('Result', img)
cv2.waitKey(0)

text = pytesseract.image_to_string(img, lang='chi_tra')
print(text)


