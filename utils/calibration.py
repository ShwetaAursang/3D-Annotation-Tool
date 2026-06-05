#Module 4: Sensor Calibration (KITTI)

#This module reads KITTI calibration files and transforms LiDAR points into the camera coordinate system.

import numpy as np


class Calibration:

    def __init__(self, calib_file):

        self.P2 = None
        self.R0 = None
        self.Tr_velo_to_cam = None

        self.load_calibration(calib_file)

    def load_calibration(self, calib_file):

        with open(calib_file, "r") as f:

            lines = f.readlines()

        for line in lines:

            if line.startswith("P2:"):

                values = np.array(
                    [float(x)
                     for x in line.strip().split()[1:]]
                )

                self.P2 = values.reshape(3, 4)

            elif line.startswith("R0_rect:"):

                values = np.array(
                    [float(x)
                     for x in line.strip().split()[1:]]
                )

                self.R0 = values.reshape(3, 3)

            elif line.startswith("Tr_velo_to_cam:"):

                values = np.array(
                    [float(x)
                     for x in line.strip().split()[1:]]
                )

                self.Tr_velo_to_cam = (
                    values.reshape(3, 4)
                )

    # ----------------------------------
    # Convert to Homogeneous Matrix
    # ----------------------------------

    def get_velo_to_cam_matrix(self):

        transform = np.eye(4)

        transform[:3, :] = (
            self.Tr_velo_to_cam
        )

        return transform

    # ----------------------------------
    # Rectification Matrix
    # ----------------------------------

    def get_rectification_matrix(self):

        rect = np.eye(4)

        rect[:3, :3] = self.R0

        return rect

    # ----------------------------------
    # LiDAR → Camera
    # ----------------------------------

    def lidar_to_camera(
        self,
        lidar_points
    ):

        n = lidar_points.shape[0]

        xyz = lidar_points[:, :3]

        xyz_hom = np.hstack(
            (
                xyz,
                np.ones((n, 1))
            )
        )

        velo_to_cam = (
            self.get_velo_to_cam_matrix()
        )

        rect = (
            self.get_rectification_matrix()
        )

        cam_points = (
            rect @
            velo_to_cam @
            xyz_hom.T
        )

        return cam_points.T
