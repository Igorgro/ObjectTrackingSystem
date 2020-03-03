
from time import sleep
from math import pi
import serial
from threading import Lock
from threading import Thread

curr_angle = 90
prev_angle = 0
flag = True
is_rotating = False
mutex = Lock()


port = serial.Serial('/dev/ttyACM0', 9600) # the port name is platform-specific, change it before use


def _rad_to_deg(rad):
    return 180*(rad/pi)

def _set_angle(angle):
    port.write(bytes([angle]))

def rotate(rel_angle):
    global curr_angle, is_rotating
    deg = _rad_to_deg(rel_angle)
    print(is_rotating)
    if abs(deg) > 10 and not is_rotating:
        curr_angle = min(max(curr_angle + deg*0.8, 10), 170)

def do_rotate():
    global prev_angle, curr_angle, is_rotating
    while flag:
        if curr_angle != prev_angle:
            is_rotating = True
            prev_angle = curr_angle
            print('Rotating at deg', int(curr_angle))
            _set_angle(int(curr_angle))
            sleep(2)
            is_rotating = False


def detach():
    global flag
    flag = False
    port.close()

Thread(target=do_rotate).start()

