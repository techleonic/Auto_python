import os
import cv2
import numpy

columns = 3
rows = 2
horizontal_margin = 40
vertical_margin = 20

images = os.listdir("images")
print(images)
images_object = [cv2.imread(f'images/{filename}') for filename in images]
shape = cv2.imread("images/1.jpeg").shape

white_backgrund = numpy.zeros((shape[0] * rows + horizontal_margin * (rows+1), shape[1]*columns + vertical_margin * (columns +1), shape[2]),
                              numpy.uint8)
white_backgrund.fill(255)

positions = [(x, y) for x in range(columns) for y in range(rows)]
print(positions)

for (pos_x, pox_y), images in zip(positions, images_object):

    x = pos_x * (shape[1] + vertical_margin) + vertical_margin
    y = pox_y * (shape[0]  + horizontal_margin) + horizontal_margin
    white_backgrund[y:y+shape[0], x:x+shape[1]] = images

cv2.imwrite("grid.jpeg", white_backgrund)