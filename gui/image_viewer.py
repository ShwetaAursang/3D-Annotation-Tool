#Image Viewer (PyQt5 + OpenCV).
#This module displays KITTI RGB images inside the GUI.

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import (
    QPainter,
    QPen,
    QColor
)

from utils.annotation import Annotation


class ImageViewer(QLabel):

    def __init__(self):

        super().__init__()

        self.annotations = []

        self.drawing = False

        self.start_point = QPoint()
        self.end_point = QPoint()

        self.current_class = "Car"

    # ------------------------------
    # Mouse Press
    # ------------------------------

    def mousePressEvent(
        self,
        event
    ):

        if event.button() == Qt.LeftButton:

            self.drawing = True

            self.start_point = event.pos()
            self.end_point = event.pos()

    # ------------------------------
    # Mouse Move
    # ------------------------------

    def mouseMoveEvent(
        self,
        event
    ):

        if self.drawing:

            self.end_point = event.pos()

            self.update()

    # ------------------------------
    # Mouse Release
    # ------------------------------

    def mouseReleaseEvent(
        self,
        event
    ):

        if event.button() == Qt.LeftButton:

            self.drawing = False

            annotation = Annotation(
                self.current_class,
                self.start_point.x(),
                self.start_point.y(),
                self.end_point.x(),
                self.end_point.y()
            )

            self.annotations.append(
                annotation
            )

            self.update()

    # ------------------------------
    # Paint Bounding Boxes
    # ------------------------------

    def paintEvent(
        self,
        event
    ):

        super().paintEvent(event)

        painter = QPainter(self)

        pen = QPen(
            QColor(255, 0, 0)
        )

        pen.setWidth(2)

        painter.setPen(pen)

        # Existing annotations

        for ann in self.annotations:

            painter.drawRect(
                ann.x1,
                ann.y1,
                ann.x2 - ann.x1,
                ann.y2 - ann.y1
            )

            painter.drawText(
                ann.x1,
                ann.y1 - 5,
                ann.class_name
            )

        # Current drawing

        if self.drawing:

            painter.drawRect(
                self.start_point.x(),
                self.start_point.y(),
                self.end_point.x()
                - self.start_point.x(),
                self.end_point.y()
                - self.start_point.y()
            )
