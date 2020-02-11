from gpiozero import Servo
from time import sleep
from math import pi

curr_angle = 0

servo = Servo (12, min_pulse_width=0.0005, max_pulse_width=0.002)
sleep(3)
servo.detach()

def rotate (rel_angle):
    """
    Rotate camera to relative angle
    """
    print(rel_angle)
    global curr_angle
    if abs(rel_angle) > pi/16: # 1/12
        print("Rotating to angle", curr_angle)
        curr_angle = curr_angle + (rel_angle/pi)
        servo.value = curr_angle
        sleep(3)
        servo.detach()
    else:
        servo.detach()
    


