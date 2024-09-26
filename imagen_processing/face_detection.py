import cv2

img =  cv2.imread("humans.jpeg", 1)
face_cascade = cv2.CascadeClassifier("faces.xml")

faces = face_cascade.detectMultiScale(img, 1.1,4)

print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x, y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite("human_faces.jpeg", img)