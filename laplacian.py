import cv2
import os

path = "C:\\images\\examples\\"
var_total = 0

img_list = os.listdir(path)
#print(len(img_list))

for f in img_list:
    img = cv2.imread(path + f)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    lap = cv2.Laplacian(gray, cv2.CV_64F)
    var = lap.var()
    var_total += var

    #print(lap)
    #print(len(lap))
    #print(var)

print('Avg var: ', var_total/len(img_list))