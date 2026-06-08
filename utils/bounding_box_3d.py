#Create 3D Bounding Box Class

import numpy as np


class BoundingBox3D:

    def __init__(
        self,
        class_name,
        x,
        y,
        z,
        length,
        width,
        height,
        rotation_y
    ):

        self.class_name = class_name

        self.x = x
        self.y = y
        self.z = z

        self.length = length
        self.width = width
        self.height = height

        self.rotation_y = rotation_y

    def get_corners(self):

        l = self.length
        w = self.width
        h = self.height

        corners = np.array([
            [ l/2,  w/2, 0],
            [ l/2, -w/2, 0],
            [-l/2, -w/2, 0],
            [-l/2,  w/2, 0],

            [ l/2,  w/2, h],
            [ l/2, -w/2, h],
            [-l/2, -w/2, h],
            [-l/2,  w/2, h]
        ])

        rotation = np.array([
            [
                np.cos(self.rotation_y),
                -np.sin(self.rotation_y),
                0
            ],
            [
                np.sin(self.rotation_y),
                np.cos(self.rotation_y),
                0
            ],
            [
                0,
                0,
                1
            ]
        ])

        corners = (
            rotation @ corners.T
        ).T

        corners += np.array([
            self.x,
            self.y,
            self.z
        ])

        return corners
