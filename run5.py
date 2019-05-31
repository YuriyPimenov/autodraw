import cv2
import random
import math

def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def is_between(a,c,b):
    return distance(a,c) + distance(c,b) == distance(a,b)

def middle(a,b):
    cX = a[0] + (b[0] - a[0]) * 0.5
    cY = a[1] + (b[1] - a[1]) * 0.5
    return (cX, cY)

img = cv2.imread('./level1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("thresh", thresh)

mor_img = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, (3, 3), iterations=3)

contours, hierarchy = cv2.findContours(mor_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # I addapted this part of the code. This is how my version works (2.4.16), but it could be different for OpenCV 3

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
i=0
points1 =[]
points2 =[]

for c in sorted_contours[1:]:
    i=i+1
    area = cv2.contourArea(c)
    if area > 4000:
        # print(area)
        # print(c)
        cv2.drawContours(img, [c], -1, (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)), 3)
        x, y, w, h = cv2.boundingRect(c)
        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        # cv2.circle(img, (x + w, y), 3, (0, 0, 255), -1)
        # cv2.circle(img, (x + w, y + h), 3, (0, 0, 255), -1)
        # cv2.circle(img, (x, y + h), 3, (0, 0, 255), -1)
        print('Контур '+str(i))
        if i==1:
            points1.append((x, y))
            points1.append((x + w, y))
            points1.append((x + w, y + h))
            points1.append((x, y + h))
        elif i==2:
            points2.append((x, y))
            points2.append((x + w, y))
            points2.append((x + w, y + h))
            points2.append((x, y + h))
        # res1 = distance((x, y),(x + w, y))
        # res2 = distance((x + w, y),(x + w, y + h))
        # res3 = distance((x + w, y + h),(x, y + h))
        # res4 = distance((x, y + h),(x, y))
        # print(res1)
        # print(res2)
        # print(res3)
        # print(res4)
print(points1)
print(points2)
paras = []
tmpP2 = (0,0)

for p1 in points1:
    print(p1)
    dist = 100000000
    for p2 in points2:
        print(p2)
        res = distance(p1, p2)
        if res==0:
            continue
        if res<dist:
            dist = res
            tmpP2 = p2
    paras.append([p1,tmpP2])
print(paras)

listCenter = []
for para in paras:
    center = middle(para[0],para[1])
    listCenter.append(center)
    cv2.circle(img, (int(center[0]),int(center[1])), 3, (0, 0, 255), -1)
cv2.imshow("mor_img", mor_img)
cv2.imshow("img", img)
cv2.waitKey(0)
