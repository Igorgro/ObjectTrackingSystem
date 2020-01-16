from imutils.video import VideoStream
import cv2

window_name = "Face tracking"

vs = VideoStream(src=0).start()
cv2.namedWindow(window_name, cv2.WINDOW_GUI_EXPANDED)
face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
while True:
    frame = vs.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=8, minSize=(10, 10))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
    cv2.imshow(window_name, frame)
    cv2.waitKey(1)
