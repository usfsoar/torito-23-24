import time
from datetime import datetime
import csv

filename = datetime.now().strftime("%H:%M:%S") + ".csv"
f = open(filename, "w")
output = csv.writer(f)

timeSinceLaunch = 0
t_end = time.time() + 20

data = ["Time Since Launch", "Sensor1", "Sensor2", "n-1 Sensor", "Last Sensor"]
output.writerow(data)

sensor1 = "FILLER"
sensor2 = "FILLER"
lastSensor = "FILLER"

while time.time() < t_end:
    data = [str(timeSinceLaunch) + "s", sensor1, sensor2, "...", lastSensor]
    output.writerow(data)
    #Sleep for 1 second
    time.sleep(1)
    timeSinceLaunch += 1

f.close()