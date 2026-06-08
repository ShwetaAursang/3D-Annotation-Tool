#Project 3D Box to Image

import numpy as np


def project_box(
    corners,
    calibration
):

    corners_hom = np.hstack(
        (
            corners,
            np.ones(
                (
                    corners.shape[0],
                    1
                )
            )
        )
    )

    projected = (
        calibration.P2
        @ corners_hom.T
    )

    projected = projected.T

    projected[:, 0] /= projected[:, 2]
    projected[:, 1] /= projected[:, 2]

    return projected[:, :2]
