# Enhancing robotic skill acquisition with multimodal sensory data: A novel dataset for kitchen tasks
Data related to the use of 17 different kitchen tools by 20 adults in dynamic scenarios was collected, including aspects of human touch, EMG signals, audio, whole-body motion, and eye-tracking data. The dataset consists of 680 segments (approximately 11 hours) containing data from seven modalities with 56,000 detailed annotations
The repository's code contains synchronized recording acquisition of 6 sensors, and wiseglove on windows
All sensor data acquisition codes are included in sensors.
You can generate the corresponding RGB and depth data from the mkv file in the kinect file in the .bat file processing data.

## 🛠️ Installation
The code is designed to run on a Windows 10 system. All necessary dependencies and setup instructions for Windows have been provided to ensure smooth execution
Make sure you have Python 3.7 or higher installed 
Install necessary Python packages. If you haven't done so already, you can use pip to install packages:
    pip install open3d numpy pandas scipy pykinect_azure
### NOKOV
The XINGYING software should be running, calibrated, and configured for network streaming before starting the Python scripts.
The "Catch - trigger" switch in the data broadcast panel enables, that is, the remote trigger function is enabled. The port is the broadcast port for XINGYING to send control commands, and the default port is 7061
### Wise-gloves
Connect the Manus USB to the computer,The raw data, Angle data, and arm spatial position data of the data glove are called in real time through python.
### Delsys
Download and install the corresponding device SDK from Delsys official website (e.g. Trigno SDK)
## **example:**
https://xingying3x-cn-docs.nokov.com/shi-si-ren-ti-mu-ban/yi-53-dian-ren-ti-tie-dian-ji-qi-gu-ge-shuo-ming
Detailed Posting instructions can be found on this website.(If you have a nokov system you can also follow these instructions)
You can visualize trc files using:

```
python action.py
```
You can play back the Lxxx.xls file using the GraspMF.exe program in the wiseglove folder.

You can apply for eye tracker freeware to process the raw eye tracker data（https://www.tobii.com/zh/products/software/data-analysis-tools/tobii-pro-lab/free-trial#freetrial）
