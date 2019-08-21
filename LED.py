import RPi.GPIO as GPIO
from time import sleep
from enum import Enum

class BlinkSpeed(Enum):

    def __str__(self):
        return str(self.value)

    SLOW = 0.5
    NORMAL = 0.1
    FAST = 0.05

class LED:

    def __init__(self, _pin):
        self.PIN = _pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_pin,GPIO.OUT)
        

    def turnon(self):
        GPIO.output(self.PIN,GPIO.HIGH)
        

    def turnoff(self):
        GPIO.output(self.PIN,GPIO.LOW)
        

    def blink(self, _repeat, _speed):
        for i in range(_repeat):
            self.turnon()
            sleep(float(str(_speed)))
            self.turnoff()
            sleep(float(str(_speed)))


