from ppadb.client import Client as AdbClient
import time

# See README.md for more info about these constants.

RECYCLE_POS = "190, 1081"
HOLD_RECYCLE_POS = "513, 1756"


def connect():
    _client = AdbClient(host="127.0.0.1", port=5037)

    devices = _client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    _device = devices[0]

    print(f'Connected to {_device}')

    return _device, _client


def start_recycle(recycle_num=1):
    device, client = connect()

    for i in range(recycle_num):
        device.shell("input tap 190 1081")  # recycle button
        time.sleep(2)  # wait for recycle screen to load
        device.shell("input touchscreen swipe 513 1756 513 1756 5000")  # hold down recycle button
        time.sleep(3)  # wait to get back to recycle screen


if __name__ == '__main__':
    num_to_recycle = input("Items to recycle: ")
    start_recycle(int(num_to_recycle))
