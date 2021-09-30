import os
from tkinter import *
from tkinter import filedialog
import tkinter as tk
#import gobject
#import gst
import sqlite3
import random
from tkinter import ttk
import PIL.Image
from PIL import ImageTk
from PIL import ImageGrab
from functools import partial
from tkinter import messagebox as mbox
#from tkcalendar import *
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
from datetime import date
import time
import numpy as np 
import cv2
import winsound
winsound.PlaySound("sound.wav",winsound.SND_LOOP|winsound.SND_ASYNC)

def A(self):
    import s
    try:
        
        self.root1.destroy()
    except:
        pass

root1 = tk.Tk() #creating window
image = ImageTk.PhotoImage(file="bg.png")
background = tk.Label(root1,image=image)
background.place(x=0,y=0)

#window icon
windowIcon = ImageTk.PhotoImage(file='Logo.png')
root1.iconphoto(False,windowIcon)

root1.title("Fine Arts") #window title
root1.geometry('2000x1500') #window size
root1.resizable(True,True) #window can be resized


g1 = Label(root1, text="WElCOME TO", fg="black", bg="#6FA5D9", font=("Lucida console", 40))
g1.place(x=650,y=380)

l2 = Label( root1,text="FINE ARTS", fg="black",bg="#6FA5D9", font=("ComicSan 10 bold", 35))
l2.place(x=700, y=450)

b1 = Button( root1,text="START", bg="black",fg="#6FA5D9", overrelief=SUNKEN, font=("ComicSan 10 bold",30),borderwidth=0,command=partial(A,root1))
b1.place(x=750, y=550)

root1.mainloop()
