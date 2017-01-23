from tkinter import *
from PIL import ImageTk, Image

root = Tk()
b = Button(root, justify=LEFT)
img = Image.open("alarm.jpg")

photo = ImageTk.PhotoImage(img)
b.config(image = photo, width = "120", height = "100")
b.pack(side = LEFT)
root.mainloop()
