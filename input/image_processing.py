from typing import List
from google.cloud import vision
from google.cloud import vision

import numpy as np
import io

import cv2

from util.common import read_static_data

api_host = "https://vision.googleapis.com"

bucket_name = "uma_factor_storage"

COUNT = 0

# set google application credentials by using file
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./.credentials/google_cred.json"

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    result = []
    result = texts[0].description.split("\n")

    text_allocate_list = []

    for text in response.text_annotations:
        text_allocate_list.append([(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])
        

    print("google API result: ", len(result))
    print(result)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return result, text_allocate_list

def merge_text_allocate_list(text_allocate_list: List):
    merge_result_list = []

    idx = 0
    for i in range(len(text_allocate_list)):
        if i < idx:
            continue
        tmp = text_allocate_list[i][2]
        for j in range (i + 1, len(text_allocate_list)):
            if abs(text_allocate_list[j][0][1] - text_allocate_list[i][0][1]) < 2:
                tmp = text_allocate_list[j][2]
            else:
                merge_result_list.append([text_allocate_list[i][0], tmp])
                idx = j
                break
        
    return merge_result_list

def cut_text(img, text_allocate_list: List):
    color = (255,255,0)
    color2 = (0,0,255)

    for text_allocate in text_allocate_list:
        img = cv2.rectangle(img, (text_allocate[0][0], text_allocate[0][1]), (text_allocate[1][0], text_allocate[1][1]), color, 3)
        img = cv2.rectangle(img, (text_allocate[0][0] + 60, text_allocate[0][1]), (text_allocate[0][0] + 130, text_allocate[0][1] + 30), color2, 3)

    cv2.imwrite('text_track.png', img)

# RGB of star
lower = np.array([50,200,240])
upper = np.array([120,230,255])

def star_tracker(img, count = 0):
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    cv2.imwrite(count + '.png', output)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return len(contours)
