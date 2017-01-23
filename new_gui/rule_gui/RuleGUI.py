"""

"""
from Tkinter import *
import Tkinter as tk
import tkFont
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
from functools import partial

global btnWidth
global btnHeight
btnWidth = 30
btnHeight = 5

class RuleWindow(tk.Frame):
    # frame type:
    #   0: main frame(self.frame)
    #   1: second frame(self.secondframe)
    #   2: third frame(self.label)
    #   3: self.controllerFrame
    #   4: self.DACFrame
    #   5: self.actuatorFrame
    #   6: master frame
    #
    def __init__(self, master):
        # path to bg
        setRuleWindow(self, master)

    def setRuleWindow(self, master):
        tk.Frame.__init__(self, master)
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        self.frame = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # put frame to its parent
        self.frame.pack(fill=BOTH, expand=YES)
        self.secondframe = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        self.secondframe.pack(fill=BOTH, expand=YES)
        self.createBgImageFrame(self.secondframe, bg, x, y)
        self.frameType = 2
        ######################### controller, DAC, sensor data
        self.createControllerFrame(self.secondframe)
        ######################### go back button
        self.createBackButton(self.secondframe)

    def createRuleBgImageFrame(self, master, bg, x, y):
        self.frameType = 1
        # make a mask
        mask = Image.new('L', bg.size, color=150)
        draw = ImageDraw.Draw(mask)
        draw.rectangle(((x, y), (self.width, self.height)), fill="white", outline="white")
        bg.putalpha(mask)
        self.backgroundImage = ImageTk.PhotoImage(bg)
        self.label = label = Label(master, image=self.backgroundImage)
        label.backgroundImage = self.backgroundImage
        # place label in frame
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def createRuleBackButton(self, master):
        self.backFrame = tk.Frame(master, width=self.width/10, height=self.height/10, bg="white", colormap="new")
        self.backFrame.place(relx=0, rely=0, anchor=NW)
        backBgImg = Image.open("back.jpg")
        self.backImg = ImageTk.PhotoImage(backBgImg)
        backButton = Button(self.backFrame, image=self.backImg, command=self.backEvent, width="25", height="25")
        backButton.pack()

    def createActuatorFrame(self, master):
        self.frameType = 5
        self.actuatorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.actuatorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="Sensor 1", fg="red", command=self.buttonThreeEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="Sensor 2", fg="green", command=self.buttonThreeEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="Sensor 3", fg="blue", command=self.buttonThreeEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createDACFrame(self, master):
        self.frameType = 4
        self.DACFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.DACFrame.pack_propagate(0)
        self.DACFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 1", fg="red", command=self.buttonTwoEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 2", fg="green", command=self.buttonTwoEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 3", fg="blue", command=self.buttonTwoEvent)
        button3.pack(anchor=CENTER, fill=X)

###"""capable of passing data"""
    def createControllerFrame(self, master):
        self.frameType = 3
        self.controllerFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.controllerFrame.pack_propagate(0)
        self.controllerFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 1", fg="red", command=self.buttonOneEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 2", fg="green", command=self.buttonOneEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 3", fg="blue", command=self.buttonOneEvent)
        button3.pack(anchor=CENTER, fill=X)

    def buttonOneEvent(self):
        # clean canvas and draw new one
        self.controllerFrame.destroy()
        self.createDACFrame(self.secondframe)

    def buttonTwoEvent(self):
        self.DACFrame.destroy()
        self.createActuatorFrame(self.secondframe)

    def buttonThreeEvent(self):
        pass

    def alarmEvent(self):
        tkMessageBox.showinfo("notice", "Actuator1 is broken")

    def infoEvent(self, text, data):
        tkMessageBox.showinfo(text, data)

###"""need to be able to go back"""
    def backEvent(self):
        # check frame type
        # actually controller frame should go back to main frame
        if (self.frameType == 4):
            # destroy DACFrame and load controllerFrame
            self.DACFrame.destroy()
            self.createControllerFrame(self.secondframe)
        elif (self.frameType == 5):
            self.sensorFrame.destroy()
            self.createDACFrame(self.secondframe)
        elif (self.frameType == 3):
            pass
        else:
            self.destroy()
