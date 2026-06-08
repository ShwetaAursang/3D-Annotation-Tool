#Module 8: Machine Learning Assisted Annotation
#This module automatically detects objects in KITTI images and creates initial annotations that users can edit.
#For a portfolio project, a practical approach is to use a pretrained YOLO model.

#Install Dependencies
#pip install ultralytics

from ultralytics import YOLO


class ObjectDetector:

    def __init__(self):

        self.model = YOLO(
            "yolov8n.pt"
        )

    def detect(
        self,
        image
    ):

        results = self.model(
            image
        )

        detections = []

        for result in results:

            boxes = result.boxes

            for box in boxes:

                x1, y1, x2, y2 = (
                    box.xyxy[0]
                    .cpu()
                    .numpy()
                )

                cls = int(
                    box.cls[0]
                )

                conf = float(
                    box.conf[0]
                )

                class_name = (
                    self.model.names[cls]
                )

                detections.append(
                    {
                        "class": class_name,
                        "confidence": conf,
                        "bbox": [
                            int(x1),
                            int(y1),
                            int(x2),
                            int(y2)
                        ]
                    }
                )

        return detections
