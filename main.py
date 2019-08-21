import UltrasonicSensor
import Email
import threading

distance_threshold = 20 #in CM
picture_taken = False

sensor = UltrasonicSensor.UltrasonicSensor(19, 26)
email = Email.Email()


def takepic_sendemail():
    #take a pic and save it
    #send email
    email.sendattachment("aj.bsb7@gmail.com", "RPi zero test email", "<h1>TEST</h1>", "/home/pi/Desktop/Code/ProximityPiCam/pi.jpg")    

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

except KeyboardInterrupt:
    print("Exit")
    sensor.cleanup()
