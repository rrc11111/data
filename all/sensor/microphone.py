import pyaudio
import wave
import time

# 定义参数
CHUNK = 1024  # 每次读取的样本数
FORMAT = pyaudio.paInt16  # 音频格式
CHANNELS = 1  # 声道数（单声道）
RATE = 44100  # 采样率
RECORD_SECONDS = 30  # 录音时长（秒）


p = pyaudio.PyAudio()

# 获取可用的输入设备列表
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# 创建两个音频输入流
stream1 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=1)
stream2 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=2)
stream3 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=3)
stream4 = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK, input_device_index=6)

# print("* recording")

frames1 = []
frames2 = []
frames3 = []
frames4 = []

start_time = time.time()
recording = True

micro_str = time.time()
print('麦克风开始时间：', time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(micro_str)))
# print('麦克风开始时间：', micro_str)
timestamp1 = []
timestamp2 = []
timestamp3 = []
timestamp4 = []
try:
    while recording:
        data1 = stream1.read(CHUNK)
        data2 = stream2.read(CHUNK)
        data3 = stream3.read(CHUNK)
        data4 = stream4.read(CHUNK)
        frames1.append(data1)
        timestamp1.append(time.time())
        frames2.append(data2)
        timestamp2.append(time.time())
        frames3.append(data3)
        timestamp3.append(time.time())
        frames4.append(data4)
        timestamp4.append(time.time())

        elapsed_time = time.time() - start_time
        if elapsed_time >= RECORD_SECONDS:
            micro_end = time.time()
            micro_end_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(micro_end))

            print('麦克风结束时间：', micro_end_string)
            # print("录制时间达到指定时长，停止录制。")
            recording = False
except KeyboardInterrupt:
    # 捕捉键盘中断信号，例如用户按下Ctrl + C
    print("录制报错.")
    recording = False

# print("* done recording")

# 停止和关闭音频流
stream1.stop_stream()
stream2.stop_stream()
stream3.stop_stream()
stream4.stop_stream()
stream1.close()
stream2.close()
stream3.close()
stream4.close()
p.terminate()

gap = '\n'
f1 = open("D:/database/voice_data/0/" + micro_end_string + ".txt", "w")
f2 = open("D:/database/voice_data/1/" + micro_end_string + ".txt", "w")
f3 = open("D:/database/voice_data/2/" + micro_end_string + ".txt", "w")
f4 = open("D:/database/voice_data/3/" + micro_end_string + ".txt", "w")

WAVE_OUTPUT_FILENAME_1 = "D:/database/voice_data/0/" + micro_end_string + ".wav"  # 输出文件名1
WAVE_OUTPUT_FILENAME_2 = "D:/database/voice_data/1/" + micro_end_string + ".wav"
WAVE_OUTPUT_FILENAME_3 = "D:/database/voice_data/2/" + micro_end_string + ".wav"
WAVE_OUTPUT_FILENAME_4 = "D:/database/voice_data/3/" + micro_end_string + ".wav"

f1.write(gap.join(str(i) for i in timestamp1))
f2.write(gap.join(str(i) for i in timestamp2))
f3.write(gap.join(str(i) for i in timestamp3))
f4.write(gap.join(str(i) for i in timestamp4))

# 将录音数据写入文件
wf1 = wave.open(WAVE_OUTPUT_FILENAME_1, 'wb')
wf1.setnchannels(CHANNELS)
wf1.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf1.setframerate(RATE)
wf1.writeframes(b''.join(frames1))
wf1.close()

wf2 = wave.open(WAVE_OUTPUT_FILENAME_2, 'wb')
wf2.setnchannels(CHANNELS)
wf2.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf2.setframerate(RATE)
wf2.writeframes(b''.join(frames2))
wf2.close()

wf3 = wave.open(WAVE_OUTPUT_FILENAME_3, 'wb')
wf3.setnchannels(CHANNELS)
wf3.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf3.setframerate(RATE)
wf3.writeframes(b''.join(frames3))
wf3.close()

wf4 = wave.open(WAVE_OUTPUT_FILENAME_4, 'wb')
wf4.setnchannels(CHANNELS)
wf4.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
wf4.setframerate(RATE)
wf4.writeframes(b''.join(frames4))
wf4.close()


f1.close()
f2.close()
f3.close()
f4.close()