from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton
)

from gui.image_viewer import ImageViewer
from utils.kitti_loader import KittiDataLoader


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "KITTI 3D Annotation Tool"
        )

        self.resize(1200, 800)

        self.frame_id = 0

        self.loader = KittiDataLoader(
            "data/training"
        )

        self.init_ui()

    def init_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        layout = QVBoxLayout()

        self.image_viewer = ImageViewer()

        load_button = QPushButton(
            "Load Frame"
        )

        load_button.clicked.connect(
            self.load_frame
        )

        layout.addWidget(load_button)
        layout.addWidget(self.image_viewer)

        central_widget.setLayout(layout)

    def load_frame(self):

        image = self.loader.load_image(
            self.frame_id
        )

        self.image_viewer.display_image(
            image
        )
