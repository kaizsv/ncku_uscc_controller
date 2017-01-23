"""
    Doc:
        generate general button frames
"""
from Tkinter import *
import Tkinter as tk
from PIL import Image as Img, ImageTk as ImgTk
from functools import partial

# layout the whole block to
class GuiBlock(tk.Frame):
    def __init__(self, master, frame_width, frame_height):
        # create a new frame
        tk.Frame.__init__(self, master, width=frame_width, heigh=frame_height)
        self.frame = Frame(master)
        i = 0
        while(i < count):
            # add a new button
            buttonText = "controller " + count
            button = tk.Button(self, text=buttonText)
            data[i]

    # update sensor data
    def updateAllData(self):
        allDACData = DR.getDACData()
        allSensorData = DR.getSensorData()

    def drawBasicGUI(self):
        pass

    def close(self):
        # destroy self frame
        self.destroy()
