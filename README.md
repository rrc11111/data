# Enhancing robotic skill acquisition with multimodal sensory data: A novel dataset for kitchen tasks
Data related to the use of 17 different kitchen tools by 20 adults in dynamic scenarios was collected, including aspects of human touch, EMG signals, audio, whole-body motion, and eye-tracking data. The dataset consists of 680 segments (approximately 11 hours) containing data from seven modalities with 56,000 detailed annotations
The repository's code contains synchronized recording acquisition of 6 sensors, and wiseglove on windows
All sensor data acquisition codes are included in sensors.
You can generate the corresponding RGB and depth data from the mkv file in the kinect file in the .bat file processing data.

## **requirements:**

    Python 3, open3d, Numpy, Pandas, Scipy，pykinect_azure

## **example:**
https://xingying3x-cn-docs.nokov.com/shi-si-ren-ti-mu-ban/yi-53-dian-ren-ti-tie-dian-ji-qi-gu-ge-shuo-ming
Detailed Posting instructions can be found on this website.(If you have a nokov system you can also follow these instructions)
You can visualize trc files using:

```
python action.py
```
You can play back the Lxxx.xls file using the GraspMF.exe program in the wiseglove folder.

You can apply for eye tracker freeware to process the raw eye tracker data（https://www.tobii.com/zh/products/software/data-analysis-tools/tobii-pro-lab/free-trial#freetrial）
