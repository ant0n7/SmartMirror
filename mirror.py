# Modules
import tkinter as tk
from datetime import datetime
import utils
import transport

# Weather Imports
import pyowm
from Keys import OWM_api_key



degree_sign = u'\N{DEGREE SIGN}'
_yellow = "#fffb80"

class Mirror:
    window = tk.Tk()

    width = 1920
    height = 1080

    # Constructor
    def __init__(self):
        self.font = "ariel"
        self.background = "black"
        self.fontFamily = "Corbel"
        self.fontStyle = "normal"
        self.standard_color = "#fff"

        # self.window.overrideredirect(True) # Remove Frame
        self.window.geometry("1920x1080")
        self.window.configure(background="black")
        # self.window.overrideredirect(True)

        # Create Labels to define later in their own methods
        self.clockLabel = None
        self.weatherLabel = None
        self.nextDepartureBus = None

    #############
    #   CLOCK   #
    #############
    def createClock(self):
        color = self.standard_color
        fontSize = 200

        self.clockLabel = tk.Label(self.window, font=(self.font + str(fontSize)), bg=self.background, fg=color)
        self.clockLabel.place(x=self.width/3, y=self.height - 500)
        self.clockLabel.configure(font=(self.fontFamily, fontSize, self.fontStyle))

    def displayClock(self):
        currentTime = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.clockLabel["text"] = currentTime
        self.window.after(249, self.displayClock)

    ###############
    #   WEATHER   #
    ###############
    def createWeather(self):
        color = _yellow
        fontSize = 100

        self.weatherLabel = tk.Label(self.window, font=(self.font + str(fontSize)), bg=self.background, fg=color)
        self.weatherLabel.place(x=self.width - 200, y=100)
        self.weatherLabel.configure(font=(self.fontFamily, fontSize, self.fontStyle))

    """Displays the text to the created weather label
    :returns: Nothing
    """
    def displayWeather(self):
        text = str(utils.getTemperature()) + "\N{DEGREE SIGN}"
        self.weatherLabel["text"] = text
        self.window.after(60000, self.displayWeather)

    ###########
    #   BUS   #
    ###########
    def createDepartureBus(self):
        color = self.standard_color
        fontSize = 100

        self.nextDepartureBus = tk.Label(self.window, font=(self.font + str(fontSize)), bg=self.background, fg=color)
        self.nextDepartureBus.place(x=100, y=100)
        self.nextDepartureBus.configure(font=(self.fontFamily, fontSize, self.fontStyle))

    def displayDepartureBus(self):
        text = transport.getNextDepartureBusTable()

        self.nextDepartureBus["text"] = text
        self.window.after(18000, self.displayDepartureBus)

    def updateColors(self):
        color_table = {
            "day": "#fff",
            "night": "#949494"
        }

        if datetime.now().hour < 4 or datetime.now().hour >= 23:
            self.standard_color = color_table["night"]
        else:
            self.standard_color = color_table["day"]

        self.clockLabel.configure(color=self.standard_color)
        self.clockLabel.configure(color=self.standard_color)
