from tkinter import *
from PIL import ImageTk,Image
import random
# import time

top = Tk()
top.title('Electrical_Bill')
top.geometry('1200x700')

p = "D:/Python(Gaurav Sir)/GUI/bill.png"
img = ImageTk.PhotoImage(Image.open(p))
l1 = Label(top,image=img)
l1.pack()

def bill_Number():
    global q
    q = random.randint(100000000000000,999999999999999)
    # q = random.randint(1,3)
    l4.config(text=q)
# def copy():
#      l15.config(text=q)
def check():
    global a
    a = int(e1.get())
    if(a==q):
        l6.config(text=": Bill Number is correct")
    else:
        l6.config(text=": Please enter correct Bill Number")
def Total_bill():
        u = int(e2.get())
        # time.sleep(2)
        if(a==q):
            l9.config(text="Your total amount are(Rs.3/unit):-")
            if(u<=100):
                l10.config(text="Free!")
            elif(u>100):
                unit_amt = u*5                  
                gst = unit_amt/100*18          
                total = unit_amt + gst           
                l10.config(text=f"Total unit amount: {unit_amt}")
            # time.sleep(2)
                l11.config(text=f"adding 18% GST = {gst}")
            # time.sleep(2)
                l12.config(text=f"Given unit = {u}")
            # time.sleep(2)
                l13.config(text=f"Total amount = {total}")
            # time.sleep(2)
            l14.config(text="Thank you!")

    

l2=Label(top,text="Electric Bill",fg='red',bg='dark Blue',font=('Arial 25 bold'))
l2.place(x=500,y=10)

l3=Label(top,text="Generate Bill Number",fg='red',bg='dark Blue',font=('Arial 25 bold'))
l3.place(x=10,y=70)
b1=Button(top,text="Click",bg='red',font=('Arial 20 bold'),command=bill_Number)
b1.place(x=120,y=120)
l4=Label(top,fg='Blue',bg='sky blue',font=('Arial 25 bold'))
l4.place(x=50,y=200)

l5=Label(top,text="Enter Bill Number:",fg='red',bg='dark Blue',font=('Arial 25 bold'))
l5.place(x=400,y=200)
e1=Entry(top,fg='Blue',bg='sky blue',font=('Arial 25 bold'))
e1.place(x=730,y=200)
# l15=Label(top,fg='Blue',bg='sky blue',font=('Arial 25 bold'))
# l15.place(x=730,y=200)
# b3=Button(top,text="Copy",bg='red',font=('Arial 20 bold'))
# b3.place(x=750,y=250)
b2=Button(top,text="Check",bg='red',font=('Arial 20 bold'),command=check)
b2.place(x=850,y=250)
l6=Label(top,fg='black',bg='yellow',font=('Arial 10 bold'))
l6.place(x=730,y=310)

l7=Label(top,text="Enter your Unit    :",fg='red',bg='dark Blue',font=('Arial 25 bold'))
l7.place(x=400,y=350)
e2=Entry(top,fg='Blue',bg='sky blue',font=('Arial 25 bold'))
e2.place(x=730,y=350)
l7=Label(top,text="Total Bill:",fg='red',bg='dark Blue',font=('Arial 25 bold'))
l7.place(x=10,y=400)
b3=Button(top,text="Click",fg='black',bg='red',font=('Arial 20 bold'),command=Total_bill)
b3.place(x=30,y=450)

l9=Label(top,fg='Black',bg='white',font=('Arial 10 bold'))
l9.place(x=200,y=450)
l10=Label(top,fg='Black',bg='white',font=('Arial 10 bold'))
l10.place(x=200,y=490)
l11=Label(top,fg='Black',bg='white',font=('Arial 10 bold'))
l11.place(x=200,y=530)
l12=Label(top,fg='Black',bg='white',font=('Arial 10 bold'))
l12.place(x=200,y=570)
l13=Label(top,fg='Black',bg='white',font=('Arial 10 bold'))
l13.place(x=200,y=570)
l14=Label(top,fg='Yellow',bg='Blue',font=('Arial 25 bold'))
l14.place(x=550,y=610)
top.mainloop()
