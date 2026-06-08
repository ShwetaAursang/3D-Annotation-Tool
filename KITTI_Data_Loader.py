#Implementation that loads RGB images, LiDAR point clouds, calibration files, and labels from the KITTI dataset.

import os
import cv2
import numpy as np


class KittiDataLoader:
    """
    KITTI Dataset Loader

    Loads:
    - RGB Images
    - LiDAR Point Clouds
    - Calibration Files
    - Annotation Labels
    """

    def __init__(self, dataset_path):
        self.dataset_path = dataset_path

        self.image_dir = os.path.join(dataset_path, "image_2")
        self.velodyne_dir = os.path.join(dataset_path, "velodyne")
        self.calib_dir = os.path.join(dataset_path, "calib")
        self.label_dir = os.path.join(dataset_path, "label_2")

    # --------------------------------------------------
    # Load RGB Image
    # --------------------------------------------------
    def load_image(self, frame_id):
        image_path = os.path.join(
            self.image_dir,
            f"{frame_id:06d}.png"
        )

        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        return image

    # --------------------------------------------------
    # Load LiDAR Point Cloud
    # --------------------------------------------------
    def load_lidar(self, frame_id):
        lidar_path = os.path.join(
            self.velodyne_dir,
            f"{frame_id:06d}.bin"
        )

        points = np.fromfile(
            lidar_path,
            dtype=np.float32
        ).reshape(-1, 4)

        return points

    # --------------------------------------------------
    # Load Calibration File
    # --------------------------------------------------
    def load_calibration(self, frame_id):
        calib_path = os.path.join(
            self.calib_dir,
            f"{frame_id:06d}.txt"
        )

        calib_data = {}

        with open(calib_path, "r") as file:
            for line in file.readlines():

                if ":" not in line:
                    continue

                key, value = line.split(":", 1)

                values = np.array(
                    [float(x) for x in value.split()]
                )

                calib_data[key] = values

        return calib_data

    # --------------------------------------------------
    # Load Labels
    # --------------------------------------------------
    def load_labels(self, frame_id):
        label_path = os.path.join(
            self.label_dir,
            f"{frame_id:06d}.txt"
        )

        labels = []

        if not os.path.exists(label_path):
            return labels

        with open(label_path, "r") as file:

            for line in file.readlines():

                data = line.strip().split()

                obj = {
                    "type": data[0],
                    "truncated": float(data[1]),
                    "occluded": int(data[2]),
                    "alpha": float(data[3]),
                    "bbox": list(map(float, data[4:8])),
                    "dimensions": list(map(float, data[8:11])),
                    "location": list(map(float, data[11:14])),
                    "rotation_y": float(data[14])
                }

                labels.append(obj)

        return labels

    # --------------------------------------------------
    # Number of Frames
    # --------------------------------------------------
    def total_frames(self):
        return len(
            sorted(os.listdir(self.image_dir))
        )
