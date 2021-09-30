
#sab import karke rakhe he in case lage toh
import os
from tkinter import *
import tkinter as tk
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
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

#import matplotlib.pyplot as plt
#import PySimpleGUI as sg

#filter1
def A(a):

     img1=cv2.imread('original.jpg')
     retval,threshold=cv2.threshold(img1,80,255,cv2.THRESH_BINARY)
     cv2.imshow("filter1", threshold)
     img_name = "filter.jpg"
     cv2.imwrite(img_name, threshold)
     print("{} written!".format(img_name))

#filter2

def C(a):
    imgUMat=cv2.imread('original.jpg')
    img_color=cv2.resize(imgUMat,(0,0),fx=0.5,fy=0.5)

    numDown=2
    numBilateralFilters=7
    img_color=imgUMat
    for _ in range(numDown):
        img_color=cv2.pyrDown(img_color)
    for _ in range(numBilateralFilters):
        img_color=cv2.bilateralFilter(img_color,9,9,7)
    for _ in range(numDown):
        img_color=cv2.pyrUp(img_color)
    img_gray=cv2.cvtColor(imgUMat,cv2.COLOR_RGB2GRAY)
    img_blur=cv2.medianBlur(img_gray,7)
    img_edge=cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)
    img_edge=cv2.cvtColor(img_edge,cv2.COLOR_GRAY2RGB)
    print(img_edge.shape)
    imgq=cv2.bitwise_and(imgUMat,img_edge)
    cv2.imshow('img',imgq)
    img_name = "filter4.jpg"
    cv2.imwrite(img_name, img_edge)
    print("{} written!".format(img_name))

#
        

   

    
    cv2.waitKey(12000)
    cv2.destroyAllWindows()



    print("hi")

#filter4     
def D(a):
   
    img=cv2.imread('original.jpg',cv2.IMREAD_COLOR)
    print(img.shape)
    cv2.imshow('img',img)
    bg_gray='C:\\Users\\shree\\Downloads\\download1.jpg'
    img_rgb=cv2.imread('original.jpg',cv2.IMREAD_COLOR)
    imgUMat=cv2.imread('original.jpg',cv2.IMREAD_COLOR)
    imgUMat=cv2.resize(imgUMat,(0,0),fx=0.5,fy=0.5)
    img_gray=cv2.cvtColor(imgUMat,cv2.COLOR_BGR2GRAY)
    #img_gray_inv=255-img_gray
    img_blur=cv2.GaussianBlur(img_gray,(21,21),0,0)
    img_blend=cv2.divide(img_gray,img_blur,scale=256)
    img_blend=cv2.multiply(img_blur,img_blend,scale=1/256)
    rd=cv2.cvtColor(img_blend,cv2.COLOR_GRAY2BGR)
    print(rd.shape)
    cv2.imshow('image',rd)
    img_name = "filter5.jpg"
    cv2.imwrite(img_name, rd)
    print("{} written!".format(img_name))

    cv2.waitKey(12000)
    cv2.destroyAllWindows()


     
#filter5
def E(a):
    
    imgUMat=cv2.imread('original.jpg',cv2.IMREAD_COLOR)
    cv2.imshow('r',imgUMat)
    img_gray=cv2.cvtColor(imgUMat,cv2.COLOR_BGR2GRAY)
    img_gray_inv=255-img_gray
    img_blur=cv2.GaussianBlur(img_gray_inv,ksize=(21,21),sigmaX=0,sigmaY=0)
    def dodgev2(image,mask):
        return cv2.divide(image,255-mask,scale=256)
    def burnv2(image,mask):
        return 255-cv2.divide(255-image,255-mask,scale=256)
    img_blend=dodgev2(img_gray,img_blur)
    img=burnv2(img_gray,img_blur)
    cv2.imshow('o',img_blend)
    img_blend=cv2.multiply(img_blend,img,scale=1/256)
    #cv2.imshow('u',img_blend)
    img_name = "filter6.jpg"
    cv2.imwrite(img_name,img_blend)
    print("{} written!".format(img_name))



    print("hi")
def F(a):
     import cv2
   
     image = cv2.imread('original.jpg')
     hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
      
     cv2.imshow('Original image',image)
     cv2.imshow('HSV image', hsvImage)
     img_name = "filtewr.jpg"
     cv2.imwrite(img_name, hsvImage)
        
     cv2.waitKey(1200)
     cv2.destroyAllWindows()
def R(a):
     img=cv2.imread('original.jpg')
     lap=cv2.Laplacian(img,cv2.CV_64F)
     cv2.imshow('io',img)
     cv2.imshow('ui',lap)
def U(a):
     img=cv2.imread('original.jpg')
     edge=cv2.Canny(img,100,100)
     cv2.imshow('ui',edge)
     

     
def H(a):
#Read the image
     image = cv2.imread("original.jpg")
     #convert to YCrCb color space
     imageYcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

     #convert to float32
     imageYcb =  np.float32(imageYcb)

     #split into channels
     Y, C, B = cv2.split(imageYcb)

     #define scale factor
     alpha = 1.5

     #scale the Y channel
     Y = Y * alpha

     #clip the values betweeen 0 and 255
     Y = np.clip(Y, 0, 255)

     #merge the channels
     imageYcb = cv2.merge([Y, C, B])

     #convert back from float32
     imageYcb = np.uint8(imageYcb)

     #convert back to BGR color space
     result = cv2.cvtColor(imageYcb, cv2.COLOR_YCrCb2BGR)

     #create windows to display images
     cv2.namedWindow("image", cv2.WINDOW_NORMAL)
     cv2.namedWindow("result", cv2.WINDOW_NORMAL)

     #display image
     cv2.imshow("image", image)
     cv2.imshow("result", result)

#press esc to exit the program
     cv2.waitKey(0)

     #close all the opended windows
     cv2.destroyAllWindows()
def K(a):
     

     image = cv2.imread("original.jpg")

     #convert to YCrCb color space
     imageYcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

     #convert to float32
     imageYcb = np.float32(imageYcb)

     #split the channels
     Y, C, B = cv2.split(imageYcb)

     #define offset factor
     beta = 100

     #add offset to the Y channel
     Y = Y + beta

     #clip the values between 0 and 255
     Y= np.clip(Y, 0, 255)

     #merge the channels
     imageYcb = cv2.merge([Y, C, B])

     #convert back from float32
     imageYcb = np.uint8(imageYcb)

     #convert back to BGR color space
     result = cv2.cvtColor(imageYcb, cv2.COLOR_YCrCb2BGR)

     #create windows to display images
     cv2.namedWindow("image", cv2.WINDOW_NORMAL)
     cv2.namedWindow("result", cv2.WINDOW_NORMAL)

     #display images
     cv2.imshow("image", image)
     cv2.imshow("result", result)

     #press esc to exit the program
     cv2.waitKey(0)

     #close all the opened windows
     cv2.destroyAllWindows()


    
    

#aur chahiye toh add karo filters
     

"""  
#aise hi kuch aur filters        
#gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
#retval2,otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)    
"""        
     

     
#main page     
def main():
     root = Tk()
     root.title("Image Filter")
     root.state('zoomed')
     image = ImageTk.PhotoImage(file="bg.png")
     background = tk.Label(root,image=image)
     background.place(x=0,y=0)
     root.configure(bg="#054d5c")

     windowIcon = ImageTk.PhotoImage(file='Logo.png')
     root.iconphoto(False,windowIcon)

     g1 = Label(root, text="Image Filters", fg="midnight blue", font=("times new roman","35","italic"),width=15, height=2)
     g1.place(x=600, y=0)

     l2 = Label(root, text="Choose your filter", fg="black",bg="#8185c7", font=("ComicSan 10 bold", 25))
     l2.place(x=660, y=130)
     l3=Label(root, text="!!! LIFE BLURRY NO WORRY DIVE IN AND ADJUST YOUR FOCUS!!!",fg="black",bg="#8185c7", font=("ComicSan 10 bold", 25))
     l3.place(x=300,y=200)
     
    # f1 = Frame(root, bg="brown", borderwidth=20, relief=SUNKEN)
     #f1.place(x=0, y=0, width=1530, height=800)

     

     b1 = Button(root, text="HSV", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(A,root))
     b1.place(x=600, y=300)
     
     b2 = Button(root, text="Cartooning", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(C,root))
     b2.place(x=850, y=300)

     b3 = Button(root, text="Black And White", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(D,root))
     b3.place(x=700, y=700)

     b4 = Button(root, text="Pencil Sketch", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(E,root))
     b4.place(x=600, y=400)
     
     b5 = Button(root, text="Comic", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(F,root))
     b5.place(x=850, y=400)
     
     b6 = Button(root, text="Contrast", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(H,root))
     b6.place(x=600, y=500)
     
     b7 = Button(root, text="Brightness", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(K,root))
     b7.place(x=850, y=500)
     
     b8 = Button(root, text="Laplacian", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(R,root))
     b8.place(x=600, y=600)
     
     b9 = Button(root, text="Edge", bg="#8185c7", fg="black", overrelief=SUNKEN, font=("ComicSan 10 bold",20),borderwidth=0,command=partial(U,root))
     b9.place(x=850, y=600)
     
     back = Button(root, text="Back", font = ("times new roman","20","italic", "bold"), fg="midnight blue" ,command=partial(Z,root))
     back.pack(anchor='sw', side="bottom")
     

     """
     
     filter3 = Image.open("filter3.png")
     filter3 = filter1.resize((150,200))
     photo3 = ImageTk.PhotoImage(filter3)
     img_label3 = Label(f1, image=photo3)
     img_label3.place(x=558,y=300)
     img_label3.pack_propagate(0)

     filter4 = Image.open("filter4.png")
     filter4 = filter4.resize((150,200))
     photo4 = ImageTk.PhotoImage(filter4)
     img_label4 = Label(f1, image=photo4)
     img_label4.place(x=768,y=300)
     img_label4.pack_propagate(0)

     filter5 = Image.open("filter5.png")
     filter5 = filter5.resize((150,200))
     photo5 = ImageTk.PhotoImage(filter5)
     img_label5 = Label(f1, image=photo5)
     img_label5.place(x=978,y=300)
     img_label5.pack_propagate(0)
     """
     
     root.mainloop()



#camera
cam = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("camera", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "original.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        main()
    def Z(self):
         
         import s
cam.release()
cv2.destroyAllWindows()

#actually mere meh baadmeh camera open nhi ho rha..kuch function not implemented error aa rha he...isliye pehle rkha
#agar aap log meh nhi aa rha aisa kuch toh waise krlo modify




