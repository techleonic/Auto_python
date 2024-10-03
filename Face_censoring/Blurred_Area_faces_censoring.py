import cv2

video = cv2.VideoCapture("smile.mp4")
success , frame = video.read()
face_cascade = cv2.CascadeClassifier("faces.xml")
output = cv2.VideoWriter("blurred_face.avi", cv2.VideoWriter_fourcc(*'DIVX'),30,
                         (frame.shape[1],frame.shape[0]))
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50,50))
    output.write(frame)
    success,frame = video.read()

output.release()

