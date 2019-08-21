import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    
    def __init__(self, _trig, _echo):
        self.TRIG = _trig
        self.ECHO = _echo

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.TRIG, GPIO.OUT)
        GPIO.setup(self.ECHO, GPIO.IN)


    def getdistance(self):
        try:
            GPIO.output(self.TRIG, False)
            time.sleep(0.1)
            
            GPIO.output(self.TRIG, True)
            time.sleep(0.00001)
            GPIO.output(self.TRIG, False)
            
            while GPIO.input(self.ECHO)==0:
              pulse_start = time.time()
    
            while GPIO.input(self.ECHO)==1:
              pulse_end = time.time()
    
            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 0)
            return distance

        except:
            return -1
        
    def cleanup(self):
        GPIO.cleanup()
