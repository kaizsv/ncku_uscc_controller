#!/user/bin/python
# -*- coding: utf-8 -*-
"""
    Doc:
        1. main window
		2. display data
"""
from Tkinter import *
import Tkinter as tk
import tkFont
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
from controller_gui.ControllerGUI import ControllerWindow
from rule_gui.RuleGUI import RuleWindow
from helper.DataReceiver import Receiver as DR

global btnWidth
global btnHeight
btnWidth = 30
btnHeight = 5
global top
top = Tk()

class GuiFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="green")
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("Farm")
        self.pack(fill=BOTH, expand=1)


class MainWindow(tk.Frame):
    # frame type:
    #   0: self.frame
    #   1: self.secondframe
    #   2: self.label - backgroundImage
    #   3: self.mainFrame
    #   4: self.controllerFrame
    #   5: self.DACFrame
    #   6: self.sensorFrame
    #   7: self.actuatorFrame
    #   8: self.sensorDataFrame
    #   9: self.motionFrame
    #
    def __init__(self, master):
        self.isActuator = 0
        self.helv36 = tkFont.Font(family="Helvetica",size=36,weight="bold")
        # path to bg
        tk.Frame.__init__(self, master)
        self.master = master
        path = "rsz_farm_bg.jpg"
        self.bg = bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        # self.height = bg.height
        x = 0
        y = 0
        # master: master window
        master.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))
        transparent_area = bg.size
        self.frame = tk.Frame(self.master, width=self.width, height=self.height, bg="", colormap="new")
        # make frame don't resize
        self.frame.pack_propagate(0)
        # put frame to its parent
        self.frame.pack(fill=BOTH, expand=YES)
        self.frameType = 0
        # self.createControllerViewButton(self.secondframe)
        ### test create two button frame
        self.setMainWindow(self.frame, self.bg, x, y)

    def setMainWindow(self, master, bg, x, y):
        self.secondframe = tk.Frame(master)
        self.secondframe.pack_propagate(0)
        self.secondframe.pack(fill=BOTH, expand=YES)
        self.frameType = 1
        # self.thirdFrame = tk.Frame(self.secondframe)
        # self.thirdFrame.pack_propagate(0)
        # self.thirdFrame.pack(fill=BOTH, expand=YES)
        # ######################### background image
        self.createBgImageFrame(self.secondframe, bg, x, y)
        # titleframe
        self.frameType = 3
        self.mainFrame = tk.Frame(master, width=self.width/2, height=self.height/6, bg="", colormap="new")
        self.mainFrame.pack_propagate(0)
        self.mainFrame.place(relx=.5, rely=.2, anchor=CENTER)
        titleLabel = Label(self.mainFrame, text="歡迎光臨智慧農場!", width=self.width/2, height=self.height/5, fg="green", font=self.helv36)
        titleLabel.pack(anchor=CENTER)
        self.createControllerViewButton(master)
        self.createRuleViewButton(master)

    def setControllerWindow(self, master):
        # path to bg
        # tk.Frame.__init__(self, master)
        # tkMessageBox.showinfo("dffsd", "zdfsfds")
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        # self.secondframe = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # self.secondframe.pack_propagate(0)
        # self.secondframe.pack(fill=BOTH, expand=YES)
        self.frameType = 1
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

    def setRuleWindow(self, master):
        # tk.Frame.__init__(self, master)
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        # self.frame = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # put frame to its parent
        # self.frame.pack(fill=BOTH, expand=YES)
        # self.secondframe = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # self.secondframe.pack_propagate(0)
        # self.secondframe.pack(fill=BOTH, expand=YES)
        self.frameType = 1
        self.createBgImageFrame(self.secondframe, bg, x, y)
        self.frameType = 2
        ######################### controller, DAC, sensor data
        self.createControllerFrame(self.secondframe)
        self.createInfoFrame(self.secondframe)
        ######################### go back button
        self.createBackButton(self.secondframe)

    def createControllerViewButton(self, master):
        self.controllerViewFrame = tk.Frame(master, width=self.width/3, height=self.height/5, bg="", colormap="new")
        self.controllerViewFrame.pack_propagate(0)
        self.controllerViewFrame.place(relx=0.1, rely=0.5, anchor=W)
        self.controllerViewButton = Button(self.controllerViewFrame, text="設備管理", command=self.createControllerWindow, width=self.width/3, height=self.height/5, bg="red")
        self.controllerViewButton.pack()

    def createRuleViewButton(self, master):
        self.ruleViewFrame = tk.Frame(master, width=self.width/3, height=self.height/5, bg="", colormap="new")
        self.ruleViewFrame.pack_propagate(0)
        self.ruleViewFrame.place(relx=0.9, rely=0.5, anchor=E)
        self.ruleViewButton = Button(self.ruleViewFrame, text="即時控制", command=self.createRuleWindow, width=self.width/3, height=self.height/5, bg="red")
        self.ruleViewButton.pack()

    # controllerViewButton events - create controller window
    def createControllerWindow(self):
        # clean currentwindow
        # self.secondframe.destroy()
        self.controllerViewFrame.destroy()
        self.mainFrame.destroy()
        self.ruleViewFrame.destroy()
        # TODO: create controller window
        # controllerWindow = ControllerWindow(self.secondframe)
        self.isActuator = 0
        self.setControllerWindow(self.frame)

    def createRuleWindow(self):
        # self.secondframe.destroy()
        self.controllerViewFrame.destroy()
        self.mainFrame.destroy()
        self.ruleViewFrame.destroy()
        # TODO: create rule window
        # ruleWindow = RuleWindow(master)
        self.isActuator = 1
        self.setRuleWindow(self.frame)

    def createBgImageFrame(self, master, bg, x, y):
        self.frameType = 2
        # make a mask
        mask = Image.new('L', bg.size, color=150)
        draw = ImageDraw.Draw(mask)
        draw.rectangle(((x, y), (self.width, self.height)), fill="white", outline="white")
        bg.putalpha(mask)
        self.backgroundImage = ImageTk.PhotoImage(bg)
        self.label = label = Label(master, image=self.backgroundImage)
        label.backgroundImage = self.backgroundImage
        self.label.pack_propagate(0)
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

    def createControllerFrame(self, master):
        self.frameType = 4
        self.controllerFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.controllerFrame.pack_propagate(0)
        self.controllerFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 1", fg="red", command=self.controllerButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 2", fg="green", command=self.controllerButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="Intelligent Controller 3", fg="blue", command=self.controllerButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createDACFrame(self, master):
        self.frameType = 5
        self.DACFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.DACFrame.pack_propagate(0)
        self.DACFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 1", fg="red", command=self.dacButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 2", fg="green", command=self.dacButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="Real time data collector 3", fg="blue", command=self.dacButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createSensorFrame(self, master):
        self.frameType = 6
        self.sensorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.sensorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 1", fg="red", command=self.sensorButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 2", fg="green", command=self.sensorButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="Sensor 3", fg="blue", command=self.sensorButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createActuatorFrame(self, master):
        self.frameType = 7
        self.actuatorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.actuatorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="自動灑水器", fg="red", command=self.actuatorButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="澆灌開關", fg="green", command=self.actuatorButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="太陽光遮罩", fg="blue", command=self.actuatorButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createSensorDataFrame(self, master):
        self.frameType = 8
        self.sensorDataFrame = tk.Frame(master, width=self.width/2, height=self.height/2, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.sensorDataFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Label(self.sensorDataFrame, width=btnWidth, height=btnHeight, text="CID: 140.116.82.0")
        button1.pack(anchor=CENTER, fill=X)
        button2 = Label(self.sensorDataFrame, width=btnWidth, height=btnHeight, text="DID: 2")
        button2.pack(anchor=CENTER, fill=X)
        button3 = Label(self.sensorDataFrame, width=btnWidth, height=btnHeight, text="Type: ST")
        button3.pack(anchor=CENTER, fill=X)
        button4 = Label(self.sensorDataFrame, width=btnWidth, height=btnHeight, text="TID: 23")
        button4.pack(anchor=CENTER, fill=X)
        button5 = Label(self.sensorDataFrame, width=btnWidth, height=btnHeight, text="Address: 40002")
        button5.pack(anchor=CENTER, fill=X)

    def createMotionFrame(self, master):
        self.frameType = 9
        self.motionFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.motionFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.motionFrame, width=btnWidth, height=btnHeight, text="開", command=self.motionEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.motionFrame, width=btnWidth, height=btnHeight, text="關", command=self.motionEvent)
        button2.pack(anchor=CENTER, fill=X)

    def motionEvent(self):
        pass

    def controllerButtonEvent(self):
        # clean canvas and draw new one
        self.controllerFrame.destroy()
        self.createDACFrame(self.secondframe)

    def dacButtonEvent(self):
        self.DACFrame.destroy()
        if (self.isActuator == 0):
            self.createSensorFrame(self.secondframe)
        else:
            self.createActuatorFrame(self.secondframe)

    def sensorButtonEvent(self):
        self.sensorFrame.destroy()
        self.createSensorDataFrame(self.secondframe)

    def actuatorButtonEvent(self):
        self.actuatorFrame.destroy()
        self.createMotionFrame(self.secondframe)

    def alarmEvent(self):
        tkMessageBox.showinfo("notice", "Actuator is broken")

    def infoEvent(self, text, data):
        tkMessageBox.showinfo(text, data)

###"""need to be able to go back"""
    def backEvent(self):
        # check frame type
        # actually controller frame should go back to main frame
        if (self.frameType == 5):
            # destroy DACFrame and load controllerFrame
            self.DACFrame.destroy()
            self.createControllerFrame(self.secondframe)
        elif (self.frameType == 6):
            # destroy sensor frame, create DAC frame
            self.sensorFrame.destroy()
            self.createDACFrame(self.secondframe)
        elif (self.frameType == 7):
            # destroy actuator frame, create DAC frame
            self.actuatorFrame.destroy()
            self.createDACFrame(self.secondframe)
        elif (self.frameType == 4):
            # at controller frame, delete controller frame, info frame, back frame
            self.controllerFrame.destroy()
            self.infoFrame.destroy()
            self.backFrame.destroy()
            # create MainWindow
            self.setMainWindow(self.secondframe, self.bg, 0, 0)
        elif (self.frameType == 8):
            self.sensorDataFrame.destroy()
            self.createSensorFrame(self.secondframe)
        elif (self.frameType == 9):
            self.motionFrame.destroy()
            self.createActuatorFrame(self.secondframe)
        else:
            pass

def main():
    # global top
    # top = Tk()
    # top.title("IoT Farm")
    app = MainWindow(master=top)
    app.master.title("Intelligent Farm")
    # use app.secondframe as the window to display all other frames ?
    app.mainloop()


if __name__ == "__main__":
    main()
