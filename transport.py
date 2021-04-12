import requests
from datetime import datetime

# Constants
_base_url = "http://transport.opendata.ch/v1/"


def getNextDepartureBus():
    station_name="Zuerich,%20Kapfstrasse"
    # KLUSPLATZ = 8591233

    #station_name = "8591221"
    complete_url = _base_url + "connections?from=" + station_name + "&to=\"Hegibachplatz\"" + "&transportations[]=bus&limit=1"

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

def getNextDepartureBusTable():
    print("timetable")
    station_name = "Zuerich,%20Kapfstrasse"

    complete_url = _base_url + "stationboard?station=" + station_name + "&limit=2"
    response = requests.get(complete_url)
    information = response.json()

    print(information)

    stationboard = information['stationboard']

    bus1 = bus(stationboard, 0)
    bus2 = bus(stationboard, 1)

    print(bus1.delay)
    print(bus1.direction)
    print(bus1.departureString)


    print(bus2.delay)
    print(bus2.direction)
    print(bus2.departureString)
    # stop = bus1['stop']
    # print(stop)

    # print(bus1['to'])

    #connection2 = information[1]
    #print("1: " + connection1)
    #print("2: " + connection2)

    return [bus1.departureString + " +"]



class bus:
    def __init__(self, stationboard, index):
        self.info = stationboard[index]
        self.stop = self.info['stop']

        self.direction = self.info['to']
        self.delay = self.stop['delay']
        self.departureMS = self.stop['departureTimestamp']
        self.departureString = self.millisecondToString()

    def millisecondToString(self):
        departure_datetime = datetime.fromtimestamp(self.departureMS)
        return departure_datetime.strftime("%H:%M")
