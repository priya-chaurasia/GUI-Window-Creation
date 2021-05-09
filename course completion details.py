import tkinter
from tkinter import messagebox, CENTER

window = tkinter.Tk()
window.title("Course Completion Certificate")
window.geometry("400x600")

tkinter.Label(window, text="Enter the details\n").pack()
tkinter.Label(window, text="Name of Student\n").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="Name of Course\n").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="Name of the Institution\n").pack()
tkinter.Entry(window).pack()

tkinter.Label(window, text="Date\n").pack()
tkinter.Entry(window).pack()

def regbutton():
    messagebox.showinfo('Message box','Submission successful')
btn = tkinter.Button(window, text="Submit",bg="blue",fg="white",command=regbutton)
btn.pack(side='bottom')

window.mainloop()


