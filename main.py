from tkinter import *

root = Tk()
root.geometry('600x500')
root.title('Registration')

full_name=StringVar()

label_0 = Label(root, text="Registration", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=full_name)
entry_1.place(x=240, y=130)

root.mainloop()