import numpy as np
import matplotlib.pyplot as plt
import cv2

import os, tkinter, tkinter.filedialog, tkinter.messagebox

root = tkinter.Tk()
root.withdraw()

CamNum = input("Enter Camera number(default:0)\n")



cap = cv2.VideoCapture(int(CamNum))
cap.set(10, 5) #set brightness


while True:

    i = 0
    while (i<15):

        try:
            # VideoCaptureから1フレーム読み込む
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            d = gray.flatten()
            

            n,bins,patches = plt.hist(d,bins = 254, range=(1, 254))

            plt.plot([5,5],[0,n.max()])
            plt.plot([250,250],[0,n.max()])

            print(n[5],n[250])
            plt.pause(0.001)
            plt.cla()
            
            cv2.imshow("raw",gray)
            
            i = i +1

        except KeyboardInterrupt:
            break

    con = tkinter.messagebox.askokcancel('message','continue?')
    #txt = input("Exit -> press 1 key and Enter \nContinue -> press other key and Enter\n")

    if(con == False):
        exit()
    
cap.release()
cv2.destroyAllWindows()