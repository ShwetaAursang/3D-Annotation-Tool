# 3D-Annotation-Tool
Developed a 3D annotation tool for KITTI autonomous driving datasets using Python, PyQt5, OpenCV, and Open3D. Implemented RGB image visualization, LiDAR point cloud processing, calibration-based projection, and annotation management to support computer vision and machine learning workflows.


# 3D KITTI Annotation Tool

A desktop application for visualizing and annotating KITTI autonomous driving datasets.

## Features

* RGB image visualization
* LiDAR point cloud visualization
* KITTI calibration support
* LiDAR point projection onto images
* Bounding box annotation
* Annotation export
* Modular PyQt5 interface

## Technologies

* Python
* PyQt5
* OpenCV
* Open3D
* NumPy

## Dataset

KITTI Vision Benchmark Suite

## Future Improvements

* 3D bounding box editing
* PointPillars integration
* Auto-annotation using deep learning
* Multi-camera support
* BEV (Bird's Eye View) visualization

# Project Workflow

## Step 1: Load KITTI Dataset

* Read RGB images from the KITTI image folder.
* Load LiDAR point clouds from Velodyne binary files.
* Parse calibration files and existing annotations.

## Step 2: Initialize Application

* Launch the PyQt5-based desktop interface.
* Create panels for image viewing, point cloud visualization, and annotation controls.

## Step 3: Visualize RGB Images

* Display camera images using OpenCV.
* Enable image navigation, zooming, and object inspection.

## Step 4: Visualize LiDAR Point Clouds

* Load and render 3D LiDAR data using Open3D.
* Allow users to rotate, zoom, and explore the point cloud scene.

## Step 5: Perform Sensor Calibration

* Read KITTI calibration matrices.
* Transform LiDAR coordinates into the camera coordinate system.

## Step 6: Project LiDAR Points onto Images

* Project 3D LiDAR points onto the RGB image plane.
* Generate synchronized visualization between camera and LiDAR sensors.

## Step 7: Create and Edit Annotations

* Select objects within the scene.
* Create, modify, and manage object annotations.
* Support common object classes such as Car, Pedestrian, and Cyclist.

## Step 8: Save Annotation Data

* Store annotation information in KITTI-compatible format.
* Maintain organized annotation files for future model training.

## Step 9: Prepare Machine Learning Dataset

* Export labeled data for computer vision and autonomous driving applications.
* Use generated annotations for object detection and sensor fusion models.


Module 1 – KITTI Data Loader: Developed a Python-based data loading module to parse KITTI RGB images, LiDAR point clouds, calibration files, and annotation labels. Implemented efficient file handling and structured data extraction to support visualization, sensor fusion, and annotation workflows.


Module 2 – RGB Image Viewer: Developed an image visualization component using PyQt5 and OpenCV to display KITTI camera frames. Implemented image loading, rendering, resizing, and GUI integration to support interactive dataset exploration.


Module 3 – LiDAR Point Cloud Viewer: Developed a 3D visualization module using Open3D to render KITTI Velodyne point clouds. Implemented point cloud loading, geometry updates, and interactive scene exploration for autonomous driving data analysis.



## Step 10: Future Enhancements

* Automatic object detection using deep learning models.
* 3D bounding box editing.
* Bird's Eye View (BEV) visualization.
* Semi-automatic annotation assistance.
* Multi-sensor dataset support.


# Results

* Successfully visualized KITTI RGB images and LiDAR point clouds.
* Implemented sensor fusion using calibration matrices.
* Created an annotation workflow for autonomous driving datasets.
* Generated training-ready annotations for machine learning models.

