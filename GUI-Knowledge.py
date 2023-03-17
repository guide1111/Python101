from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk () # นี่คือหน้าจอหลักของโปรแกรม
GUI.title ( 'โปรแกรมบันทึกข้อมูล' ) #นี่คือชื่อโปรแกรม
GUI.geometry ( '500x400' ) #นี่คือขนาดโ)รแกรม


B1 = ttk.Button (GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)


#################
def Button2 () :
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = LabelFrame(GUI,text='Money') # คล้ายกระดาน
FB1.place (x=100,y=80)
B2 = ttk.Button (FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)
#################


def Button3() :
    text = 'Python 101, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB2= LabelFrame(GUI) # คล้ายกระดาน
FB2.place (x=100,y=180)
B3= ttk.Button (FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
