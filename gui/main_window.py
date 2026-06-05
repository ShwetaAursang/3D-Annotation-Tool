from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)

from gui.image_viewer import ImageViewer
from gui.lidar_viewer import LidarViewer
from utils.kitti_loader import KittiDataLoader
from utils.calibration import Calibration
from utils.projection import Projection
from utils.draw_projection import (
    draw_projected_points
)

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "KITTI 3D Annotation Tool"
        )

        self.resize(1200, 800)

        # Dataset Path
        self.dataset_path = "data/training"

        # Current Frame
        self.frame_id = 0

        # Load KITTI Dataset
        self.loader = KittiDataLoader(
            self.dataset_path
        )

        # Total Frames
        self.total_frames = (
            self.loader.total_frames()
        )

        # Viewers
        self.image_viewer = ImageViewer()
        self.lidar_viewer = LidarViewer()

        # Build GUI
        self.init_ui()

    def init_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout()

        # ----------------------------------
        # Frame Information
        # ----------------------------------

        self.frame_label = QLabel(
            f"Frame: {self.frame_id}"
        )

        main_layout.addWidget(
            self.frame_label
        )

        # ----------------------------------
        # Buttons
        # ----------------------------------

        button_layout = QHBoxLayout()

        self.prev_button = QPushButton(
            "Previous Frame"
        )

        self.load_button = QPushButton(
            "Load Frame"
        )

        self.next_button = QPushButton(
            "Next Frame"
        )

        self.prev_button.clicked.connect(
            self.previous_frame
        )

        self.load_button.clicked.connect(
            self.load_frame
        )

        self.next_button.clicked.connect(
            self.next_frame
        )

        button_layout.addWidget(
            self.prev_button
        )

        button_layout.addWidget(
            self.load_button
        )

        button_layout.addWidget(
            self.next_button
        )

        main_layout.addLayout(
            button_layout
        )

        # ----------------------------------
        # RGB Viewer
        # ----------------------------------

        main_layout.addWidget(
            self.image_viewer
        )

        central_widget.setLayout(
            main_layout
        )

    # ----------------------------------
    # Load Current Frame
    # ----------------------------------

def load_frame(self):

    image = self.loader.load_image(
        self.frame_id
    )

    points = self.loader.load_lidar(
        self.frame_id
    )

    calib_file = (
        f"data/training/calib/"
        f"{self.frame_id:06d}.txt"
    )

    calibration = Calibration(
        calib_file
    )

    projection = Projection(
        calibration
    )

    image_points, cam_points = (
        projection.project_lidar_to_image(
            points
        )
    )

    image = draw_projected_points(
        image,
        image_points,
        cam_points
    )

    self.image_viewer.display_image(
        image
    )

    self.lidar_viewer.update_point_cloud(
        points
    )

    # ----------------------------------
    # Next Frame
    # ----------------------------------

    def next_frame(self):

        if self.frame_id < (
            self.total_frames - 1
        ):

            self.frame_id += 1

            self.load_frame()

    # ----------------------------------
    # Previous Frame
    # ----------------------------------

    def previous_frame(self):

        if self.frame_id > 0:

            self.frame_id -= 1

            self.load_frame()

    # ----------------------------------
    # Close Application
    # ----------------------------------

    def closeEvent(self, event):

        self.lidar_viewer.close()

        event.accept()
