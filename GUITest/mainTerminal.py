import time
import os
from datetime import datetime
import csv
import piplates.THERMOplate as THERMO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

print('Reading Sensor values, press Ctrl-C to quit...')


#Filing Initalization for reading
filename = time.ctime() + ".csv"
f = open(filename, "w")
output = csv.writer(f)

timeSinceLaunch = 0

#data = ["Time Since Launch", "Tank 1", "Tank 2", "n-1 Sensor", "Last Sensor"] example
data = ["Time Since Launch", "Sensor1", "Sensor2", "n-1 Sensor", "Last Sensor"]
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


#Thermo Plates Code
THERMO.setSCALE('f')
#Need to define them before function call or it will throw an error
t1 = THERMO.getTEMP(0,1)
t2 = THERMO.getTemp(0,2)
t3 = THERMO.getTemp(0,3)
t4 = THERMO.getTemp(0,4)


#Functions go before main loop
def FileWrite():
    data = [str(timeSinceLaunch) + "s", values[1], values[2], "...", t1, t2, t3, t4]
    output.writerow(data)


# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    os.system('clear')
    print('Reading Sensor values, press Ctrl-C to quit...')

    #Getting thermocouples Termperature
    t1 = THERMO.getTEMP(0,1)
    t2 = THERMO.getTemp(0,2)
    t3 = THERMO.getTemp(0,3)
    t4 = THERMO.getTemp(0,4)

    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    #print('Current Time | PSensor {0:>4} | PSensor {1:>4} | PSensor {2:>4} | PSensor {3:>4} | PSensor {4:>4} | PSensor {5:>4} | PSensor {6:>4} | PSensor {7:>4} |'.format(*range(8)), "TSensor 1 | TSensor 2 | TSensor 3 | TSensor 4")
    #print(time.ctime(), '| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values), str(t1) + "F | ", str(t2) + "F | ", str(t3) + "F | ", str(t4) + "F")
    # Pause for half a second.
    print(time.ctime(), "| Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("-"*60)
    for i in range(len(values)):
        print("Pressure Sensor", i, ":", values[i])
    print("Temp Sensor 1: ", t1, "F")
    print("Temp Sensor 2: ", t2, "F")
    print("Temp Sensor 3: ", t3, "F")
    print("Temp Sensor 4: ", t4, "F")
    f = open(filename, "a")
    output = csv.writer(f)
    FileWrite()
    timeSinceLaunch += 0.5
    f.close()
    time.sleep(0.5)
