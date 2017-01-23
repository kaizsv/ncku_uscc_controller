"""
    Doc:
"""
from Tkinter import *
import Tkinter as Tk

# ask redwolf how the data storage format is
class Receiver(object):
    # parse data here and abstract DACs and Sensors
    def __init__(self, dataObj):
        parseAllData(dataobj)

    def parseAllData(self, dataObj):
        self.dacData = parseControllerData(dataObj)
        self.sensorData = parseDACData(self.dacData)

    def parseControllerData(self, dataObj):
        # parse controller data into DAC data
        dacData = 0
        return dacData

    def parseDACData(self, dacData):
        # parse dac data
        # sensor = parsing
        sensor = 0
        return sensor

    def getDACData():
        return self.dacData

    def getSensorData():
        return self.sensorData
