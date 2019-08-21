import UltrasonicSensor

distance_threshold = 20 #in CM

sensor = UltrasonicSensor.UltrasonicSensor(19, 26)

picture_taken = False

try:
    while True:
        #print("get distance")
        distance = sensor.getdistance()
        
        if distance <= distance_threshold:
            #print("distance <= distance_threshold")
            if not picture_taken:
                #print("not picture_taken")
                #print("too close, taking a picture...")
                print("too close, taking a picture...")
                #print("picture_taken = True")
                picture_taken = True
        else:
            #print("ELSE distance > distance_threshold")
            #print("picture_taken = False")
            picture_taken = False
        
except KeyboardInterrupt:
    print("Exit")
    sensor.cleanup()
