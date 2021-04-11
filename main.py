# Frameworks
import tkinter as tk
from mirror import *
import transport


print("Hello World\n")
print(utils.getNextDeparture())
print(transport.getNextDepartureBus())

# Create window
"""
root = tk.Tk()

# Create a new widget
myLabel1 = tk.Label(root, text="10:10")
myLabel2 = tk.Label(root, text="Sa, 3.4.2021")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)

#myLabel1.pack()  # pack it to the screen


root.mainloop()
#7158CC2857755964

##as
"""

myMirror = Mirror()
myMirror.createClock()
myMirror.createWeather()

myMirror.displayClock()
myMirror.displayWeather()

myMirror.window.mainloop()
