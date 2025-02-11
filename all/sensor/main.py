import threading
import os
import time
import multiprocessing




def kinect_open():
    os.system('python ./kinect.py')


def tobii_open():
    os.system('python ./tobii.py')


def act_capture_open():
    os.system('python ./act_capture.py')


def trigno_open():
    os.system('python ./check_trigno.py')


def gloves_open():
    os.system('python ./gloves.py')

def micro_open():
    os.system('python ./microphone.py')


'''threads = []
# threads.append(threading.Thread(target=frpc))
threads.append(threading.Thread(target=kinect_open))  # args为函数接受的参数，多个
threads.append(threading.Thread(target=nokov_open))
threads.append(threading.Thread(target=act_capture_open))'''

if __name__ == "__main__":
    start = time.time()
    print('开始时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start)))


    p1 = multiprocessing.Process(target=gloves_open)
    p2 = multiprocessing.Process(target=kinect_open)
    p3 = multiprocessing.Process(target=act_capture_open)
    p4 = multiprocessing.Process(target=tobii_open)
    p5 = multiprocessing.Process(target=trigno_open)
    p6 = multiprocessing.Process(target=micro_open)

    # 启动子进程

    p1.start()
    
    p5.start()
    
    p4.start()
    
    p2.start()
    
    p6.start()
    p3.start()
    # 6.95485\3.91674\2.5796322\1.3684\0.0268

    # 等待fork的子进程终止再继续往下执行，可选填一个timeout参数

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    end = time.time()
    print('结束时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end)))
