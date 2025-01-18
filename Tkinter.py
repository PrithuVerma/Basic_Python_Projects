from tkinter import*

window= Tk()
window.title('My GUI')
window.minsize(1000,1000)




my_label = Label(text='I am a label',font=('Arial',24,"bold"),fg="White")
my_label.pack()

def clicked():
    print('I got clapped')
    my_label.config("Clapped")

button = Button(text="Click me",command=clicked)
button.pack()



window.mainloop()