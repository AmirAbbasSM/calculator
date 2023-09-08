from tkinter import *
import tkinter as tk


root = Tk()
root.title('Calculator')
root.geometry('376x570')

# def section
def equal():
    input_1 = Entry_1.get()
    try:
        Answer = round(eval(input_1),5)
        
    except:
        Answer = 'Error in writing'

    Entry_1.delete(0,tk.END)
    Entry_1.insert(0,Answer)


def delet():
    Entry_1.delete(0,tk.END)

def clean():
    text_Entry = Entry_1.get()
    if text_Entry:
        new_text = text_Entry[:-1]
        Entry_1.delete(0,tk.END)
        Entry_1.insert(0,new_text)

def number_decimal_point():
    Entry_1.insert(tk.END,'.')

def plus_sign():
    Entry_1.insert(tk.END,'+')

def minus_sign():
    Entry_1.insert(tk.END,'-')

def times_sign():
    Entry_1.insert(tk.END,'*')

def division_sign():
    Entry_1.insert(tk.END,'/')

def power():
    Entry_1.insert(tk.END,'**')

def square_root():
    Entry_1.insert(tk.END,'**0.5')

#   __def_button_Number__   
def number_1():
    Entry_1.insert(tk.END,1)

def number_2():
    Entry_1.insert(tk.END,2)

def number_3():
    Entry_1.insert(tk.END,3)

def number_4():
    Entry_1.insert(tk.END,4)

def number_5():
    Entry_1.insert(tk.END,5)

def number_6():
    Entry_1.insert(tk.END,6)

def number_7():
    Entry_1.insert(tk.END,7)

def number_8():
    Entry_1.insert(tk.END,8)

def number_9():
    Entry_1.insert(tk.END,9)

def number_0():
    Entry_1.insert(tk.END,0)

def number_00():
    Entry_1.insert(tk.END,'00')



#Tag section
Entry_1 = Entry(root,width=12,font=("Comic Sans MS",37,"bold"))
Entry_1.place(x=6,y=10)

#button section
button_equal = Button(root,text="🟰",width=3,height=2,font=("Comic Sans MS",28,"bold"),command=equal)
button_equal.place(x=290,y=423)

button_del = Button(root,text='C',width=4,font=("Comic Sans MS",20,"bold"),command=delet)
button_del.place(x=192,y=90)

button_clean = Button(root,text='⌫',width=4,font=("Comic Sans MS",20,"bold"),command=clean)
button_clean.place(x=293,y=90)

button_power = Button(root,text='x^y',width=4,font=("Comic Sans MS",20,"bold"),command=power)
button_power.place(x=100,y=90)

button_square_root = Button(root,text='√',width=4,font=("Comic Sans MS",20,"bold"),command=square_root)
button_square_root.place(x=8,y=90)

butt_plus_sign = Button(root,width=5,text='➕️',font=("Comic Sans MS",17,"bold"),command=plus_sign)
butt_plus_sign.place(x=291,y=165)

butt_minus_sign = Button(root,width=5,text='➖️',font=("Comic Sans MS",17,"bold"),command=minus_sign)
butt_minus_sign.place(x=291,y=229)

butt_times_sign = Button(root,width=5,text='✖️',font=("Comic Sans MS",17,"bold"),command=times_sign)
butt_times_sign.place(x=291,y=293)

butt_division_sign = Button(root,width=5,text='➗️',font=("Comic Sans MS",17,"bold"),command=division_sign)
butt_division_sign.place(x=291,y=357)


button_Number_decimal_point= Button(root,text='.',width=3,font=("Comic Sans MS",28,"bold"),command=number_decimal_point)
button_Number_decimal_point.place(x=192, y=474)

#   __button_Number__

button_Number1 = Button(root,text='1',width=3,font=("Comic Sans MS",28,"bold"),command=number_1)
button_Number1.place(x=8, y=177)

button_Number2 = Button(root,text='2',width=3,font=("Comic Sans MS",28,"bold"),command=number_2)
button_Number2.place(x=100, y=177)

button_Number3 = Button(root,text='3',width=3,font=("Comic Sans MS",28,"bold"),command=number_3)
button_Number3.place(x=192, y=177)

button_Number4 = Button(root,text='4',width=3,font=("Comic Sans MS",28,"bold"),command=number_4)
button_Number4.place(x=8, y=276)

button_Number5 = Button(root,text='5',width=3,font=("Comic Sans MS",28,"bold"),command=number_5)
button_Number5.place(x=100, y=276)

button_Number6 = Button(root,text='6',width=3,font=("Comic Sans MS",28,"bold"),command=number_6)
button_Number6.place(x=192, y=276)

button_Number7 = Button(root,text='7',width=3,font=("Comic Sans MS",28,"bold"),command=number_7)
button_Number7.place(x=8, y=375)

button_Number8 = Button(root,text='8',width=3,font=("Comic Sans MS",28,"bold"),command=number_8)
button_Number8.place(x=100, y=375)

button_Number9 = Button(root,text='9',width=3,font=("Comic Sans MS",28,"bold"),command=number_9)
button_Number9.place(x=192, y=375)

button_Number00 = Button(root,text='00',width=3,font=("Comic Sans MS",28,"bold"),command=number_00)
button_Number00.place(x=8, y=474)

button_Number0 = Button(root,text='0',width=3,font=("Comic Sans MS",28,"bold"),command=number_0)
button_Number0.place(x=100, y=474)


root.mainloop()