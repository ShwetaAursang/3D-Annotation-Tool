#Module 7: Annotation Export (KITTI Format)

#Now we'll save annotations to KITTI label files.

import os


class KittiExporter:

    def __init__(self, output_dir):

        self.output_dir = output_dir

        os.makedirs(
            output_dir,
            exist_ok=True
        )

    def save_annotations(
        self,
        frame_id,
        annotations
    ):

        filename = os.path.join(
            self.output_dir,
            f"{frame_id:06d}.txt"
        )

        with open(
            filename,
            "w"
        ) as f:

            for ann in annotations:

                line = (
                    f"{ann.class_name} "
                    f"0.00 0 -1.00 "
                    f"{ann.x1:.2f} "
                    f"{ann.y1:.2f} "
                    f"{ann.x2:.2f} "
                    f"{ann.y2:.2f} "
                    f"0.00 0.00 0.00 "
                    f"0.00 0.00 0.00 "
                    f"0.00\n"
                )

                f.write(line)

        print(
            f"Saved: {filename}"
        )
