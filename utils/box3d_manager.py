#Create 3D Box Manager

class Box3DManager:

    def __init__(self):

        self.boxes = []

    def add_box(
        self,
        box
    ):

        self.boxes.append(
            box
        )

    def clear(self):

        self.boxes.clear()

    def get_boxes(self):

        return self.boxes
