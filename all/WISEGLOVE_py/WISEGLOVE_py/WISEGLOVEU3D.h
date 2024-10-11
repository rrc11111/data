#include "windows.h"
extern "C" _declspec(dllexport) bool wgInit();
extern "C" _declspec(dllexport) bool wgInitManu(unsigned int comport,unsigned int baudrate=115200);
extern "C" _declspec(dllexport) int wgGetNumOfSensor(void);
extern "C" _declspec(dllexport) int  wgGetNumOfPressure(void);
extern "C" _declspec(dllexport) int  wgGetNumOfArm(void);
extern "C" _declspec(dllexport) void wgClose();
extern "C" _declspec(dllexport) bool wgLoadPressureCalib(char *filename);
extern "C" _declspec(dllexport) bool wgLoadCalib(char *filename);
extern "C" _declspec(dllexport) bool wgSaveCalib(char *filename);
extern "C" _declspec(dllexport) void wgSetCalibMode(int mode);
extern "C" _declspec(dllexport) bool wgSetCalib(int index, unsigned short min,unsigned short max, float angle);
/////////////////////////////////////////
extern "C" _declspec(dllexport) bool wgSetCalibmin(int index, unsigned short min);
extern "C" _declspec(dllexport) bool wgSetCalibmax(int index, unsigned short max);
extern "C" _declspec(dllexport) bool wgSetCalibRange(int index, float angle);
extern "C" _declspec(dllexport) unsigned short wgGetCalibmin(int index);
extern "C" _declspec(dllexport) unsigned short wgGetCalibmax(int index);
extern "C" _declspec(dllexport) float wgGetCalibRange(int index);
////////////////////////////////////////
extern "C" _declspec(dllexport) bool wgSetMin_adj(int index, float min_adj);
extern "C" _declspec(dllexport) bool wgSetMax_adj(int index, float max_adj);
////////////////////////////////////////
extern "C" _declspec(dllexport) float wgGetMin_adj(int index);
extern "C" _declspec(dllexport) float wgGetMax_adj(int index);
////////////////////////////////////////
extern "C" _declspec(dllexport) void wgResetCalib();
extern "C" _declspec(dllexport)  unsigned int wgGetData(unsigned short *data);
extern "C" _declspec(dllexport)  unsigned int  wgGetScaledData(unsigned short *data);
extern "C" _declspec(dllexport)  unsigned int  wgGetAngle(float *data);
extern "C" _declspec(dllexport)  unsigned int  wgGetPressure(int *pressure);
extern "C" _declspec(dllexport) unsigned int  wgGetPressureRaw(int  *pressure);

extern "C" _declspec(dllexport) unsigned int wgGetQuatOrg(float *quat); //读传感器原始数据
extern "C" _declspec(dllexport) unsigned int wgGetQuat(float *quat);
extern "C" _declspec(dllexport) bool wgSetFeedBack(unsigned char *data);
extern "C" _declspec(dllexport)  void wgResetQuat();

//extern "C" _declspec(dllexport) void wgSetCallbackEuler(float *euler);
//extern "C" _declspec(dllexport) void wgGetEuler(float* quat, float *angle);
