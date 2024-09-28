import cv2
from pathlib import Path

main_dir = Path("input")
face_cascade = cv2.CascadeClassifier("faces.xml")
for img in main_dir.glob("*.jpeg"):
    img_input =  cv2.imread(str(img), 1)
    faces = face_cascade.detectMultiScale(img_input, 1.1 , 4)
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img_input, (x, y), (x+w, y+h) ,(255, 255, 255), 4)
    img_output = img_input
    cv2.imwrite(f"output/{img.name}", img_output)

    # print(None if len(faces) == 0 else faces)
    # for (x,y, w, h) in faces:
