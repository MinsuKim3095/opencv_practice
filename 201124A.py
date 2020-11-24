import cv2

imageFile = '.\OpenCV_Python\data/lena.jpg'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, 0)
cv2.imshow('Lena Color',img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()

imageFile = '.\OpenCV_Python\data/lena.jpg'
img = cv2.imread(imageFile)
cv2.imwrite('.\OpenCV_Python/data/Lena.bmp', img)
cv2.imwrite('.\OpenCV_Python/data/Lena.png', img)
cv2.imwrite('.\OpenCV_Python/data/Lena2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
cv2.imwrite('.\OpenCV_Python/data/Lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])

