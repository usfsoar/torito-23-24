from tkinter import *
import time
from datetime import datetime
import csv
import random

#Main frame for the GUI
root = Tk()

#Lables for the GUI
lab1 = Label(root)
filler = Label(root)
pSensor1 = Label(root)
pSensor2 = Label(root)
pSensor3 = Label(root)
pSensor4 = Label(root)
pSensor5 = Label(root)
pSensor6 = Label(root)
pSensor7 = Label(root)
pSensor8 = Label(root)
filler2 = Label(root)
tSensor1 = Label(root)
tSensor2 = Label(root)
tSensor3 = Label(root)
tSensor4 = Label(root)

#Pack the labels onto the GUI
lab1.pack(pady=(10,0))
lab1.config(font=(25))
filler.pack(padx=(10,10))
pSensor1.pack(pady=(5,0)) 
pSensor2.pack(pady=(5,0)) 
pSensor3.pack(pady=(5,0)) 
pSensor4.pack(pady=(5,0)) 
pSensor5.pack(pady=(5,0)) 
pSensor6.pack(pady=(5,0)) 
pSensor7.pack(pady=(5,0)) 
pSensor8.pack(pady=(5,0))
filler2.pack()
tSensor1.pack(pady=(5,0))
tSensor2.pack(pady=(5,0))
tSensor3.pack(pady=(5,0))
tSensor4.pack(pady=(5,10))

#File writing and opening
filename = time.ctime() + ".csv"
f = open(filename, "w")
output = csv.writer(f)

data = ["Time Since Launch", "P Sensor1", "P Sensor2", "n-1 Sensor", "Temp 1", "Temp 2", "Temp 3", "Temp 4"]
output.writerow(data)
f.close()

#Variables are initalized
sensor1 = "FILLER"
sensor2 = "FILLER"
lastSensor = "FILLER"

timeSinceLaunch = 0
temp1 = 0
temp2 = random.randint(0, 9)
temp3 = random.randint(0, 9)
temp4 = random.randint(0, 9)

values = [0]*8
for i in range(8):
    values[i] += i + 1

#Functions for updating the sensors
def updateSensor():
    global temp1
    global temp2, temp3, temp4
    global timeSinceLaunch
    global values
    temp1 += 1
    temp2 = random.randint(0, 9)
    temp3 = random.randint(0, 9)
    temp4 = random.randint(0, 9)
    for i in range(8):
        values[i] += 1
    timeSinceLaunch += 0.5 #Dependent on the refresh rate of the update

#Functions for writing to the file
def FileWrite():
    f = open(filename, "a")
    output = csv.writer(f)
    data = [str(timeSinceLaunch) + "s", str(values[0]), str(values[1]), "...", temp1, temp2, temp3, temp4]
    output.writerow(data)
    f.close()

#Infinite Loop function for updating the GUI output
def update():
    lab1['text'] = time.ctime() + " | Time Since Launch: " + str(timeSinceLaunch) + "s"
    filler['text'] = "-"*80
    pSensor1['text'] = "Pressure Sensor 1: " + str(values[0]) + " PSI"
    pSensor2['text'] = "Pressure Sensor 2: " + str(values[1]) + " PSI"
    pSensor3['text'] = "Pressure Sensor 3: " + str(values[2]) + " PSI"
    pSensor4['text'] = "Pressure Sensor 4: " + str(values[3]) + " PSI"
    pSensor5['text'] = "Pressure Sensor 5: " + str(values[4]) + " PSI"
    pSensor6['text'] = "Pressure Sensor 6: " + str(values[5]) + " PSI"
    pSensor7['text'] = "Pressure Sensor 7: " + str(values[6]) + " PSI"
    pSensor8['text'] = "Pressure Sensor 8: " + str(values[7]) + " PSI"
    filler2['text'] = " "*100
    tSensor1['text'] = "Thermo Sensor 1: " + str(temp1) + " F"
    tSensor2['text'] = "Thermo Sensor 2: " + str(temp2) + " F"
    tSensor3['text'] = "Thermo Sensor 3: " + str(temp3) + " F"
    tSensor4['text'] = "Thermo Sensor 4: " + str(temp4) + " F"
    FileWrite()
    updateSensor()
    root.after(500, update) # run itself again after 500 ms, recursion woooooo

# run first time for recrsive infinite loop
update()

root.mainloop()