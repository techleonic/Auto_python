import cv2

video = cv2.VideoCapture('video.mp4')
# print(video.read())
success, frame = video.read()
count = 1
while success:
    cv2.imwrite(f'frames/{count}.jpg', frame)
    success, frame = video.read()
    count+=1
