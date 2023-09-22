import time
import os
from datetime import datetime
import csv

#Filing Initalization for reading
filename = time.ctime() + ".csv"
f = open(filename, "w")
output = csv.writer(f)

data = ["Time Since Launch", "Sensor1", "Sensor2", "n-1 Sensor", "Last Sensor"]
output.writerow(data)

sensor1 = "FILLER"
sensor2 = "FILLER"
lastSensor = "FILLER"
timeSinceLaunch = 0

#Functions Go here
def FileWrite():
    data = [str(timeSinceLaunch) + "s", sensor1, sensor2, "...", lastSensor]
    output.writerow(data)

print("STUFF HERE FOR Titles")

#Think of a way to have two files just in case the rocket explodes and no backup is found
    #Kind of like saving a copy to the ssh machine and to the pi itself
#GUI
while True:
    # Read all the ADC channel values in a list.
    os.system('clear')
    values = [0]*8
    for i in range(8):
        values[i] += i + 1
        # The read_adc function will get the value of the specified channel (0-7).
        #values[i] = mcp.read_adc(i)
    # Print the ADC values.
    #print('Current Time | PSensor {0:>4} | PSensor {1:>4} | PSensor {2:>4} | PSensor {3:>4} | PSensor {4:>4} | PSensor {5:>4} | PSensor {6:>4} | PSensor {7:>4} |'.format(*range(8)), "TSensor 1 | TSensor 2 | TSensor 3 | TSensor 4")
    #print('-' * 100)
    #print(time.ctime(), '| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values) + " Hello world | This is a test")
    print(time.ctime(), "| Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("-"*60)
    for i in range(8):
        print("Press Sensor ", i, ":", values[i])
    print("Temp Sensor 1: ", "Test Value", "F")
    print("Temp Sensor 2: ", "Test Value", "F")
    print("Temp Sensor 3: ", "Test Value", "F")
    print("Temp Sensor 4: ", "Test Value", "F")
    f = open(filename, "a")
    output = csv.writer(f)
    FileWrite()
    timeSinceLaunch += 0.5
    # Pause for half a second.
    f.close()
    time.sleep(0.5)

