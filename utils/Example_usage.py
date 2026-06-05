from utils.calibration import Calibration

calib = Calibration(
    "data/training/calib/000000.txt"
)

points = loader.load_lidar(0)

cam_points = calib.lidar_to_camera(
    points
)

print(cam_points.shape)
