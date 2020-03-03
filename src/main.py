import cv2
import math
from concurrent.futures import ThreadPoolExecutor
from face_holder import FaceHolder

import servo3 as servo

webcam_angle = math.pi/3


def main():
    window_name = "Face tracking"
    vs = cv2.VideoCapture(0)
    cv2.namedWindow(window_name, cv2.WINDOW_GUI_EXPANDED)
    face_cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
    face_holder = FaceHolder()
    frame_counter = 0

    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            frame = vs.read()[1]
            frame_counter += 1
            coeff = frame.shape[0] / 240  # lower coefficient for image quality for better performance
            proceeding_frame = cv2.resize(frame, (int(frame.shape[1] / coeff), int(frame.shape[0] // coeff)), interpolation=cv2.INTER_AREA)
            faces = executor.submit(proceed_frame, face_cascade, proceeding_frame)
            face, centroid = face_holder.update(faces.result())  # actual face
            if face is not None:
                x, y, w, h = list(map(lambda el: int(el*coeff), face))
                centroid_x, centroid_y = list(map(lambda el: int(el*coeff), centroid))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
                if frame_counter > -1:
                    executor.submit(calculate_angle, centroid_x, frame.shape[1], webcam_angle)
                    frame_counter = 0
            cv2.imshow(window_name, frame)
            cv2.waitKey(1)


def proceed_frame(face_cascade, frame):
    return face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=8, minSize=(10, 10))


def calculate_angle(centroid_x, image_width, camera_angle):
    tan = (((image_width / 2) - centroid_x) / (image_width / 2)) * math.tan(camera_angle/2)
    servo.rotate(math.atan(tan))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        servo.detach()
        print('\nBye bye')
