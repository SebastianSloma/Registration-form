from tkinter import *
import sqlite3

root = Tk()
root.geometry('600x500')
root.title('Registration')

full_name = StringVar()
Email = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()


def database():
    name = full_name.get()
    email = Email.get()
    gender = var.get()
    country = c.get()
    drink = var1.get()
    con = sqlite3.connect('form.db')
    with con:
        cursor = con.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS Student (full_name TEXT, email TEXT, gender TEXT, country TEXT, drink text )')
        cursor.execute('INSERT INTO Student (full_name, email,gender, country, drink ) VALUES(?,?,?,?,?)',
                       (name, email, gender, country, drink,))
        con.commit()


label_0 = Label(root, text="Registration", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Full Name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=full_name)
entry_1.place(x=240, y=130)

root.mainloop()
