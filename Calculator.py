from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('500x600')

def structure():
    input_1 = Entry_1.get()
    print(input_1)
    # print(int(input_1))
    # print(type(3*60))
    


#Tag section
Entry_1 = Entry(root,width=14,font=("Comic Sans MS",40,"bold"))
Entry_1.place(x=24,y=10)

#button section
button_1 = Button(root,text="=",font=("Comic Sans MS",30,"bold"),command=structure)
button_1.place(x=430,y=500)



root.mainloop()