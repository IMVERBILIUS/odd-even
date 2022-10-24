from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  
import math

pi=math.pi
win=Tk()
win.title('simple INCREMENT & DECREMENT')
main=Frame(win)
win.geometry("1200x550")


def forget():
        for i in options:
                if clicked.get() == 'cone':
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        b.place_forget()
                        wlabel.place_forget()
                        mylabelq.place_forget()
                        mylabels.place_forget()
                        

                else:
                        myButton1['state'] = NORMAL
                        a.place_forget()
                        myDel2.place_forget()
                        myButton23.place_forget()
                        mylabel.place_forget()
                        wlabel.place_forget()
                        


def cal_inc():
       global wlabel
       t1=int(a.get())
       
       
       myButton23['state'] = DISABLED
       
       
       for n in range(t1,64):
               if n%2==0 and t1>0:
                   wlabel=Label(win, text=n)
                   wlabel.pack(side=RIGHT)
                    
                        
                   
       

def cal_dec():
       global wlabel
       t1=int(a.get())
       myButton23['state'] = DISABLED
       
       for n in range(t1,64):
               if n%2!=0 and t1>0:
                   wlabel=Label(win, text=n)
                   wlabel.pack(side=RIGHT)
       

               
       
       
def myDel():
    global wlabel
    wlabel.pack_forget()
    myButton23['state'] = NORMAL      

           
def show():
    global a
    global myButton23
    global wlabel
    global myDel2
    global mylabel


         
    for i in options:
        if  clicked.get() == 'Odd':
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="INCREMENT")
                mylabel.place(x=305, y=99)
                a=Entry(win, width=29)
                a.place(x=275, y=115)
                myDel2 = Button(win, text="CLEAR INCREMENT", command=myDel)
                myDel2.place(x=210, y=178)
                myButton23 = Button(win,width=18, text="calculate", command=cal_inc , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")

                break    
                
        else:
                myButton1['state'] = DISABLED
                mylabel = Label(win, text="Even Number")
                mylabel.place(x=305, y=125)
                a=Entry(win, width=29)
                a.place(x=275, y=155)
                myDel2 = Button(win, text="CLEAR Decrement", command=myDel)
                myDel2.place(x=210, y=178)
                myButton23 = Button(win,width=18, text="calculate", command=cal_dec , bg="red", fg="white")
                myButton23.place(x=375, y=178)
                wlabel = Label(win, text="")
                break
                
            

            

options =[
    "Odd",
    "Even",
    ]

clicked = StringVar()
clicked.set(options[0])
Label(win, text="Enter Number", font=('Calibri 10'), bg="yellow", fg="black").place(x=315, y=5)
drop = ttk.Combobox(win, width = 27, textvariable = clicked, value=options)
drop.place(x=265, y=35)





myButton1 = Button(win, text="Show Selection", bg="red", fg="white", command=show)
myButton1.place(x=265, y=61)
myButton2 = Button(win,width=11, text="delete con", bg="pink", fg="white", command=forget)
myButton2.place(x=365, y=61)
exit_button = Button(win,width=5, text="Exit",bg="red", command=win.destroy)
exit_button.place(x=485, y=35)


win.mainloop()
