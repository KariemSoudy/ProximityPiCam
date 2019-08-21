import UltrasonicSensor

distance_threshold = 20 #in CM

sensor = UltrasonicSensor.UltrasonicSensor(19, 26)

picture_taken = False

try:
    while True:
        #print("get distance")
        distance = sensor.getdistance()

        if distance == -1: #sensor error
            continue
        
        if distance <= distance_threshold:
            if not picture_taken:
                print("too close, taking a picture...")
                picture_taken = True
        else:
            if picture_taken:
                print("too far, release...")
                picture_taken = False
        
except KeyboardInterrupt:
    print("Exit")
    sensor.cleanup()
