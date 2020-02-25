
import RPi.GPIO as GPIO
from time import sleep
from math import pi

curr_angle = 90
SERVO_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)

def _rad_to_deg(rad):
    return 180*(rad/pi)

def _set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(SERVO_PIN, True)
    pwm.ChangeDutyCycle(duty)
    sleep(0.8)
    GPIO.output(SERVO_PIN, False)
    pwm.ChangeDutyCycle(0)

_set_angle(curr_angle)

def rotate(rel_angle):
    global curr_angle
    deg = _rad_to_deg(rel_angle)
    if abs(deg) > 10:
        curr_angle = min(max(curr_angle + deg*0.6, 0), 180)
        print('Rotating at deg', curr_angle)
        _set_angle(curr_angle)

def detach():
    GPIO.cleanup()
