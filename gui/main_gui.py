"""
    Doc:
        1. 此為背景 & 主視窗
        2. 根據有的資料選擇要顯示哪些
"""
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
from controller_gui.controller_gui import GuiBlock as GUI
from helper.data_receiver import DataReceiver as DR


class GuiFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="green")
        self.parent = parent
        self.initGUI()

    def initGUI(self):
        self.parent.title("智慧生活農場")
        self.pack(fill=BOTH, expand=1)


class GuiWindow(tk.Frame):
    # frame type:
    #   0: main frame(self.frame)
    #   1: second frame(self.secondframe)
    #   2: third frame(self.label)
    #   3: self.controllerFrame
    #   4: self.DACFrame
    #   5: self.sensorFrame
    #
    def __init__(self, master):
        # path to bg
        tk.Frame.__init__(self, master)
        self.frameType = 0
        path = "rsz_farm_bg.jpg"
        bg = Image.open(path).convert('RGBA')
        self.width = bg.width
        self.height = bg.height
        x = 0
        y = 0
        # master: master window
        master.geometry("%dx%d+%d+%d" % (self.width, self.height, x, y))
        transparent_area = bg.size
        self.frame = tk.Frame(master, width=self.width, height=self.height, bg="", colormap="new")
        # make frame don't resize
        self.frame.pack_propagate(0)
        # put frame to its parent
        self.frame.pack(fill=BOTH, expand=YES)
        self.secondframe = tk.Frame(self.frame)
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

    def setHeight(self, heightValue):
        self.height = heightValue

    def setWidth(self, widthValue):
        self.width = widthValue

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
        infoButton = Button(self.infoFrame, image=self.infoBgImage, command=lambda: self.infoEvent("Information", "資料收集器"), width="25", height="25")
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
        self.sensorFrame.pack_propagate(0)
        self.sensorFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.sensorFrame, width=15, height=3, text="感測器 1", fg="red", command=self.buttonThreeEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.sensorFrame, width=15, height=3, text="感測器 2", fg="green", command=self.buttonThreeEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.sensorFrame, width=15, height=3, text="感測器 3", fg="blue", command=self.buttonThreeEvent)
        button3.pack(anchor=CENTER, fill=X)

    def createDACFrame(self, master):
        self.frameType = 4
        self.DACFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        self.DACFrame.pack_propagate(0)
        self.DACFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.DACFrame, width=15, height=3, text="即時資料收集器 1", fg="red", command=self.buttonTwoEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.DACFrame, width=15, height=3, text="即時資料收集器 2", fg="green", command=self.buttonTwoEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.DACFrame, width=15, height=3, text="即時資料收集器 3", fg="blue", command=self.buttonTwoEvent)
        button3.pack(anchor=CENTER, fill=X)

###"""還需要能夠傳送資料"""
    def createControllerFrame(self, master):
        self.frameType = 3
        self.controllerFrame = tk.Frame(master, width=self.width/3, height=self.height/3, bg="", colormap="new")
        self.controllerFrame.pack_propagate(0)
        self.controllerFrame.place(relx=.5, rely=.5, anchor=CENTER)
        button1 = Button(self.controllerFrame, width=15, height=3, text="智慧控制器 1", fg="red", command=self.buttonOneEvent)
        button1.pack(anchor=CENTER, fill=X)
        button2 = Button(self.controllerFrame, width=15, height=3, text="智慧控制器 2", fg="green", command=self.buttonOneEvent)
        button2.pack(anchor=CENTER, fill=X)
        button3 = Button(self.controllerFrame, width=15, height=3, text="智慧控制器 3", fg="blue", command=self.buttonOneEvent)
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
        messagebox.showinfo("notice", "灑水器壞掉了！")

    def infoEvent(self, text, data):
        messagebox.showinfo(text, data)

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
            pass


def initializeTkinter():
    # Tkinter window
    top = Tk()
    return top


def main():
    top = initializeTkinter()
    # top.title("IoT Farm")
    app = GuiWindow(master=top)
    app.master.title("智慧生活農場")
    app.mainloop()


if __name__ == "__main__":
    main()
