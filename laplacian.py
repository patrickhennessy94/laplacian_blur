import cv2

img = cv2.imread("images\dog.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(gray, cv2.CV_64F)
var = lap.var()

print(lap)
print(len(lap))
print(var)