#Bird's Eye View (BEV) Visualization

import numpy as np
import cv2


class BEVGenerator:

    def __init__(self):

        self.x_min = 0
        self.x_max = 50

        self.y_min = -25
        self.y_max = 25

        self.resolution = 0.1

    def generate(self, points):

        bev_width = int(
            (self.y_max - self.y_min)
            / self.resolution
        )

        bev_height = int(
            (self.x_max - self.x_min)
            / self.resolution
        )

        bev = np.zeros(
            (
                bev_height,
                bev_width
            ),
            dtype=np.uint8
        )

        xyz = points[:, :3]

        for point in xyz:

            x, y, z = point

            if (
                x < self.x_min or
                x > self.x_max or
                y < self.y_min or
                y > self.y_max
            ):
                continue

            px = int(
                (y - self.y_min)
                / self.resolution
            )

            py = int(
                (x - self.x_min)
                / self.resolution
            )

            bev[
                bev_height - py - 1,
                px
            ] = 255

        return bev
