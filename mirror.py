# Modules
import tkinter as tk
from datetime import datetime

font = "ariel"
background = "black"
fontFamily = "Corbel"
fontStyle = "normal"


class Mirror:
    window = tk.Tk()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "5c694c8c22bb0c291b34809563b2ca1d"
    city_name = "Zurich"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    width = 1920
    height = 1080

    # Constructor
    def __init__(self):
        print("Mirror Constructor")
        # self.window.overrideredirect(True) # Remove Frame
        self.window.geometry("1920x1080")
        self.window.configure(background="black")

        self.clockLabel = None

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
