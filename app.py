from tkinter import *
import sqlite3
import bcrypt
from View import login
from View.registerview import registerView
from View.login import loginView

root = Tk()
username = StringVar()
password = StringVar()
fullname = StringVar()

signup_frame = Frame(root)
signup_frame.pack()

login_frame = Frame(root)
login_frame.pack()

root.geometry('500x500+200+100')


def register():
    db = sqlite3.connect('app.db')
    cur = db.cursor()

#     cur.execute(
#         'CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL,fullname TEXT NOT NULL, password TEXT NOT NUll)')
    hashed_password = bcrypt.hashpw(
        password.get().encode('utf-8'), bcrypt.gensalt())
    print(fullname.get())
    print(username.get())
    print(hashed_password)

    cur.execute("""INSERT INTO users(fullname, username, password) values(?,?,?)""",
                (fullname.get(), username.get(), hashed_password))
    db.commit()


registerView(signup_frame, fullname, username, password, register)
loginView(login_frame, fullname, username, password, login)
root.mainloop()
