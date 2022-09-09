from heapq import merge
import numpy as np
import cv2

# RGB of star
lower = np.array([50,200,240])
upper = np.array([120,230,255])

def star_tracker(img):
    output = cv2.inRange(img, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    output = cv2.dilate(output, kernel)
    output = cv2.erode(output, kernel)
    cv2.imwrite('oxxostudio.png', output)
    contours, hierarchy = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return len(contours)

def offset_text_cut_block(text_allocate_list):
     for i in range(len(text_allocate_list)):
        text_allocate_list[i][0][0] = text_allocate_list[i][0][0] + 60
        text_allocate_list[i][1][0] = text_allocate_list[i][1][0] + 130
        text_allocate_list[i][1][1] = text_allocate_list[i][1][1] + 30

text_allocate_list = [[(-6, 73), (604, 73), (604, 524), (-6, 524)], [(-4, 148), (13, 148), (13, 162), (-4, 162)], [(17, 148), (18, 148), (18, 161), (17, 161)], [(-6, 379), (26, 379), (26, 402), (-6, 402)], [(50, 181), (52, 181), (52, 195), (50, 195)], [(56, 181), (87, 181), (87, 195), (56, 195)], [(90, 181), (120, 181), (120, 195), (90, 195)], [(81, 222), (105, 222), (105, 233), (81, 233)], [(80, 266), (91, 266), (91, 278), (80, 278)], [(94, 266), (105, 266), (105, 278), (94, 278)], [(107, 266), (131, 266), (131, 278), (107, 278)], [(134, 266), (158, 266), (158, 278), (134, 278)], [(161, 266), (171, 266), (171, 278), (161, 278)], [(173, 266), (198, 266), (198, 278), (173, 278)], [(200, 266), (211, 266), (211, 278), (200, 278)], [(82, 310), (104, 310), (104, 323), (82, 323)], [(105, 310), (117, 310), (117, 322), (105, 322)], [(119, 310), (131, 310), (131, 322), (119, 322)], [(82, 356), (104, 356), (104, 367), (82, 367)], [(106, 356), (114, 356), (114, 367), (106, 367)], [(81, 401), (105, 401), (105, 412), (81, 412)], [(107, 401), (114, 401), (114, 412), (107, 412)], [(347, 73), (351, 73), (351, 88), (347, 88)], [(352, 73), (382, 73), (382, 88), (352, 88)], [(385, 73), (399, 73), (399, 88), (385, 88)], [(401, 73), (416, 73), (416, 88), (401, 88)], [(417, 73), (421, 73), (421, 88), (417, 88)], [(340, 93), (394, 93), (394, 109), (340, 109)], [(396, 93), (430, 93), (430, 109), (396, 109)], [(334, 222), (345, 222), (345, 234), (334, 234)], [(346, 222), (371, 222), (371, 234), (346, 234)], [(327, 267), (329, 267), (329, 279), (327, 279)], [(332, 266), (358, 266), (358, 278), (332, 278)], [(359, 266), (371, 266), (371, 278), (359, 278)], [(327, 311), (328, 311), (328, 323), (327, 323)], [(333, 311), (357, 311), (357, 323), (333, 323)], [(360, 311), (372, 311), (372, 323), (360, 323)], [(334, 355), (358, 355), (358, 367), (334, 367)], [(360, 355), (385, 355), (385, 367), (360, 367)], [(386, 355), (397, 355), (397, 367), (386, 367)], [(585, 238), (586, 238), (586, 247), (585, 247)], [(588, 238), (602, 238), (602, 247), (588, 247)], [(603, 238), (604, 238), (604, 247), (603, 247)], [(603, 513), (603, 524), (593, 524), (593, 513)]]

merge_result = []

idx = 0
for i in range(len(text_allocate_list)):
    if i < idx:
        continue
    tmp = text_allocate_list[i][2]
    for j in range (i + 1, len(text_allocate_list)):
        # if text_allocate_list[j][0][1] - text_allocate_list[i][0][1] == 5:
        if abs(text_allocate_list[j][0][1] - text_allocate_list[i][0][1]) < 2:
            tmp = text_allocate_list[j][2]
        else:
            merge_result.append([text_allocate_list[i][0], tmp])
            idx = j
            break
        
# merge_result = offset_text_cut_block(merge_result)

print(merge_result)


img = cv2.imread('./var/fullscreen.png')

color = (255,255,0)
color2 = (0,0,255)

print(len(merge_result))

num_of_stars = []

count = 0
for result in merge_result:
    img = cv2.rectangle(img, (result[0][0], result[0][1]), (result[1][0], result[1][1]), color, 3)
    img = cv2.rectangle(img, (result[0][0] + 60, result[0][1]), (result[0][0] + 130, result[0][1] + 30), color2, 3)
#     try:
#         num_of_stars.append(star_tracker(img[result[0][1] : result[0][1] + 30, result[0][0] + 60 : result[0][0] + 130]))
#     except:
#         num_of_stars.append(0)
#     # cv2.imwrite(str(count) + '.png', img[result[0][1] : result[0][1] + 30, result[0][0] + 60 : result[0][0] + 130])
    try:
        cv2.imwrite(str(count) + '.png', img[result[0][1] : result[0][1] + 30, result[0][0] + 60 : result[0][0] + 130])
    except:
        pass
    count += 1
# print(num_of_stars)


cv2.imwrite('text_track.png', img)
