import requests
from datetime import datetime

# Constants
_base_url = "http://transport.opendata.ch/v1/connections"


def getNextDepartureBus():
    station_name="Zuerich,%20Kapfstrasse"
    # KLUSPLATZ = 8591233

    #station_name = "8591221"
    complete_url = _base_url + "?from=" + station_name + "&to=\"Hegibachplatz\"" + "&transportations[]=bus&limit=1"

    # print(complete_url)

    response = requests.get(complete_url)
    information = response.json()

    # print(information)

    connection = information["connections"]
    departure = connection[0]["from"]
    departure_timestamp = departure["departureTimestamp"]

    # print(connection)
    # print(departure)
    # print(departure_timestamp)

    departure_datetime = datetime.fromtimestamp(departure_timestamp)
    departure_string = departure_datetime.strftime("%H:%M")

    delay = departure["delay"]

    return departure_string + " +" + str(delay)
    # if delay == 0 or delay is None:
    #     return departure_string
    # else:
    #     return departure_string + " +" + str(delay)
