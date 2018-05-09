from tkinter import *
from support.main import start
import time

win = Tk()
win.title("Protected Qr Generator")
output1 = StringVar()
passw = StringVar()

def show_qr():
    link = start(output1.get(),passw.get())
    photo = PhotoImage(file="qrstore" + "\\" + "qrimage" + ".Bmp")
    label = Label(win,image = photo)
    label.image = photo
    # label.pack()
    label.grid(row=7,column=0)
    w3 = Label(win,text="Or Share The Url Below")
    # w3.pack()
    w3.grid(row=8,column=0)
    w2 = Label(win,text="QR Image Saved !! \qrstore\qrimage.Bmp")
    # w2.pack()
    w2.grid(row=7,column=1)
    text1 = Text(win,height = 1 , width = 40)
    # text1.pack()
    text1.grid(row=9,column=0)
    text1.insert(END,link)

w = Label(win,text="To Store Data In Protected Format")
# w.pack()
w.grid(row=0,column=0)

w1 = Label(win,text="Enter Text Below To Share !")
# w1.pack()
w1.grid(row=1,column=0)

Input_box = Entry(win , textvariable = output1)
# Input_box.pack()
Input_box.grid(row=2,column=0)

w5 = Label(win,text="Type Password Below !")
# w1.pack()
w5.grid(row=3,column=0)

Input_box2 = Entry(win , textvariable = passw)
# Input_box.pack()
Input_box2.grid(row=4,column=0)

button1 = Button(win,text = "Generate", command = show_qr )
# button1.pack()
button1.grid(row=5,column=0)

w2 = Label(win,text="Scan The Qr Below")
# w2.pack()
w2.grid(row=6,column=0)

w3 = Label(win,text="@developed BY Pratik")
# w3.pack()
w3.grid(row=10,column=1)

win.mainloop()
