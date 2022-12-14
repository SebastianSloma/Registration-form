# import library tkinter and sqlite3 database
from tkinter import *
import sqlite3

# Create window object
root = Tk()
root.geometry('600x500')
root.title("Registration")


Fullname = StringVar()
Email = StringVar()
var = IntVar()
c = StringVar()
var1 = IntVar()

# create database and add record


def database():
    name1 = Fullname.get()
    email = Email.get()
    gender = var.get()
    country = c.get()
    drink = var1.get()
    conn = sqlite3.connect('Formdb.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS User (Fullname TEXT,Email TEXT,Gender TEXT,Country TEXT,Drink TEXT)')
    cursor.execute('INSERT INTO User (FullName,Email,Gender,Country,Drink) VALUES(?,?,?,?,?)',
                   (name1, email, gender, country, drink,))
    conn.commit()


# definition of labelas ans buttons
label_0 = Label(root, text="Registration", width=20, font=("bold", 20))
label_0.place(x=90, y=53)


label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20,
            variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text="country", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

list1 = ['Poland', 'Espaniol', 'Portugal', 'Germany', 'France', 'Italy']

droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240, y=280)

label_4 = Label(root, text="Drink", width=20, font=("bold", 10))
label_4.place(x=85, y=330)
var2 = IntVar()
Checkbutton(root, text="Coffee", variable=var1).place(x=290, y=330)

Checkbutton(root, text="Tea", variable=var2).place(x=235, y=330)

Button(root, text='Submit', width=20, bg='grey',
       fg='white', command=database).place(x=180, y=380)

root.mainloop()
