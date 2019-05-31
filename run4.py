import cv2
import numpy as np
import math

filename = './level1.jpg'
# path = r'C:\Users\selwyn77\Desktop\Stack\corner'


img = cv2.imread('./level1.jpg')
# img = cv2.imread(os.path.join(path, filename))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    #--- convert to grayscale

bi = cv2.bilateralFilter(gray, 5, 75, 75)
cv2.imshow('bi',bi)

dst = cv2.cornerHarris(bi, 2, 3, 0.04)

#--- create a black image to see where those corners occur ---
mask = np.zeros_like(gray)

#--- applying a threshold and turning those pixels above the threshold to white ---
mask[dst>0.01*dst.max()] = 255
cv2.imshow('mask', mask)

#Рисуем углы на изображении
img[dst > 0.01 * dst.max()] = [0, 0, 255]   #--- [0, 0, 255] --> Red ---
cv2.imshow('dst', img)

#получить массив всех пикселей с углами
coordinates = np.argwhere(mask)
#Переменная coordinates является массивом массивов. Преобразование его в список списков
coor_list = [l.tolist() for l in list(coordinates)]
#Преобразование вышеупомянутого в список кортежей
coor_tuples = [tuple(l) for l in coor_list]

#У меня есть простой и довольно наивный способ найти 4 угла.
#  Я просто рассчитал расстояние каждого угла до каждого другого угла.
#  Я сохранил те углы, расстояние которых превышало определенный порог.
thresh = 50

def distance(pt1, pt2):
    (x1, y1), (x2, y2) = pt1, pt2
    dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return dist

coor_tuples_copy = coor_tuples

i = 1
for pt1 in coor_tuples:

    print(' I :', i)
    for pt2 in coor_tuples[i::1]:
        print(pt1, pt2)
        print('Distance :', distance(pt1, pt2))
        if(distance(pt1, pt2) < thresh):
            coor_tuples_copy.remove(pt2)
    i+=1

#Теперь все, что вам нужно сделать, это просто отметить эти 4 точки на копии исходного изображения.
img2 = img.copy()
for pt in coor_tuples:
    cv2.circle(img2, tuple(reversed(pt)), 3, (0, 0, 255), -1)
cv2.imshow('Image with 4 corners', img2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()