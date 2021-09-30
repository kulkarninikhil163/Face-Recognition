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

def A(a):
    from PIL import Image
    import PIL
    import numpy as np
    global my_video
    root.filename=filedialog.askopenfilename(initialdir="/Desktop/",title="Select",filetypes=(("avi files","*.avi"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    imgUMat=Image.open(root.filename)
    my_video1=ImageTk.PhotoImage(imgUMat)
    my_video_label=Label(image=my_video1).pack()
    #img1=(my_video)

    grayscaled=cv2.cvtColor(my_video1,cv2.COLOR_BGR2GRAY)
    grayscaled.show()


                                             
def B(a):
    cap=cv2.VideoCapture(0)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    outu=cv2.VideoWriter('outu.avi',fourcc,21.0,(659,490))
    while True:
        
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('frame1',frame1)
        frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #img_gray_inv=255-img_gray
        img_blur=cv2.GaussianBlur(img_gray,(21,21),0,0)
        img_blend=cv2.divide(img_gray,img_blur,scale=256)
        img_blend=cv2.multiply(img_blur,img_blend,scale=1/256)
        rd=cv2.cvtColor(img_blend,cv2.COLOR_GRAY2BGR)
        #print(rd.shape)
        outu.write(rd)
        cv2.imshow('image',rd)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def D(a):
    from PIL import Image 
    import PIL
    root.filename=filedialog.askopenfilename(initialdir="/Desktop/",title="Select",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    my_video=Image.open(root.filename)
    my=ImageTk.PhotoImage(my_video)
    my_video_label=Label(image=my).pack()


    # creating a image object (main image) 
    #im1 = Image.open("C:\\Users\\shree\\Downloads\\11.png") 

    # rotating a image 90 deg counter clockwise 
    my = my_video.rotate(30, PIL.Image.NEAREST, expand = 1) 

    # to show specified image 
    my.show() 

def E(a):
    # Improting Image class from PIL module 
    from PIL import Image
    root.filename=filedialog.askopenfilename(initialdir="/Desktop/",title="Select",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    my_video=Image.open(root.filename)
    my=ImageTk.PhotoImage(my_video)
    my_video_label=Label(image=my).pack()

      
    # Opens a image in RGB mode 
    #im = Image.open("C:\\Users\\shree\\Downloads\\11.png") 
      
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = my_video.size
    print(my_video.size)

    # Setting the points for cropped image 
    left = 5
    top = height / 4
    right = 164
    bottom = 3 * height / 4
      
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    my_video = my_video.crop((left, top, right, bottom)) 
      
    # Shows the image in image viewer 
    my_video.show()
def F(a):
    # import image module from pillow 
    from PIL import Image
    root.filename=filedialog.askopenfilename(initialdir="/Desktop/",title="Select",filetypes=(("PNG files","*.PNG"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    my_video=Image.open(root.filename)
    my=ImageTk.PhotoImage(my_video)
    my_video_label=Label(image=my).pack()


    # open the image C:\\Users\\shree\\Downloads\\11.png
    #my_video = Image.open(root.filename)
    my_video.show()

    # make a copy the image so that the 
    # original image does not get affected 
    Image1copy = my_video.copy() 
    Image2 = Image.open(root.filename)
    me=ImageTk.PhotoImage(Image2)

    
    Image2copy = Image2.copy()
    

    # paste image giving dimensions 
    Image1copy.paste(Image2copy, (0, 0)) 

    # save the image 
    Image1copy.save("C://Users//shree//Desktop//project//16.png")
    Image1copy.show()
def S(a):
    from PIL import Image
    root.filename=filedialog.askopenfilename(initialdir="/Desktop/",title="Select",filetypes=(("MP4 files","*.MP4"),("all files","*.*")))
    my_label=Label(root,text=root.filename).pack()
    #my_video=Video.open(root.filename)
    #my_video_label=Label(image=my_video).pack()

    cap=cv2.VideoCapture(root.filename)
    fgbg=cv2.createBackgroundSubtractorMOG2()
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    outu=cv2.VideoWriter('best.avi',fourcc,21.0,(659,490))
    while True:
        
        ret,frame=cap.read()
        fgmask=fgbg.apply(frame)
        cv2.imshow('io',frame)
        cv2.imshow('oo',fgmask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
def X(a):
    import faces
    


def C(a):
    import anu
    try:
        root.destroy
    except:
        pass
    #root.destroy()
    

root = tk.Toplevel()
root.title("IMAGE FILTER")
root.state('zoomed')
image = ImageTk.PhotoImage(file="bg.png")
background = tk.Label(root,image=image)
background.place(x=0,y=0)
root.configure(bg="#054d5c")


#f2 = Frame(root,  borderwidth=20, relief=SUNKEN)
#f2.pack(side="top",fill="both",expand=True)
def opt(a):
    
    menuu = Menu(root)
    root.config(menu=menuu)
   
    
   
    file_menu=Menu(menuu)
    file_menu.config(bg="#93accc")
    file_menu.configure(font=("Verdana",25))
    menuu.add_cascade(label="FILE",font=("Italic",30),menu=file_menu)
    file_menu.add_command(label="Crop",command=partial(E,root))
    file_menu.add_separator()
    file_menu.add_command(label="CopyAndPaste",command=partial(F,root))
    file_menu.add_separator()
    file_menu.add_command(label="Rotate",command=partial(D,root))
    

    edit_menu=Menu(menuu)
    edit_menu.config(bg="#93accc")
    edit_menu.configure(font=("Verdana",25))
    menuu.add_cascade(label="VIDEO FILTERINGS",menu=edit_menu)
    edit_menu.add_command(label="ORIGINAL TO GRAY",command=partial(B,root))
    edit_menu.add_separator()
   
def Z(self):
    import welcome
    try:
        
        self.root.destroy()
    except:
        pass

head = Label(root,text = 'EXPLORE!!!',font = ("times new roman","40","italic"),pady = 50,fg="midnight blue")
head.place(x=650,y=0)

options=Button( root,text="OPTION MENU", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(opt,root))
options.place(x=700, y=250)

b1 = Button(root,text="Select pic to modify", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(A,root))
b1.place(x=680, y=350)

b2 = Button(root, text="Next for applying filters", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(C,root))
b2.place(x=670, y=450)

b3 = Button(root, text="Background Reduction In Video", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(S,root))
b3.place(x=640, y=550)

b4 = Button( root,text="Detect Yourself!", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(X,root))
b4.place(x=700, y=650)

back = Button(root, text="Back", font = ("times new roman","20","italic", "bold"), fg="midnight blue" ,command=partial(Z,root))
back.pack(anchor='sw', side="bottom")
root.mainloop()



cv2.waitKey(1200)
cv2.destroyAllWindows()
