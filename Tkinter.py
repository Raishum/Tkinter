from tkinter import*


def myFunction():
    # myEntry.get()
    myLabel.config(text=myEntry.get())


root = Tk()

root.geometry("500x500")
root.resizable(False, False)

myEntry = Entry(root, borderwidth=5.0)
myButton = Button(root, text ="Button Dose Stuff", command=myFunction)
myLabel = Label(root, text="Starting text")

myEntry.place(X=200,Y=50)
myButton.place(X=200,Y=50)
myLabel.place(X=200,Y=50)



root.mainloop()