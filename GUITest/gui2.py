from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from datetime import datetime
import time
import csv
import random

#Constants for Sensors
MAX_PRESSURE = 200          # test value for changing color
MAX_TEMPERATURE = 100       # test value for changing color
THRESHOLD_PRESSURE = 100
THRESHOLD_TEMPERATURE = 50

#Main frame for the GUI
root = Tk(className='Sensors')
root['bg'] = 'black'
# root.geometry("1050x500")

# titleFont = tkFont.Font(size=38)
sensFont = tkFont.Font(size=36)

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
loadCell = Label(root)

#Make a grid for the labels onto the GUI
lab1.grid(column=1,row=0, pady=(10,0))
lab1.config(font=(36), fg='white', bg='black')

filler.grid(column=1, row=1, padx=(5,5))
filler.config(font=(36), fg='white', bg='black')

pSensor1.grid(column=0, row=2, padx=(100, 10), pady=(0, 10)) 
pSensor1.config(font=sensFont, fg="green", bg='black')

pSensor2.grid(column=0, row=3, padx=(100, 10), pady=(0, 10)) 
pSensor2.config(font=sensFont, fg="green", bg='black')

pSensor3.grid(column=0, row=4, padx=(100, 10), pady=(0, 10)) 
pSensor3.config(font=sensFont, fg="green", bg='black')

pSensor4.grid(column=0, row=5, padx=(100, 10), pady=(0, 10)) 
pSensor4.config(font=sensFont, fg="green", bg='black')

pSensor5.grid(column=0, row=6, padx=(100, 10), pady=(0, 10)) 
pSensor5.config(font=sensFont, fg="green", bg='black')

pSensor6.grid(column=0, row=7, padx=(100, 10), pady=(0, 10)) 
pSensor6.config(font=sensFont, fg="green", bg='black')

pSensor7.grid(column=0, row=8, padx=(100, 10), pady=(0, 10)) 
pSensor7.config(font=sensFont, fg="green", bg='black')

pSensor8.grid(column=0, row=9, padx=(100, 10), pady=(0, 10))
pSensor8.config(font=sensFont, fg="green", bg='black')

tSensor1.grid(column=2, row=2, padx=(10, 100), pady=(0, 10))
tSensor1.config(font=sensFont, fg="green", bg='black')

tSensor2.grid(column=2, row=3, padx=(10, 100), pady=(0, 10))
tSensor2.config(font=sensFont, fg="green", bg='black')

tSensor3.grid(column=2, row=4, padx=(10, 100), pady=(0, 10))
tSensor3.config(font=sensFont, fg="green", bg='black')

tSensor4.grid(column=2, row=5, padx=(10, 100), pady=(0, 10))
tSensor4.config(font=sensFont, fg="green", bg='black')

#Can change row from 2 to any number until 9 if you want the load cell label to move down
loadCell.grid(column=1, row=2, padx=(10,10), pady=(10,10))
loadCell.config(font=sensFont, fg="green", bg='black')

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

poundsPerForce = 50

values = [0]*8
for i in range(8):
    values[i] += i + 1

img = Image.open("Emergency.jpg")
img = ImageTk.PhotoImage(img)

#Functions for updating the sensors
def updateSensor():
    global temp1
    global temp2, temp3, temp4
    global timeSinceLaunch
    global values
    global poundsPerForce

    temp1 += 10
    temp2 += 100 #random.randint(0, 9)
    temp3 += random.randint(0, 9)
    temp4 += random.randint(0, 9)

    poundsPerForce += random.randint(1,10)
    poundsPerForce -= random.randint(0,9)

    #https://www.cytron.io/tutorial/reading-analog-signal-using-mcp3008-raspberry-pi
    #Fix code to read the output directly into a psi
    for i in range(8):
        values[i] += random.randint(1, 20)
        if(values[i] >= THRESHOLD_PRESSURE and values[i] < MAX_PRESSURE):
            if(i == 0):
                pSensor1.config(font=sensFont, fg="yellow")
            elif(i == 1):
                pSensor2.config(font=sensFont, fg="yellow")
            elif(i == 2):
                pSensor3.config(font=sensFont, fg="yellow")
            elif(i == 3):
                pSensor4.config(font=sensFont, fg="yellow")
            elif(i == 4):
                pSensor5.config(font=sensFont, fg="yellow")
            elif(i == 5):
                pSensor6.config(font=sensFont, fg="yellow")
            elif(i == 6):
                pSensor7.config(font=sensFont, fg="yellow")
            elif(i == 7):
                pSensor8.config(font=sensFont, fg="yellow")
        elif(values[i] >= MAX_PRESSURE):
            if(i == 0):
                pSensor1.config(font=sensFont, fg="red")
            elif(i == 1):
                pSensor2.config(font=sensFont, fg="red")
            elif(i == 2):
                pSensor3.config(font=sensFont, fg="red")
            elif(i == 3):
                pSensor4.config(font=sensFont, fg="red")
            elif(i == 4):
                pSensor5.config(font=sensFont, fg="red")
            elif(i == 5):
                pSensor6.config(font=sensFont, fg="red")
            elif(i == 6):
                pSensor7.config(font=sensFont, fg="red")
            elif(i == 7):
                pSensor8.config(font=sensFont, fg="red")
        if(values[i] < MAX_PRESSURE and values[i] < THRESHOLD_PRESSURE):
            if(i == 0):
                pSensor1.config(font=sensFont, fg="green")
            elif(i == 1):
                pSensor2.config(font=sensFont, fg="green")
            elif(i == 2):
                pSensor3.config(font=sensFont, fg="green")
            elif(i == 3):
                pSensor4.config(font=sensFont, fg="green")
            elif(i == 4):
                pSensor5.config(font=sensFont, fg="green")
            elif(i == 5):
                pSensor6.config(font=sensFont, fg="green")
            elif(i == 6):
                pSensor7.config(font=sensFont, fg="green")
            elif(i == 7):
                pSensor8.config(font=sensFont, fg="green")
            
    if(temp1 >= MAX_TEMPERATURE):
        tSensor1.config(font=sensFont, fg="red")
    if(temp2 >= MAX_TEMPERATURE):
        tSensor2.config(font=sensFont, fg="red")
    if(temp3 >= MAX_TEMPERATURE):
        tSensor3.config(font=sensFont, fg="red")
    if(temp4 >= MAX_TEMPERATURE):
        tSensor4.config(font=sensFont, fg="red")
    if(temp1 >= THRESHOLD_TEMPERATURE and temp1 < MAX_TEMPERATURE):
        tSensor1.config(font=sensFont, fg="yellow")
    if(temp2 >= THRESHOLD_TEMPERATURE and temp2 < MAX_TEMPERATURE):
        tSensor2.config(font=sensFont, fg="yellow")
    if(temp3 >= THRESHOLD_TEMPERATURE and temp3 < MAX_TEMPERATURE):
        tSensor3.config(font=sensFont, fg="yellow")
    if(temp4 >= THRESHOLD_TEMPERATURE and temp4 < MAX_TEMPERATURE):
        tSensor4.config(font=sensFont, fg="yellow")
    if(temp1 < MAX_TEMPERATURE and temp1 < THRESHOLD_TEMPERATURE):
        tSensor1.config(font=sensFont, fg="green")
    if(temp2 < MAX_TEMPERATURE and temp2 < THRESHOLD_TEMPERATURE):
        tSensor2.config(font=sensFont, fg="green")
    if(temp3 < MAX_TEMPERATURE and temp3 < THRESHOLD_TEMPERATURE):
        tSensor3.config(font=sensFont, fg="green")
    if(temp4 < MAX_TEMPERATURE and temp4 < THRESHOLD_TEMPERATURE):
        tSensor4.config(font=sensFont, fg="green")

    timeSinceLaunch += 0.5 #Dependent on the refresh rate of the update
        

def Emergency():
    global img
    win = Toplevel()
    win.wm_title("Emergency")
    l = Label(win, image=img)
    l.pack()

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
    filler['text'] = "-"*90
    pSensor1['text'] = "Pressure Sensor 1: " + str(values[0]) + " PSI"
    pSensor2['text'] = "Pressure Sensor 2: " + str(values[1]) + " PSI"
    pSensor3['text'] = "Pressure Sensor 3: " + str(values[2]) + " PSI"
    pSensor4['text'] = "Pressure Sensor 4: " + str(values[3]) + " PSI"
    pSensor5['text'] = "Pressure Sensor 5: " + str(values[4]) + " PSI"
    pSensor6['text'] = "Pressure Sensor 6: " + str(values[5]) + " PSI"
    pSensor7['text'] = "Pressure Sensor 7: " + str(values[6]) + " PSI"
    pSensor8['text'] = "Pressure Sensor 8: " + str(values[7]) + " PSI"
    tSensor1['text'] = "Thermo Sensor 1: " + str(temp1) + " F"
    tSensor2['text'] = "Thermo Sensor 2: " + str(temp2) + " F"
    tSensor3['text'] = "Thermo Sensor 3: " + str(temp3) + " F"
    tSensor4['text'] = "Thermo Sensor 4: " + str(temp4) + " F"
    loadCell['text'] = "Load Cell: " + str(poundsPerForce) + " lbf"

    FileWrite()
    updateSensor()
    if(values[0] >= MAX_PRESSURE and values[1] >= MAX_PRESSURE and values[2] >= MAX_PRESSURE and values[3] >= MAX_PRESSURE and values[4] >= MAX_PRESSURE and values[5] >= MAX_PRESSURE and values[6] >= MAX_PRESSURE and values[7] >= MAX_PRESSURE and temp1 >= MAX_TEMPERATURE and temp2 >= MAX_TEMPERATURE and temp3 >= MAX_TEMPERATURE and temp4 >= MAX_TEMPERATURE):
        Emergency()
    else:
        root.after(500, update) # run itself again after 500 ms, recursion woooooo

# run first time for recrsive infinite loop
update()

root.mainloop()