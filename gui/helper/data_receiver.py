"""
    Doc:
        1. 解析 Controller 變成 DAC 資料，並傳回 controller_gui 中的函數負責顯示所有的 DAC 資料
        2. 解析 DAC 變成 sensor 資料，並傳回 controller_gui 中的函數負責顯示一個 DAC 所有的 sensor 資料
"""
from tkinter import *
import tkinter as Tk

# ask redwolf how the data storage format is
class DataReceiver(object):
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
