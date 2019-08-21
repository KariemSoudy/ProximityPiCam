from picamera import PiCamera
import datetime
from time import sleep

class Camera:

    def __init__(self):
        self.camera = PiCamera()

    def capture(self):
        date = datetime.datetime.now()
        image_path = '/home/pi/Desktop/Code/ProximityPiCam/capture/' + date.strftime("%y") + date.strftime("%m") + date.strftime("%d") + date.strftime("%M") + date.strftime("%H") + date.strftime("%S") + date.strftime("%f") + '.jpg'

        self.camera.start_preview()
        self.camera.exposure_mode = "sports"
        sleep(1)
        self.camera.capture(image_path)
        self.camera.stop_preview()

        return image_path
