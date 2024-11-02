from pyzbar.pyzbar import decode
import cv2

video = cv2.VideoCapture(0)
success, frame = video.read()


while success:
    detected_barcodes = decode(frame)

    if detected_barcodes:
        for barcode in detected_barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)
            print(barcode.data)
            print(barcode.type)
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

    success, frame = video.read()

cv2.imwrite(f'barcode_detection.jpg', frame)
video.release()
cv2.destroyAllWindows()