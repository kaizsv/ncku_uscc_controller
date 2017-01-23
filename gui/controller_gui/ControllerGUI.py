"""
    Doc:
        generate general button frames
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

# layout the whole block to
class ControllerWindow(tk.Frame):
    # frame type:
    #   0: main frame(self.frame)
    #   1: second frame(self.secondframe)
    #   2: third frame(self.label)
    #   3: self.controllerFrame
    #   4: self.DACFrame
    #   5: self.sensorFrame
    #
    def __init__(self, master):
        setControllerWindow(self, master)

    def setControllerWindow(self, master):
        # path to bg
        tk.Frame.__init__(self, master)
        # tkMessageBox.showinfo("dffsd", "zdfsfds")
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        # master: master window
        self.frame = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # put frame to its parent
        self.frame.pack_propagate(0)
        self.frame.pack(fill=BOTH, expand=YES)
        self.secondframe = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        self.secondframe.pack_propagate(0)
        self.secondframe.pack(fill=BOTH, expand=YES)
        ######################### background image
        self.createBgImageFrame(self.secondframe, bg, x, y)
        self.frameType = 2
        ######################### controller, DAC, sensor data
        self.createControllerFrame(self.secondframe)
        ######################### notice & info button
        ### information frame
        self.createInfoFrame(self.secondframe)
        ######################### go back button
        self.createBackButton(self.secondframe)

    def createBgImageFrame(self, master, bg, x, y):
        self.frameType = 1
        # make a mask
        mask = Image.new('L', bg.size, color=150)
        draw = ImageDraw.Draw(mask)
        draw.rectangle(((x, y), (self.width, self.height)), fill="white", outline="white")
        bg.putalpha(mask)
        self.backgroundImage = ImageTk.PhotoImage(bg)
        self.label = label = Label(master, image=self.backgroundImage)
        label.backgroundImage = self.backgroundImage
        # self.label.pack_propagate(0)
        # place label in frame
        # self.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def createInfoFrame(self, master):
        self.infoFrame = tk.Frame(master, width=self.width/10, height=self.height/10, bg="white", colormap="new")
        self.infoFrame.place(relx=1, rely=0, anchor=NE)
        btbBgImg = Image.open("alarm.jpg")
        self.buttonbgImage = ImageTk.PhotoImage(btbBgImg)
        notificationBtn = Button(self.infoFrame, image=self.buttonbgImage, command=self.alarmEvent, width="25", height="25")
        notificationBtn.pack()
        infoBg = Image.open("info.jpg")
        self.infoBgImage = ImageTk.PhotoImage(infoBg)
        infoButton = Button(self.infoFrame, image=self.infoBgImage, command=lambda: self.infoEvent("Information", "Data collector"), width="25", height="25")
        infoButton.pack(side=BOTTOM)

    def createBackButton(self, master):
        self.backFrame = tk.Frame(master, width=self.width/10, height=self.height/10, bg="white", colormap="new")
        self.backFrame.place(relx=0, rely=0, anchor=NW)
        backBgImg = Image.open("back.jpg")
        self.backImg = ImageTk.PhotoImage(backBgImg)
        backButton = Button(self.backFrame, image=self.backImg, command=self.backEvent, width="25", height="25")
        backButton.pack()

    def createSensorFrame(self, master):
        self.frameType = 5
        self.sensorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.sensorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 1", fg="red", command=self.buttonThreeEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 2", fg="green", command=self.buttonThreeEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 3", fg="blue", command=self.buttonThreeEvent)
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
        self.createSensorFrame(self.secondframe)

    def buttonThreeEvent(self):
        pass
        # self.sensorFrame.destroy()

    def alarmEvent(self):
        tkMessageBox.showinfo("notice", "Actuator is broken")

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
