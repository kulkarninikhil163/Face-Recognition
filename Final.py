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

    grayscaled=cv2.cvtColor(np.float32(my_video1),cv2.COLOR_BGR2GRAY)
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
    

root = Tk()
root.title("Image Filter")
root.state('zoomed')
root.configure(bg="grey50")
f2 = Frame(root, bg="coral", borderwidth=20, relief=SUNKEN)
f2.place(x=0, y=0, width=1530, height=800)
b1 = Button(f2, text="Select pic to modify", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(A,root))
b1.place(x=200, y=300)
b2 = Button(f2, text="Video", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(B,root))
b2.place(x=00, y=300)
b3 = Button(f2, text="Next for applying filters", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(C,root))
b3.place(x=500, y=300)
b4 = Button(f2, text="Rotate", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(D,root))
b4.place(x=800, y=500)
b5 = Button(f2, text="Crop", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(E,root))
b5.place(x=1000, y=500)
b6 = Button(f2, text="CopyAndPaste", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(F,root))
b6.place(x=200, y=500)
b6 = Button(f2, text="BackgroundReductionInVideo", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(S,root))
b6.place(x=400, y=200)
b6 = Button(f2, text="Detect", bg="brown", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(X,root))
b6.place(x=400, y=400)
root.mainloop()



cv2.waitKey(1200)
cv2.destroyAllWindows()
