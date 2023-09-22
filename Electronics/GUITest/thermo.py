#Code for the thermocouples with the plate
# Need to install pi-plates using pip/pip3

import piplates.THERMOplate as THERMO
import time
import os
 
THERMO.setSCALE('f')

while(1):
    #The two tank temperatures would be t1 and t2
    #Nozzle and combution chmaber would be t3 nd t4 respectively
    t1 = THERMO.getTEMP(0,1)
    t2 = THERMO.getTemp(0,2)
    t3 = THERMO.getTemp(0,3)
    t4 = THERMO.getTemp(0,4)
    os.system('clear')
    print (time.ctime(),'Temperature of Tank 1: ',t1)
    print (time.ctime(),'Temperature of Tank 2: ',t2)
    print (time.ctime(),'Temperature of Combution Chmaber: ',t3)
    print (time.ctime(),'Temperature of Nozzle: ',t4)
    time.sleep(1)
    #Time sleep 1 reads the couples once a second