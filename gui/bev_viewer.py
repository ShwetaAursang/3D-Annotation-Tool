#Create BEV Viewer

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import (
    QPixmap,
    QImage
)
from PyQt5.QtCore import Qt


class BEVViewer(QLabel):

    def __init__(self):

        super().__init__()

        self.setAlignment(
            Qt.AlignCenter
        )

        self.setText(
            "BEV View"
        )

    def display_bev(
        self,
        bev_image
    ):

        h, w = bev_image.shape

        bytes_per_line = w

        q_image = QImage(
            bev_image.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_Grayscale8
        )

        pixmap = (
            QPixmap.fromImage(
                q_image
            )
        )

        self.setPixmap(
            pixmap.scaled(
                self.width(),
                self.height(),
                Qt.KeepAspectRatio
            )
        )
