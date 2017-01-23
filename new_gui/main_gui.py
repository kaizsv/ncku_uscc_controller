#!/user/bin/python
# -*- coding: utf-8 -*-
"""
    Doc:
        1. main window
        2. display data

        frame type:
            0: self.frame
            1: self.secondframe
            2: self.label - backgroundImage
            3: self.mainFrame
            4: self.controllerFrame
            5: self.DACFrame
            6: self.sensorFrame
            7: self.actuatorFrame
            8: self.sensorDataFrame
            9: self.motionFrame
"""
from Tkinter import *
import Tkinter as tk
import tkFont
import tkMessageBox
from PIL import Image, ImageTk, ImageDraw
from controller_gui.ControllerGUI import ControllerWindow
from rule_gui.RuleGUI import RuleWindow
from helper.DataReceiver import Receiver as DR
import rpc_related.rpc_client as RpcClient
import time

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
        self.TID = 5
        self.DID = 1
        self.address = 40005
        self.CID = RpcClient.server_ip
        self.buttonValue = 0
        self.TYPE = 'AW'

    def setMainWindow(self, master, bg, x, y):
        self.secondframe = tk.Frame(master)
        self.secondframe.pack_propagate(0)
        self.secondframe.pack(fill=BOTH, expand=YES)
        self.frameType = 1
        # ######################### background image
        self.createBgImageFrame(self.secondframe, bg, x, y)
        # titleframe
        self.frameType = 3
        self.mainFrame = tk.Frame(master, width=self.width/2, height=self.height/6, bg="", colormap="new")
        self.mainFrame.pack_propagate(0)
        self.mainFrame.place(relx=.5, rely=.2, anchor=CENTER)
        titleLabel = Label(self.mainFrame, text="智慧農場", width=self.width/2, height=self.height/5, fg="green", font=self.helv36)
        titleLabel.pack(anchor=CENTER)
        self.createControllerViewButton(master)
        self.createRuleViewButton(master)

    def setControllerWindow(self, master):
        # path to bg
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        self.frameType = 1
        ### background image
        self.createBgImageFrame(self.secondframe, bg, x, y)
        self.frameType = 2
        ### controller, DAC, sensor data
        self.createControllerFrame(self.secondframe)
        ### notice & info button
        ### information frame
        self.createInfoFrame(self.secondframe)
        ### go back button
        self.createBackButton(self.secondframe)

    def setRuleWindow(self, master):
        # tk.Frame.__init__(self, master)
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width, self.height = bg.size
        x = 0
        y = 0
        self.frameType = 1
        self.createBgImageFrame(self.secondframe, bg, x, y)
        self.frameType = 2
        ######################### controller, DAC, sensor data
        self.createControllerFrame(self.secondframe)
        self.createInfoFrame(self.secondframe)
        ######################### go back button
        self.createBackButton(self.secondframe)

    def createControllerViewButton(self, master):
        self.controllerViewFrame = tk.Frame(master, width=self.width/4, height=self.height/6, bg="", colormap="new")
        self.controllerViewFrame.pack_propagate(0)
        self.controllerViewFrame.place(relx=0.1, rely=0.7, anchor=W)
        self.controllerViewButton = Button(self.controllerViewFrame, text="設備管理", command=self.createControllerWindow, width=self.width/5, height=self.height/6)
        self.controllerViewButton.pack()

    def createRuleViewButton(self, master):
        self.ruleViewFrame = tk.Frame(master, width=self.width/4, height=self.height/6, bg="", colormap="new")
        self.ruleViewFrame.pack_propagate(0)
        self.ruleViewFrame.place(relx=0.9, rely=0.7, anchor=E)
        self.ruleViewButton = Button(self.ruleViewFrame, text="即時控制", command=self.createRuleWindow, width=self.width/5, height=self.height/6)
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
        self.label.place(relx=0.5, rely=0.5, anchor=CENTER)

    def createInfoFrame(self, master):
        self.infoFrame = tk.Frame(master, width=self.width/8, height=self.height/8, bg="white", colormap="new")
        self.infoFrame.place(relx=1, rely=0, anchor=NE)
        btbBgImg = Image.open("alarm.jpg")
        self.buttonbgImage = ImageTk.PhotoImage(btbBgImg)
        notificationBtn = Button(self.infoFrame, image=self.buttonbgImage, command=self.alarmEvent, width="40", height="40")
        notificationBtn.pack()
        infoBg = Image.open("info.jpg")
        self.infoBgImage = ImageTk.PhotoImage(infoBg)
        infoButton = Button(self.infoFrame, image=self.infoBgImage, command=lambda: self.infoEvent("資訊", "自動灑水器"), width="40", height="40")
        infoButton.pack(side=BOTTOM)

    def createBackButton(self, master):
        self.backFrame = tk.Frame(master, width=self.width/8, height=self.height/8, bg="white", colormap="new")
        self.backFrame.place(relx=0, rely=0, anchor=NW)
        backBgImg = Image.open("back.jpg")
        self.backImg = ImageTk.PhotoImage(backBgImg)
        backButton = Button(self.backFrame, image=self.backImg, command=self.backEvent, width="50", height="40")
        backButton.pack()

    def createControllerFrame(self, master):
        self.frameType = 4
        self.controllerFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.controllerFrame.pack_propagate(0)
        self.controllerFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="智慧控制器 1", fg="red", command=self.controllerButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="智慧控制器 2", fg="green", command=self.controllerButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.controllerFrame, width=btnWidth, height=btnHeight, text="智慧控制器 3", fg="blue", command=self.controllerButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createDACFrame(self, master):
        self.frameType = 5
        self.DACFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.DACFrame.pack_propagate(0)
        self.DACFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="即時資料收集器 1", fg="red", command=self.dacButtonEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="即時資料收集器 2", fg="green", command=self.dacButtonEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.DACFrame, width=btnWidth, height=btnHeight, text="即時資料收集器 3", fg="blue", command=self.dacButtonEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createSensorFrame(self, master):
        self.frameType = 6
        self.sensorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.sensorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="環境溫度感測器", fg="blue", command=lambda: self.sensorButtonEvent(0))
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="環境濕度感測器", fg="blue", command=lambda: self.sensorButtonEvent(1))
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="土壤濕度感測器", fg="blue", command=lambda: self.sensorButtonEvent(2))
        button3.pack(anchor=CENTER, fill=X)
        button4 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="土壤濕度感測器", fg="blue", command=lambda: self.sensorButtonEvent(3))
        button4.pack(anchor=CENTER, fill=X)
        button5 = Button(self.sensorFrame, width=btnWidth, height=btnHeight, text="土壤濕度感測器", fg="blue", command=lambda: self.sensorButtonEvent(4))
        button5.pack(anchor=CENTER, fill=X)

    def createActuatorFrame(self, master):
        self.frameType = 7
        self.actuatorFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.actuatorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="灑水器 1", fg="red", command=lambda: self.actuatorButtonEvent(5, 40005))
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="灑水器 2", fg="green", command=lambda: self.actuatorButtonEvent(6, 40006))
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.actuatorFrame, width=btnWidth, height=btnHeight, text="灑水器 3", fg="blue", command=lambda: self.actuatorButtonEvent(7, 40007))
        button3.pack(anchor=CENTER, fill=X)

    def createSensorDataFrame(self, master, sensor_data, tid):
        self.frameType = 8
        newButtonHeight = 4
        self.sensorDataFrame = tk.Frame(master, width=self.width/2, height=self.height/2, bg="", colormap="new")
        self.sensorDataFrame.place(relx=.5, rely=.5, anchor=CENTER)
        # set sensor type with tid
        type_text = self.assignTypeWithTID(tid)
        # unpack sensor data
        label1 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="CID: 192.168.1.15")
        label1.pack(anchor=CENTER, fill=X)
        label2 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="DID: 0")
        label2.pack(anchor=CENTER, fill=X)
        label3 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="Type: " + type_text)
        label3.pack(anchor=CENTER, fill=X)
        label4 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="TID: " + str(tid))
        label4.pack(anchor=CENTER, fill=X)
        label5 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="Address: 4000" + str(tid))
        label5.pack(anchor=CENTER, fill=X)
        label6 = Label(self.sensorDataFrame, width=btnWidth, height=newButtonHeight, text="感測器數值: " + str(sensor_data))
        label6.pack(anchor=CENTER, fill=X)

    def assignTypeWithTID(self, tid):
        if tid == 0:
            return "ST"
        elif tid == 1:
            return "SH"
        elif tid == 2:
            return "SHE"
        elif tid == 3:
            return "SPH"
        else:
            return "SI"

    def createMotionFrame(self, master):
        self.frameType = 9
        self.motionFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        # self.sensorFrame.pack_propagate(0)
        self.motionFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.motionFrame, width=btnWidth, height=btnHeight, text="開", command=self.motionOnEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.motionFrame, width=btnWidth, height=btnHeight, text="關", command=self.motionOffEvent)
        button2.pack(anchor=CENTER, fill=X)

    def motionOffEvent(self):
        self.buttonValue = 0
        # pack data
        data = self.packRpcData()
        # call function to send data
        RpcClient.rpc_send_data(data)

    def motionOnEvent(self):
        self.buttonValue = 1
        data = self.packRpcData()
        RpcClient.rpc_send_data(data)

    def controllerButtonEvent(self):
        # clean canvas and draw new one
        self.controllerFrame.destroy()
        self.createDACFrame(self.secondframe)

    def dacButtonEvent(self):
        self.DACFrame.destroy()
        if (self.isActuator == 0):
            self.DID = 0
            self.createSensorFrame(self.secondframe)
        else:
            self.DID = 1
            self.createActuatorFrame(self.secondframe)

    def sensorButtonEvent(self, tid):
        # get data
        self.TID = tid
        sensor_data = self.receivceRpcData(tid)
        self.sensorFrame.destroy()
        self.createSensorDataFrame(self.secondframe, sensor_data, tid)

    def actuatorButtonEvent(self, tid, actuator_address):
        self.TID = tid
        self.address = actuator_address
        self.actuatorFrame.destroy()
        self.createMotionFrame(self.secondframe)

    def alarmEvent(self):
        tkMessageBox.showinfo("警告", "灑水器壞掉了！")

    def infoEvent(self, text, data):
        tkMessageBox.showinfo(text, data)

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

    def receivceRpcData(self, tid):
        # send request to server and get data back
        sensorData = RpcClient.rpc_get_sensor_data(tid)
        print(sensorData)
        return sensorData

    def packRpcData(self):
        immediate_control = []
        control_data = {
            'condition': None,
            'action': [
                {
                    'actuator': {
                        'CID': self.CID,
                        'DID': self.DID,
                        'TYPE': self.TYPE,
                        'TID': self.TID,
                        'ADDRESS': self.address
                    },
                    'value': self.buttonValue
                }
            ],
            'period': {
                'start_time': '2017-01-22 13:01:00',
                'duration': 0
            },
            'rule_make_time': time.strftime("%Y-%m-%d %H:%M:%S")
        }
        # add data to list
        immediate_control.append(control_data)
        return immediate_control

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
