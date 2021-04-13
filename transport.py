import traceback

import requests
from datetime import datetime

# Constants
_base_url = "http://transport.opendata.ch/v1/"


# WARNING: DEPRECATED!
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
    station_name = "Zurich,%20Kapfstrasse"
    limit = 5

    complete_url = _base_url + "stationboard?station=" + station_name + "&limit=" + str(limit)

    try:
        response = requests.get(complete_url)
        information = response.json()

        stationboard = information['stationboard']

        bus_list = []
        for i in range(0, limit):
            bus_list.append(bus(stationboard, i))
    except Exception:
        traceback.print_exc()
        return "Can't connect to \nOpenTransport Server"

    # Filter out all busses that go to Altstetten
    bus_to_city_list = []

    for busx in bus_list:
        if busx.direction == "Zürich Altstetten, Bahnhof" and len(bus_to_city_list) < 2:
            bus_to_city_list.append(busx)

    for bus_to_city in bus_to_city_list:
        print(bus_to_city.departureString)

    try:
        return_string = "Bus " + bus_to_city_list[0].number + " Departures: " + bus_to_city_list[0].departureString
        line2_string = bus_to_city_list[1].departureString
        return_string2 = "\n" + " " * round(len(return_string) * 1.5) + line2_string
        # return_string length = 28 -> number of whitespaces = 1.5x length
        #return return_string + return_string2
        return bus_to_city_list[0].departureString + "\n" + bus_to_city_list[1].departureString
    except IndexError:
        return "Error Processing Data\nNo Timetables available"


class bus:
    def __init__(self, stationboard, index):
        self.info = stationboard[index]
        self.stop = self.info['stop']

        self.direction = self.info['to']
        self.delay = self.stop['delay']
        self.departureMS = self.stop['departureTimestamp']
        self.departureString = self.millisecondToString()
        self.number = self.info['number']

    def millisecondToString(self):
        departure_datetime = datetime.fromtimestamp(self.departureMS)
        departure_string = departure_datetime.strftime("%H:%M")

        if self.delay is None or self.delay == 0:
            return departure_string + " +0\'"
        else:
            return departure_string + " +" + self.delay + "\'"

