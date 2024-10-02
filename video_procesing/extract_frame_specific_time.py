import cv2

video = cv2.VideoCapture("video.mp4")
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)
print(nr_frames, fps)

timestamp = '00:00:02.75'
timestamp_list = timestamp.split(":")
timestamp_list = [float(i) for i in timestamp_list]
hours, minutes, seconds = timestamp_list

framne_nr = (hours * 3600) * fps + (minutes * 60 * fps) + (seconds * fps)
video.set(1, framne_nr)
success, frame = video.read()
print(success,frame)
if success == True:
    cv2.imwrite(f"frame{hours}-{minutes}-{seconds}.jpg", frame)
else:
    print("unable to find the frame")