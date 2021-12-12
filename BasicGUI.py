# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.geometry('500x300')
GUI.title('โปรแกรมของลุง')

#file = PhotoImage(file='purepoo.png')
#IMG = Label(GUI,image=file,text='')
#IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวนขี้ไส้เดือน',font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวน',font=('Angsana New',20,))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปลที่ใช้เก็บข้อมูลช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 30
	print('จำนวน', float(quantity) * price)
	cal = float(quantity) * price
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','ขี้ไส้เดือน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal))


B1 = ttk.Button(GUI, text='คำนวน',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

GUI.mainloop()