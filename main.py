from UltrasonicSensor import UltrasonicSensor
from Email import Email
from Camera import Camera
from LED import LED,BlinkSpeed
from Buzzer import Buzzer,BeepSpeed
import threading
import os
import time

#variables
distance_threshold  = 20 #in CM
picture_taken       = False

#objects
sensor              = UltrasonicSensor(19, 26)
email               = Email()
camera              = Camera()
grn_led             = LED(13)
red_led             = LED(6)
buzzer              = Buzzer(5)

#methods
def blink_red():
    red_led.blink(5, BlinkSpeed.NORMAL)


def blink_green():
    grn_led.blink(5, BlinkSpeed.NORMAL)


def beep_buzzer():
    buzzer.beep(5, BlinkSpeed.NORMAL)

    
def takepic_sendemail():
    #take a pic and save it
    image_path = camera.capture()
    #send email
    #email.sendattachment("aj.bsb7@gmail.com", "RPi zero captured image", "<h1>BODY</h1>", image_path)
    #delete file
    try:
        os.remove(image_path)
    except:
        pass
    blink_green()
    reset()
    

def take_picture_async():
    blink_red_thread = threading.Thread(target = blink_red, args = (), kwargs = {})
    blink_red_thread.start()

    beep_buzzer_thread = threading.Thread(target = beep_buzzer, args = (), kwargs = {})
    beep_buzzer_thread.start()
    
    takepic_sendemail_thread = threading.Thread(target = takepic_sendemail, args = (), kwargs = {})
    takepic_sendemail_thread.start()


def reset():
    grn_led.turnon()
    red_led.turnoff()

def cleanup():
    grn_led.turnoff()
    red_led.turnoff()

#main program
try:
    reset()
    buzzer.beep(2, BeepSpeed.FAST)
    while True:
        #print("get distance")
        distance = sensor.getdistance()

        if distance == -1: #sensor error
            continue
        
        if distance <= distance_threshold:
            if not picture_taken:
                print("too close, taking a picture...")
                take_picture_async()
                picture_taken = True
        else:
            if picture_taken:
                print("too far, release...")
                buzzer.beep(2, BeepSpeed.FAST)
                picture_taken = False

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Cleanup")
    cleanup()
    print("Exit")
    sensor.cleanup()
