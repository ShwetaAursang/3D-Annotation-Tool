#Auto Annotation Module

from utils.annotation import (
    Annotation
)


class AutoAnnotator:

    def __init__(
        self,
        detector
    ):

        self.detector = detector

    def generate_annotations(
        self,
        image
    ):

        detections = (
            self.detector.detect(
                image
            )
        )

        annotations = []

        for det in detections:

            annotation = Annotation(
                det["class"],
                det["bbox"][0],
                det["bbox"][1],
                det["bbox"][2],
                det["bbox"][3]
            )

            annotations.append(
                annotation
            )

        return annotations
