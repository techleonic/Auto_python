import cv2

imagen =  cv2.imread("elfs.jpeg")
water_mark = cv2.imread("watermark.png")

x = imagen.shape[1] - water_mark.shape[1]
y = imagen.shape[0] - water_mark.shape[0]

water_mark_portion =  imagen[y:, x:]
cv2.imwrite("water_mark_portion.jpeg", water_mark_portion)

blend = cv2.addWeighted(water_mark_portion, 0.5, water_mark, 0.5, 0)
cv2.imwrite('blend.jpeg', blend)

imagen[y:, x:] = blend

cv2.imwrite("elfs-watermarked.jpeg", imagen)