import cv2
import numpy as np
image = cv2.imread("giraffe.jpeg")
backgroud = cv2.imread("safari.jpeg")

# [ 28 255  76]

print(image[40, 40])
height = image.shape[0]
width = image.shape[1]
resized_backgroud = cv2.resize(backgroud, (width, height))
for i in range(width):
    for j in range (height):
      pixel =    image[j, i]
      if np.any(pixel == [1, 255, 0]):
          image[j,i] = resized_backgroud[j, i]


cv2.imwrite("output.jpeg",image)
