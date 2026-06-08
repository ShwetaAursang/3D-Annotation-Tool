from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QMessageBox
)

from gui.image_viewer import ImageViewer
from gui.lidar_viewer import LidarViewer

from utils.kitti_loader import KittiDataLoader
from utils.calibration import Calibration
from utils.projection import Projection
from utils.draw_projection import draw_projected_points
from utils.export_kitti import KittiExporter
from ml.detector import (
    ObjectDetector
)

from ml.auto_annotation import (
    AutoAnnotator
)
from gui.bev_viewer import (
    BEVViewer
)

from utils.bev_generator import (
    BEVGenerator
)

class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "KITTI 3D Annotation Tool"
        )

        self.resize(1400, 900)

        # Dataset Path
        self.dataset_path = "data/training"

        # Current Frame
        self.frame_id = 0

        # Dataset Loader
        self.loader = KittiDataLoader(
            self.dataset_path
        )

        # Exporter
        self.exporter = KittiExporter(
            "annotations"
        )

        # Total Frames
        self.total_frames = (
            self.loader.total_frames()
        )

        # Viewers
        self.image_viewer = ImageViewer()
        self.lidar_viewer = LidarViewer()
        
        self.init_ui()
        self.detector = (
            ObjectDetector()
        )
        
        self.auto_annotator = (
            AutoAnnotator(
                self.detector
            )
        )
        self.bev_viewer = (
            BEVViewer()
        )
        
        self.bev_generator = (
            BEVGenerator()
        )
    # ==================================================
    # UI
    # ==================================================

    def init_ui(self):

        central_widget = QWidget()

        self.setCentralWidget(
            central_widget
        )

        main_layout = QVBoxLayout()

        # ----------------------------------
        # Frame Label
        # ----------------------------------

        self.frame_label = QLabel(
            f"Frame: {self.frame_id}"
        )

        main_layout.addWidget(
            self.frame_label
        )
        self.auto_button = QPushButton(
            "Auto Annotate"
        )
        
        self.auto_button.clicked.connect(
            self.auto_annotate
        )
        
        button_layout.addWidget(
            self.auto_button
        )
        # ----------------------------------
        # Class Selector
        # ----------------------------------

        self.class_selector = QComboBox()

        self.class_selector.addItems(
            [
                "Car",
                "Pedestrian",
                "Cyclist"
            ]
        )

        self.class_selector.currentTextChanged.connect(
            self.change_class
        )

        main_layout.addWidget(
            self.class_selector
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

        self.show_button = QPushButton(
            "Show Annotations"
        )

        self.save_button = QPushButton(
            "Save Annotations"
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

        self.show_button.clicked.connect(
            self.show_annotations
        )

        self.save_button.clicked.connect(
            self.save_annotations
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

        button_layout.addWidget(
            self.show_button
        )

        button_layout.addWidget(
            self.save_button
        )

        main_layout.addLayout(
            button_layout
        )
        main_layout.addWidget(
            self.bev_viewer
        )
        # ----------------------------------
        # Image Viewer
        # ----------------------------------

        main_layout.addWidget(
            self.image_viewer
        )

        central_widget.setLayout(
            main_layout
        )

    # ==================================================
    # Change Annotation Class
    # ==================================================

    def change_class(self, text):

        self.image_viewer.current_class = text

    # ==================================================
    # Load Frame
    # ==================================================

    def load_frame(self):

        try:

            # RGB Image
            image = self.loader.load_image(
                self.frame_id
            )

            # LiDAR
            lidar_points = (
                self.loader.load_lidar(
                    self.frame_id
                )
            )

            # Calibration
            calib_file = (
                f"{self.dataset_path}/calib/"
                f"{self.frame_id:06d}.txt"
            )

            calibration = Calibration(
                calib_file
            )

            # Projection
            projection = Projection(
                calibration
            )

            image_points, cam_points = (
                projection.project_lidar_to_image(
                    lidar_points
                )
            )

            # Draw projected points
            projected_image = (
                draw_projected_points(
                    image,
                    image_points,
                    cam_points
                )
            )

            # Display image
            self.image_viewer.display_image(
                projected_image
            )

            # Display LiDAR
            self.lidar_viewer.update_point_cloud(
                lidar_points
            )

            self.frame_label.setText(
                f"Frame: {self.frame_id}"
            )

            print(
                f"Loaded Frame: "
                f"{self.frame_id}"
            )

            print(
                f"LiDAR Points: "
                f"{lidar_points.shape[0]}"
            )
            bev = (
                self.bev_generator.generate(
                    lidar_points
                )
            )
            
            self.bev_viewer.display_bev(
                bev
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
            )

    # ==================================================
    # Next Frame
    # ==================================================

    def next_frame(self):

        if self.frame_id < (
            self.total_frames - 1
        ):

            self.frame_id += 1

            self.load_frame()

    # ==================================================
    # Previous Frame
    # ==================================================

    def previous_frame(self):

        if self.frame_id > 0:

            self.frame_id -= 1

            self.load_frame()

    # ==================================================
    # Show Annotations
    # ==================================================

    def show_annotations(self):

        annotations = (
            self.image_viewer.annotations
        )

        print(
            "\n========== ANNOTATIONS =========="
        )

        if len(annotations) == 0:

            print(
                "No annotations found."
            )

        for ann in annotations:

            print(
                ann.to_dict()
            )

        print(
            "=================================\n"
        )

    # ==================================================
    # Save Annotations
    # ==================================================

    def save_annotations(self):

        try:

            annotations = (
                self.image_viewer.annotations
            )

            self.exporter.save_annotations(
                self.frame_id,
                annotations
            )

            QMessageBox.information(
                self,
                "Saved",
                f"Annotations saved for frame "
                f"{self.frame_id}"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Export Error",
                str(e)
            )
    def auto_annotate(self):

    try:

        image = (
            self.loader.load_image(
                self.frame_id
            )
        )

        annotations = (
            self.auto_annotator
            .generate_annotations(
                image
            )
        )

        self.image_viewer.annotations = (
            annotations
        )

        self.image_viewer.update()

        print(
            f"Generated "
            f"{len(annotations)} "
            f"annotations"
        )

    except Exception as e:

        print(e)
    # ==================================================
    # Close Application
    # ==================================================

    def closeEvent(self, event):

        try:

            self.lidar_viewer.close()

        except Exception:
            pass

        event.accept()
