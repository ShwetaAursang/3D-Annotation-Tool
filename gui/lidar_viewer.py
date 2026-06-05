#Module 3: LiDAR Point Cloud Viewer (Open3D)

#This module loads KITTI Velodyne .bin files and visualizes the LiDAR point cloud in 3D.

#Step 3.1 Install Open3D
#pip install open3d

import open3d as o3d
import numpy as np


class LidarViewer:

    def __init__(self):
        self.vis = o3d.visualization.Visualizer()

        self.vis.create_window(
            window_name="LiDAR Viewer",
            width=1000,
            height=700
        )

        self.point_cloud = o3d.geometry.PointCloud()

        self.vis.add_geometry(
            self.point_cloud
        )

    def update_point_cloud(self, points):

        xyz = points[:, :3]

        self.point_cloud.points = (
            o3d.utility.Vector3dVector(xyz)
        )

        self.vis.update_geometry(
            self.point_cloud
        )

        self.vis.poll_events()
        self.vis.update_renderer()

    def run(self):
        self.vis.run()

    def close(self):
        self.vis.destroy_window()
