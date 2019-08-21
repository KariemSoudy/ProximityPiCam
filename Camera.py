from picamera import PiCamera
import datetime
from time import sleep

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.date = datetime.datetime.now()

    def capture(self):
        image_path = '/home/pi/Desktop/Code/ProximityPiCam/capture/' + self.date.strftime("%y") + self.date.strftime("%m") + self.date.strftime("%d") + self.date.strftime("%M") + self.date.strftime("%H") + self.date.strftime("%S") + self.date.strftime("%f") + '.jpg'

        self.camera.start_preview()
        self.camera.exposure_mode = "sports"
        sleep(1)
        self.camera.capture(image_path)
        self.camera.stop_preview()

        return image_path
