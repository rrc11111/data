"""
Tests communication with and data acquisition from a Delsys Trigno wireless
EMG system. Delsys Trigno Control Utility needs to be installed and running,
and the device needs to be plugged in. Tests can be run with a device connected
to a remote machine if needed.

The tests run by this script are very simple and are by no means exhaustive. It
just sets different numbers of channels and ensures the data received is the
correct shape.

Use `-h` or `--help` for options.
"""

import argparse
import numpy as np
import time
import pandas as pd

try:
    import pytrigno
except ImportError:
    import sys
    sys.path.insert(0, '..')
    import pytrigno

def check_emg(host):
    dev = pytrigno.TrignoEMG(channel_range=(4, 11), samples_per_read=4000,
                             host=host)

    '''# test single-channel
    dev.start()
    for i in range(4):
        data = dev.read()
        assert data.shape == (1, 270)
    dev.stop()'''

    # test multi-channel
    dev.set_channel_range((0, 4))
    time_emg_begin = time.time()
    dev.start()
    for i in range(4):
        data_EMG = dev.read()
        assert data_EMG.shape == (5, 4000)
    dev.stop()
    time_emg_end = time.time()
    data_emg_timestamp = np.linspace(time_emg_begin, time_emg_end, dev.samples_per_read)
    time_EMG = time.time()
    time_EMG_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_EMG))
    data_EMG = np.vstack((data_emg_timestamp, data_EMG))
    data_EMG = pd.DataFrame(data_EMG, columns=None)
    data_EMG.to_csv('D:/database/delsys_data/emg/EMG'+time_EMG_string+'.csv', index=None)
    # np.savetxt('./EMG/emg/EMG'+time_EMG_string+'.csv', data_EMG)


def check_accel(host):
    dev = pytrigno.TrignoAccel(channel_range=(0, 2), samples_per_read=10,
                               host=host)

    time_acc_begin = time.time()
    dev.start()
    for i in range(4):
        data_acc = dev.read()
        assert data_acc.shape == (3, 10)
    dev.stop()

    time_acc_end = time.time()
    data_acc_timestamp = np.linspace(time_acc_begin, time_acc_end, dev.samples_per_read)
    data_acc = np.vstack((data_acc_timestamp, data_acc))

    time_acc = time.time()
    time_acc_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_acc))
    data_acc = pd.DataFrame(data_acc)
    data_acc.to_csv('D:/database/delsys_data/acc/acc' + time_acc_string + '.csv', index=None)
    #np.savetxt('./EMG/acc/acc' + time_acc_string + '.csv', data_acc)


def check_emg_acc(host):
    dev_emg = pytrigno.TrignoEMG(channel_range=(0,15), samples_per_read=800,
                             host=host)
    dev_acc = pytrigno.TrignoAccel(channel_range=(0,15), samples_per_read=800,
                               host=host)

    # test multi-channel

    dev_emg.start()
    dev_acc.start()
    time_emg_acc_begin = time.time()
    print('肌电开始时间：',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_emg_acc_begin)))
    # print('肌电开始时间：', time_emg_acc_begin)
    for i in range(16):
        data_EMG = dev_emg.read()
        data_acc = dev_acc.read()
        assert data_EMG.shape == (16, 800)#40*second
    time_emg_acc_end = time.time()
    print('肌电结束时间：', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_emg_acc_end)))
    dev_emg.stop()
    dev_acc.stop()
    time_emg_acc_end = time.time()
    data_emg_acc_timestamp = np.linspace(time_emg_acc_begin, time_emg_acc_end, dev_emg.samples_per_read)
    time_end_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_emg_acc_end))

    data_EMG = np.vstack((data_emg_acc_timestamp, data_EMG))
    data_EMG = pd.DataFrame(data_EMG, columns=None)
    data_EMG.to_csv('D:/database/delsys_data/emg/EMG'+time_end_string+'.csv', index=None)

    data_acc = np.vstack((data_emg_acc_timestamp, data_acc))
    data_acc = pd.DataFrame(data_acc)
    data_acc.to_csv('D:/database/delsys_data/acc/acc' + time_end_string + '.csv', index=None)

    # np.savetxt('./EMG/emg/EMG'+time_EMG_string+'.csv', data_EMG)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-a', '--addr',
        dest='host',
        default='100.78.236.13',
        help="IP address of the machine running TCU. Default is localhost.")
    args = parser.parse_args(args=[])
    check_emg_acc(args.host)
    #check_emg(args.host)
    #check_accel(args.host)