#Box Translation Select,Move,Resize,Rotate,Delete

'''W → Move Forward

S → Move Backward

A → Move Left

D → Move Right

Q → Rotate Left

E → Rotate Right

+ → Increase Size

- → Decrease Size

Delete → Remove Box'''

class BoxTransform:

    @staticmethod
    def move(
        box,
        dx,
        dy,
        dz
    ):

        box.x += dx
        box.y += dy
        box.z += dz

    @staticmethod
    def rotate(
        box,
        angle
    ):

        box.rotation_y += angle

    @staticmethod
    def resize(
        box,
        dl,
        dw,
        dh
    ):

        box.length += dl
        box.width += dw
        box.height += dh
