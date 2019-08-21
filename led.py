import RPi.GPIO as GPIO
from time import sleep

def blinkLED(pin,repeat):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)

    for i in range(repeat):
        GPIO.output(pin,GPIO.HIGH)
        sleep(0.1)
        GPIO.output(pin,GPIO.LOW)
        sleep(0.1)
        
    GPIO.cleanup()


LED_PIN = 19
blinkLED(LED_PIN,2)
