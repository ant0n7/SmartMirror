import pyowm
from Keys import OWM_api_key
import pySBB
from datetime import datetime

####################################################################
# TRANSPORT API CONSTANTS ##########################################
####################################################################




"""
:returns: current temperature in celsius
"""



def getTemperature():
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

    return round(temp_avg_celsius)


def getNextDeparture():
    currentDateTime = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M")

    entries = pySBB.get_stationboard("Kapfstrasse", limit=2, datetime=currentDateTime)

    print(entries[0])
    connection = pySBB.get_connections("Kapfstrasse", "Klusplatz", limit=2)
    print(connection[0])

    return None
