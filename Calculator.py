from tkinter import *
import tkinter as tk

root = Tk()
root.title('Calculator')
root.geometry('500x600')

def structure():
    input_1 = Entry_1.get()
    try:
        Answer = eval(input_1)
        # print(Answer)
    except:
        Answer = 'Error in writing'

    Entry_1.delete(0,tk.END)
    Entry_1.insert(0,Answer)

def delet():
    Entry_1.delete(00,tk.END)
    
    # print(int(input_1))
    # print(type(3*60))
    


#Tag section
Entry_1 = Entry(root,width=14,font=("Comic Sans MS",40,"bold"))
Entry_1.place(x=24,y=10)

#button section
button_1 = Button(root,text="=",width=4,font=("Comic Sans MS",30,"bold"),command=structure)
button_1.place(x=400,y=500)

button_2 = Button(root,text='del',font=("Comic Sans MS",30,"bold"),command=delet)
button_2.place(x=400,y=100)


root.mainloop()