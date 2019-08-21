import UltrasonicSensor
import Email
import Camera
import threading
import os
import time

distance_threshold = 20 #in CM
picture_taken = False

sensor = UltrasonicSensor.UltrasonicSensor(19, 26)
email = Email.Email()
camera = Camera.Camera()

def takepic_sendemail():
    #take a pic and save it
    image_path = camera.capture()
    #send email
    email.sendattachment("aj.bsb7@gmail.com", "RPi zero captured image", "<h1>BODY</h1>", image_path)
    #delete file
    try:
        os.remove(image_path)
    except:
        pass

try:
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
    print("Exit")
    sensor.cleanup()
