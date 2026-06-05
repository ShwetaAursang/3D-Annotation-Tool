#Draw LiDAR Points on RGB Image

import cv2
import numpy as np


def draw_projected_points(
    image,
    image_points,
    cam_points
):

    output = image.copy()

    height, width = output.shape[:2]

    for i in range(
        len(image_points)
    ):

        x = int(image_points[i, 0])
        y = int(image_points[i, 1])

        if (
            x < 0 or
            x >= width or
            y < 0 or
            y >= height
        ):
            continue

        depth = cam_points[i, 2]

        if depth < 20:
            color = (0, 0, 255)

        elif depth < 40:
            color = (0, 255, 255)

        else:
            color = (0, 255, 0)

        cv2.circle(
            output,
            (x, y),
            2,
            color,
            -1
        )

    return output
