# Enhancing robotic skill acquisition with multimodal sensory data: A novel dataset for kitchen tasks
Data related to the use of 17 different kitchen tools by 20 adults in dynamic scenarios was collected, including aspects of human touch, EMG signals, audio, whole-body motion, and eye-tracking data. The dataset consists of 680 segments (approximately 11 hours) containing data from seven modalities with 56,000 detailed annotations
The repository's code contains synchronized recording acquisition of 6 sensors, and wiseglove on windows
All sensor data acquisition codes are included in sensors.
You can generate the corresponding RGB and depth data from the mkv file in the kinect file in the .bat file processing data.

## **requirements:**

    Python 3, open3d, Numpy, Pandas, Scipy，pykinect_azure
