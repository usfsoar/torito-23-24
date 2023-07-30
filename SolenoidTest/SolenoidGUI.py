# This code is meant to be used and imported onto a Raspberry Pi while connected to a solenoid.
# Please see the Electronics Guide to Set up if there are any concerns or confusion in using the code below

from tkinter import *
from tkinter import tkk
import tkinter.font as tkFont
import RPi.GPIO as GPIO

#Setting up GPIO
GPIO.setwarning(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23,0)

#Global strings for later use
openText = "The solenoid is open"
closedText = "The solenoid is closed"

#Functions for buttons
def openSol():
    label.config(text = openText)
    GPIO.output(23, 1)

def closeSol():
    label.config(text = closedText)
    GPIO.output(23, 0)

#GUI Stuff to see when the solenoid is changing states
root = Tk(className = 'Solenoid')
root.geometry("300x200")

label = Label(root, text = "Solenoid is currently closed")
openButton = Button(root, text = "Open", command = openSol)
closeButton = Button(root, text = "Close", command = closeSol)

label.grid(row = 0, column = 0, columnspan = 2. padx = 50, pady = (10, 10))
openButton.grid(row = 1, column = 0, padx = (50, 5))
closeButton.grid(row = 1, column = 1, padx = (5, 50))

root.mainloop()