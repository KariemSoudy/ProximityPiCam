from UltrasonicSensor import UltrasonicSensor
from Email import Email
from Camera import Camera
from LED import LED,BlinkSpeed
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

#methods
def takepic_sendemail():
    #take a pic and save it
    image_path = camera.capture()
    #send email
    #email.sendattachment("aj.bsb7@gmail.com", "RPi zero captured image", "<h1>BODY</h1>", image_path)
    #delete file
    #try:
        #os.remove(image_path)
    #except:
        #pass

def cleanup():
    grn_led.cleanup()
    red_led.cleanup()

#main program
try:
    grn_led.turnon()
    red_led.turnoff()
    while True:
        #print("get distance")
        distance = sensor.getdistance()

        if distance == -1: #sensor error
            continue
        
        if distance <= distance_threshold:
            if not picture_taken:
                print("too close, taking a picture...")
                takepic_sendemail_thread = threading.Thread(target = takepic_sendemail, args = (), kwargs = {})
                takepic_sendemail_thread.start()
                picture_taken = True
        else:
            if picture_taken:
                print("too far, release...")
                picture_taken = False

        time.sleep(0.1)

except KeyboardInterrupt:
    print("Cleanup")
    cleanup()
    print("Exit")
    sensor.cleanup()
