import cv2
import numpy as np

path = './plan.jpg'

#0 - черный
#255 - белый

image = cv2.imread(path)
cv2.imshow("Image", image)
cv2.waitKey(0)

border = 170

countColumns = image.shape[0]
countRows = image.shape[1]
countRGB = image.shape[2]

for i in range(countColumns):
    for j in range(countRows):
        for k in range(countRGB):
            if image[i][j][k] < border:
                image[i][j][k] = 0
            else:
                image[i][j][k] = 255

# Select ROI
showCrosshair = False
fromCenter = False
r = cv2.selectROI("Image", image, fromCenter, showCrosshair)

# Crop image
imCrop = image[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

# Display cropped image
cv2.imshow("imCrop", imCrop)
cv2.waitKey(0)

wallTemplate = None
print('imCrop.size', imCrop.shape)

countColumns = imCrop.shape[0]
countRows = imCrop.shape[1]
countRGB = imCrop.shape[2]

for i in range(countColumns):
    isBlack = False
    for j in range(countRows):
        for k in range(countRGB):
            print("imCrop[%s][%s][%s] = %s" % (i, j, k, imCrop[i][j][k]))
            if imCrop[i][j][k] == 0:
                isBlack = True
    if isBlack == False:
        imCrop = imCrop[i+1:]

cv2.imshow("imCrop", imCrop)
cv2.waitKey(0)

countColumns = imCrop.shape[0]
countRows = imCrop.shape[1]
countRGB = imCrop.shape[2]

for j in range(countRows):
    isBlack = False
    for i in range(countColumns):
        for k in range(countRGB):
            print("imCrop[%s][%s][%s] = %s" % (i, j, k, imCrop[i][j][k]))
            if imCrop[i][j][k] == 0:
                isBlack = True
    if isBlack == False:
        imCrop = imCrop[i+1:]

cv2.imshow("imCrop", imCrop)
cv2.waitKey(0)

# M = cv2.getRotationMatrix2D((imCrop.shape[0]/2,imCrop.shape[1]/2),90,1)
# rotateImage = cv2.warpAffine(imCrop,M,(imCrop.shape[0],imCrop.shape[1]))

# cv2.imshow("wallTemplate", rotateImage)
# cv2.waitKey(0)
#
# print('imCrop.size', rotateImage.shape)
# for i in range(len(rotateImage)):
#     isBlack = False
#     for j in range(len(rotateImage[i])):
#         for k in range(len(rotateImage[i][j])):
#             print("imCrop[%s][%s][%s] = %s" % (i, j, k, rotateImage[i][j][k]))
#             if rotateImage[i][j][k] == 0:
#                 isBlack = True
#     if isBlack == False:
#         rotateImage = rotateImage[i+1:]
#
# M = cv2.getRotationMatrix2D((rotateImage.shape[0]/2,rotateImage.shape[1]/2),90,1)
# imCrop = cv2.warpAffine(rotateImage,M,(rotateImage.shape[0],rotateImage.shape[1]))

wallTemplate = imCrop

cv2.imshow("wallTemplate", wallTemplate)
cv2.waitKey(0)
# for i in image:
#         image[i][286][286][0] = 0
#         image[i][286][286][1] = 0
#         image[i][286][286][2] = 0
#         print(image[i][286])
# print('image[0] ', image[0])
# print('image[0][0] ',image[0][0])
cv2.imshow('План.jpg',image)


cv2.waitKey(0)
cv2.destroyAllWindows()