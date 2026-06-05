#Module 5: LiDAR-to-Camera Projection

#This module projects LiDAR points onto the RGB image using KITTI calibration matrices.

import numpy as np


class Projection:

    def __init__(self, calibration):
        self.calib = calibration

    def project_lidar_to_image(
        self,
        lidar_points
    ):

        cam_points = (
            self.calib.lidar_to_camera(
                lidar_points
            )
        )

        # Keep only points in front of camera
        valid = cam_points[:, 2] > 0

        cam_points = cam_points[valid]

        projected = (
            self.calib.P2 @
            cam_points.T
        )

        projected = projected.T

        projected[:, 0] /= projected[:, 2]
        projected[:, 1] /= projected[:, 2]

        return projected[:, :2], cam_points
