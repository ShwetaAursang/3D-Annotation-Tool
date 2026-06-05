#Module 6: Annotation System (2D Bounding Box Annotation)

#This module allows users to:

#Draw bounding boxes with the mouse
#Select object classes
#Store annotations
#Display annotations on images
#Prepare labels for export

class Annotation:

    def __init__(
        self,
        class_name,
        x1,
        y1,
        x2,
        y2
    ):

        self.class_name = class_name

        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

    def to_dict(self):

        return {
            "class": self.class_name,
            "bbox": [
                self.x1,
                self.y1,
                self.x2,
                self.y2
            ]
        }
