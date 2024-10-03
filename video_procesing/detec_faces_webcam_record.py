import cv2

import cv2

video = cv2.VideoCapture(0)
# print(video.read())
success, frame = video.read()

#xml how a face looke like
face_cascade = cv2.CascadeClassifier('../imagen_processing/faces.xml')

#prepare the writer with codex fps and size video
output = cv2.VideoWriter('output.avi',
                         cv2.VideoWriter_fourcc(*'DIVX'), 30, (frame.shape[1],frame.shape[0]))
count = 0
while success:
    #detect faces in each frame
    faces = face_cascade.detectMultiScale(frame,  1.1, 4)
    #draw a square in each frame
    for (x, y, w, h) in  faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 255), 4)

    # writing each frame in the videowriter
    output.write(frame)

    #get new frame
    success, frame = video.read()
    count+=1
    print(count)
output.release()