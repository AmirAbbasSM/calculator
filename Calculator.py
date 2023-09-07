from tkinter import *
import tkinter as tk

root = Tk()
root.title('Calculator')
root.geometry('400x600')

# def section
def structure():
    input_1 = Entry_1.get()
    try:
        Answer = eval(input_1)
    except:
        Answer = 'Error in writing'

    Entry_1.delete(0,tk.END)
    Entry_1.insert(0,Answer)


def delet():
    Entry_1.delete(0,tk.END)
    

    
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
Entry_1 = Entry(root,width=12,font=("Comic Sans MS",40,"bold"))
Entry_1.place(x=8,y=10)

#button section
button_1 = Button(root,text="=",width=3,height=2,font=("Comic Sans MS",30,"bold"),command=structure)
button_1.place(x=300,y=445)

button_del = Button(root,text='del',font=("Comic Sans MS",30,"bold"),command=delet)
button_del.place(x=300,y=100)

#   __button_Number__

button_Number1 = Button(root,text='1',width=3,font=("Comic Sans MS",30,"bold"),command=number_1)
button_Number1.place(x=8, y=100)

button_Number2 = Button(root,text='2',width=3,font=("Comic Sans MS",30,"bold"),command=number_2)
button_Number2.place(x=100, y=100)

button_Number3 = Button(root,text='3',width=3,font=("Comic Sans MS",30,"bold"),command=number_3)
button_Number3.place(x=192, y=100)

button_Number4 = Button(root,text='4',width=3,font=("Comic Sans MS",30,"bold"),command=number_4)
button_Number4.place(x=8, y=205)

button_Number5 = Button(root,text='5',width=3,font=("Comic Sans MS",30,"bold"),command=number_5)
button_Number5.place(x=100, y=205)

button_Number6 = Button(root,text='6',width=3,font=("Comic Sans MS",30,"bold"),command=number_6)
button_Number6.place(x=192, y=205)

button_Number7 = Button(root,text='7',width=3,font=("Comic Sans MS",30,"bold"),command=number_7)
button_Number7.place(x=8, y=310)

button_Number8 = Button(root,text='8',width=3,font=("Comic Sans MS",30,"bold"),command=number_8)
button_Number8.place(x=100, y=310)

button_Number9 = Button(root,text='9',width=3,font=("Comic Sans MS",30,"bold"),command=number_9)
button_Number9.place(x=192, y=310)

button_Number00 = Button(root,text='00',width=3,font=("Comic Sans MS",30,"bold"),command=number_00)
button_Number00.place(x=8, y=415)

button_Number0 = Button(root,text='0',width=3,font=("Comic Sans MS",30,"bold"),command=number_0)
button_Number0.place(x=100, y=415)


root.mainloop()