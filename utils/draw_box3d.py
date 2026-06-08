#Draw 3D Box

import cv2


def draw_box3d(
    image,
    points
):

    points = points.astype(int)

    edges = [

        (0,1),
        (1,2),
        (2,3),
        (3,0),

        (4,5),
        (5,6),
        (6,7),
        (7,4),

        (0,4),
        (1,5),
        (2,6),
        (3,7)
    ]

    for start, end in edges:

        cv2.line(
            image,
            tuple(points[start]),
            tuple(points[end]),
            (0,255,0),
            2
        )

    return image
