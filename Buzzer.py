import RPi.GPIO as GPIO
from time import sleep

class Buzzer:

    def __init__(self, _pin):
        self.PIN = _pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_pin,GPIO.OUT)
        

    def beepon(self):
        GPIO.output(self.PIN,GPIO.HIGH)
        

    def beepoff(self):
        GPIO.output(self.PIN,GPIO.LOW)
        

    def beep(self, _repeat, _speed):
        for i in range(_repeat):
            self.beepon()
            sleep(float(str(_speed)))
            self.beepoff()
            sleep(float(str(_speed)))

