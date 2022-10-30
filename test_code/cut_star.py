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

text_allocate_list = [[(30, 65), (417, 65), (417, 322), (30, 322)], [(30, 177), (33, 177), (33, 192), (30, 192)], [(35, 177), (67, 177), (67, 192), (35, 192)], [(70, 177), (101, 177), (101, 192), (70, 192)], [(60, 219), (85, 219), (85, 231), (60, 231)], [(87, 219), (98, 219), (98, 231), (87, 231)], [(61, 265), (72, 265), (72, 276), (61, 276)], [(74, 265), (86, 265), (86, 276), (74, 276)], [(87, 265), (113, 265), (113, 276), (87, 276)], [(115, 265), (139, 265), (139, 276), (115, 276)], [(142, 265), (152, 265), (152, 276), (142, 276)], [(155, 265), (180, 265), (180, 276), (155, 276)], [(182, 265), (193, 265), (193, 276), (182, 276)], [(60, 310), (72, 310), (72, 322), (60, 322)], [(72, 309), (98, 309), (98, 321), (72, 321)], [(99, 309), (112, 309), (112, 321), (99, 321)], [(332, 66), (336, 66), (336, 81), (332, 81)], [(337, 66), (368, 66), (368, 81), (337, 81)], [(371, 66), (386, 66), (386, 81), (371, 81)], [(387, 66), (402, 66), (402, 81), (387, 81)], [(404, 66), (408, 66), (408, 81), (404, 81)], [(325, 88), (379, 88), (379, 105), (325, 105)], [(382, 88), (417, 88), (417, 105), (382, 105)], [(318, 219), (343, 219), (343, 230), (318, 230)], [(320, 265), (343, 265), (343, 277), (320, 277)], [(345, 265), (354, 265), (354, 277), (345, 277)], [(318, 311), (343, 311), (343, 322), (318, 322)], [(345, 311), (371, 311), (371, 322), (345, 322)], [(372, 311), (384, 311), (384, 322), (372, 322)]]

merge_result = []

def merge_text_allocate_list(text_allocate_list):
    merge_result_list = []

    idx = 0
    for i in range(len(text_allocate_list)):
        print(i, idx)
        if i < idx:
            continue
        tmp = text_allocate_list[i][2]
        for j in range (i + 1, len(text_allocate_list)):
            print(j)
            if abs(text_allocate_list[j][0][1] - text_allocate_list[i][0][1]) < 2:
                tmp = text_allocate_list[j][2]
                print("merge", i, j)
            else:
                # left top, right down
                merge_result_list.append([text_allocate_list[i][0], tmp])
                idx = j
                break
        if i == len(text_allocate_list) - 1 and idx != i:
            merge_result_list.append([text_allocate_list[idx][0], tmp])

        
    return merge_result_list


# idx = 0
# for i in range(len(text_allocate_list)):
#     if i < idx:
#         continue
#     tmp = text_allocate_list[i][2]
#     for j in range (i + 1, len(text_allocate_list)):
#         # if text_allocate_list[j][0][1] - text_allocate_list[i][0][1] == 5:
#         if abs(text_allocate_list[j][0][1] - text_allocate_list[i][0][1]) < 2:
#             tmp = text_allocate_list[j][2]
#         else:
#             merge_result.append([text_allocate_list[i][0], tmp])
#             idx = j
#             break
merge_result = merge_text_allocate_list(text_allocate_list)
# merge_result = offset_text_cut_block(merge_result)

print(merge_result)


img = cv2.imread('./var/fullscreen.png')

color = (255,255,0)
color2 = (0,0,255)

print(len(merge_result))

num_of_stars = []

count = 0
for result in text_allocate_list:
    img = cv2.rectangle(img, (result[0][0], result[0][1]), (result[2][0], result[2][1]), (0,0,0), 3)
    # img = cv2.rectangle(img, (result[0][0] + 60, result[0][1]), (result[0][0] + 130, result[0][1] + 30), color2, 3)

for result in merge_result:
    img = cv2.rectangle(img, (result[0][0], result[0][1]), (result[1][0], result[1][1]), color, 3)
#     img = cv2.rectangle(img, (result[0][0] + 60, result[0][1]), (result[0][0] + 130, result[0][1] + 30), color2, 3)
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
