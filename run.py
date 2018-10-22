import numpy as np
import matplotlib.pyplot as plt
import cv2

import os, tkinter, tkinter.filedialog, tkinter.messagebox


#global CamNum = 0


root = tkinter.Tk()
root.geometry('150x100')
txt = tkinter.Entry(width = 2)
txt.place(x=30, y=43)
txt.insert(tkinter.END,"0")

txt2 = tkinter.Entry(width = 3)
txt2.place(x=30, y=5)
txt2.insert(tkinter.END,"1.0")

lbl = tkinter.Label(text='Movie Scale')
lbl.place(x=60, y=5)


lbl2 = tkinter.Label(text='Camera Number')
lbl2.place(x=50, y=43)



def button1_clicked():
    global CamNum
    global Scale
    CamNum = txt.get()
    Scale = txt2.get()
    Scale = float(Scale)
    root.destroy()

button1 = tkinter.Button(root, text='Enter', command=button1_clicked)
button1.place(x=30, y=60)

root.mainloop()





cap = cv2.VideoCapture(int(CamNum))


while True:

    r = 0
    while (r < 15):

        try:
            # VideoCaptureから1フレーム読み込む
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            
            
            height = gray.shape[0]
            width =gray.shape[1]
            gray = cv2.resize(gray,(int(width/Scale),int(height/Scale)))
           
            d = gray.flatten()
           
            

            n,bins,patches = plt.hist(d,bins = 258, range=(-1, 256))
            size = np.size(d)
            v_5 = size*0.05

            i = 0
            j = 255
            sum = 0
            sum2 = 0

            v_5_pole = 0
            v_95_pole = 0

            while(True):
                if(sum > v_5):
                    v_5_pole = i
                    break
                sum = sum + n[i]
                i = i + 1


            while(True):
                if(sum2 > v_5):
                    v_95_pole = j
                    break
                sum2 = sum2 + n[j]
                j = j - 1
            
            print("5% = ",v_5_pole, "95% = ", v_95_pole)

            plt.plot([v_5_pole,v_5_pole],[0,n.max()])
            plt.plot([v_95_pole,v_95_pole],[0,n.max()])
            
           
            
            plt.pause(0.0001)
            plt.cla()
            
            cv2.imshow("raw",gray)
            
            r = r + 1


        except:
            err = tkinter.messagebox.showerror('error','cannot connect')
            if(err == 'ok'):
                exit()

   

    con = tkinter.messagebox.askquestion('message','continue?')
    if(con == 'no'):
        exit()
       
cap.release()
cv2.destroyAllWindows()
