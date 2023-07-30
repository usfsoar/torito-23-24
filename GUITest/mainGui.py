from tkinter import *
import time
import sys
from datetime import datetime
import csv
import piplates.THERMOplate as THERMO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

print('Reading Sensor values, press Ctrl-C to quit...')

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
loadCell = Label(root)

#Pack the labels onto the GUI
lab1.pack()
filler.pack()
pSensor1.pack() 
pSensor2.pack() 
pSensor3.pack() 
pSensor4.pack() 
pSensor5.pack() 
pSensor6.pack() 
pSensor7.pack() 
pSensor8.pack()
filler2.pack()
tSensor1.pack()
tSensor2.pack()
tSensor3.pack()
tSensor4.pack()
loadCell.pack()

#Variables for stuff
filename = time.ctime() + ".csv"
f = open(filename, "w")
output = csv.writer(f)

#data = ["Time Since Launch", "Tank 1", "Tank 2", "n-1 Sensor", "Last Sensor"] - example
data = ["Time Since Launch", "Sensor1", "Sensor2", "n-1 Sensor", "Last Sensor", "Load Cell"]
output.writerow(data)

#Pressure Sensors\Conversion
# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


#Load Cell Configuration
#Please see loadCellExample.py for any confusion or calibration that needs to be done
EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(113)

# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#The above line is used to calibrate the load cell to make sure you are getting proper weight
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()

#Variables
timeSinceLaunch = 0

#Pressure sensors
values = [0]*8
for i in range(8):
    values[i] = mcp.read_adc(i)

#Thermo Plates Sensors
#Can change the k in the string to c, f, or k to get the repsective temperature scale
THERMO.setSCALE('k')
#Need to define them before function call or it will throw an error
t1 = THERMO.getTEMP(0,1)
t2 = THERMO.getTemp(0,2)
t3 = THERMO.getTemp(0,3)
t4 = THERMO.getTemp(0,4)

#Inital Load Cell Force
val = hx.get_weight(5)
pounds = val * 0.0022
poundsPerForce = pounds * 32.174049 #Ft/s^2
hx.power_down()
hx.power_up()

#Functions for updating the sensors
def updateSensor():
    global timeSinceLaunch
    global t1
    global t2
    global t3
    global t4
    global values
    timeSinceLaunch += 0.5 #Dependent on the refresh rate of the update
    t1 = THERMO.getTEMP(0,1)
    t2 = THERMO.getTemp(0,2)
    t3 = THERMO.getTemp(0,3)
    t4 = THERMO.getTemp(0,4)
    for i in range(8)
        values[i] = mcp.read_adc(i)

    
    val = hx.get_weight(5)

    #For any confusion prease go to loadCellExample.py
    #CONVERT THE VALUE FROM GRAMS TO LBS THEN FROM LBS TO LBS PER FORCE, thanks future me, also integrate this into the mainGui.py you lazy bum
    pounds = val * 0.0022
    poundsPerForce = pounds * 32.174049 #Ft/s^2

    #If only want positive values then set the line above to val = max(0, int(hx.get_weight(5)))
    #Was print(val) which prints out grams only
    # print(poundsPerForce)

    # To get weight from both channels (if you have load cells hooked up 
    # to both channel A and B), do something like this
    #val_A = hx.get_weight_A(5)
    #val_B = hx.get_weight_B(5)
    #print "A: %s  B: %s" % ( val_A, val_B )

    hx.power_down()
    hx.power_up()

def FileWrite():
    f = open(filename, "a")
    output = csv.writer(f)
    data = [str(timeSinceLaunch) + "s", values[1], values[2], "...", t1, t2, t3, t4, poundsPerForce]
    output.writerow(data)
    f.close()

def update():
    lab1['text'] = time.ctime() + " | Time Since Launch: " + str(timeSinceLaunch) + "s"
    filler['text'] = "-"*100
    pSensor1['text'] = "Pressure Sensor 1: " + str(values[0]) + " PSI"
    pSensor2['text'] = "Pressure Sensor 2: " + str(values[1]) + " PSI"
    pSensor3['text'] = "Pressure Sensor 3: " + str(values[2]) + " PSI"
    pSensor4['text'] = "Pressure Sensor 4: " + str(values[3]) + " PSI"
    pSensor5['text'] = "Pressure Sensor 5: " + str(values[4]) + " PSI"
    pSensor6['text'] = "Pressure Sensor 6: " + str(values[5]) + " PSI"
    pSensor7['text'] = "Pressure Sensor 7: " + str(values[6]) + " PSI"
    pSensor8['text'] = "Pressure Sensor 8: " + str(values[7]) + " PSI"
    filler2['text'] = " "*100
    tSensor1['text'] = "Thermo Sensor 1: " + str(t1) + " F"
    tSensor2['text'] = "Thermo Sensor 2: " + str(t2) + " F"
    tSensor3['text'] = "Thermo Sensor 3: " + str(t3) + " F"
    tSensor4['text'] = "Thermo Sensor 4: " + str(t4) + " F"
    loadCell['text'] = "Load Cell: " + str(poundsPerForce) + "lbs/f"
    FileWrite()
    updateSensor()
    root.after(500, update) # run itself again after 500 ms

# run first time for recrsive infinite loop
update()

root.mainloop()