# Modules
import tkinter as tk
from datetime import datetime
import utils
import transport

# Weather Imports
import pyowm
from Keys import OWM_api_key

font = "ariel"
background = "black"
fontFamily = "Corbel"
fontStyle = "normal"

degree_sign = u'\N{DEGREE SIGN}'

class Mirror:
    window = tk.Tk()

    width = 1920
    height = 1080

    # Constructor
    def __init__(self):
        print("Mirror Constructor")
        # self.window.overrideredirect(True) # Remove Frame
        self.window.geometry("1920x1080")
        self.window.configure(background="black")

        # Create Labels to define later in their own methods
        self.clockLabel = None
        self.weatherLabel = None
        self.nextDepartureBus = None

    """
    def getTemperature(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "5c694c8c22bb0c291b34809563b2ca1d"
        city_name = "Zurich"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        owm = pyowm.OWM(OWM_api_key)
        manager = owm.weather_manager()
        weather = manager.weather_at_place("Zurich").weather
        dump_dict = weather.to_dict()

        temp_avg_kelvin = dump_dict['temperature']['temp']
        temp_avg_celsius = temp_avg_kelvin - 273.15

        print(temp_avg_celsius)

        return temp_avg_celsius
        """


    def createClock(self):
        color = "white"
        fontSize = 200

        self.clockLabel = tk.Label(self.window, font=(font + str(fontSize)), bg=background, fg=color)
        self.clockLabel.place(x=self.width - 1000, y=self.height - 1000)
        self.clockLabel.configure(font=(fontFamily, fontSize, fontStyle))


    def displayClock(self):
        currentTime = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.clockLabel["text"] = currentTime
        self.window.after(249, self.displayClock)


    def createWeather(self):
        color = "white"
        fontSize = 100

        self.weatherLabel = tk.Label(self.window, font=(font + str(fontSize)), bg=background, fg=color)
        self.weatherLabel.place(x=self.width - 500, y=self.height - 500)
        self.weatherLabel.configure(font=(fontFamily, fontSize, fontStyle))

    """Displays the text to the created weather label
    :returns: Nothing
    """
    def displayWeather(self):
        text = str(utils.getTemperature()) + "\N{DEGREE SIGN}"
        self.weatherLabel["text"] = text
        self.window.after(60000, self.displayWeather)


    def createDepartureBus(self):
        color = "white"
        fontSize = 100

        self.weatherLabel = tk.Label(self.window, font=(font + str(fontSize)), bg=background, fg=color)
        self.weatherLabel.place(x=self.width - 500, y=self.height - 500)
        self.weatherLabel.configure(font=(fontFamily, fontSize, fontStyle))

    def displayDepartureBus(self):
        text = transport.getNextDepartureBus()

