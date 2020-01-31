import math


class FaceHolder:
    def __init__(self):
        self.face_center = (0, 0)

    def update(self, faces):
        if len(faces) == 0:
            return None, self.face_center
        if self.face_center == (0, 0):
            (x, y, w, h) = faces[0]
            self.face_center = (x + w / 2, y + h / 2)
            return faces[0], self.face_center
        else:
            distances = []
            centers = []
            for (x, y, w, h) in faces:
                center = (x + w/2, y + h/2)
                centers.append(center)
                distances.append(math.sqrt((self.face_center[0] - center[0]) * (self.face_center[0] - center[0])
                                           +
                                           (self.face_center[1] - center[1]) * (self.face_center[1] - center[1])))  # calculate distance
            min_index = distances.index(min(distances))
            self.face_center = centers[min_index]
            return faces[min_index], self.face_center


