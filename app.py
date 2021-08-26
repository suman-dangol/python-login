from tkinter import *
import sqlite3
import bcrypt

root = Tk()
username = StringVar()
password = StringVar()
fullname = StringVar()

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


Label(root, text="Login", fg="#999", padx=10,
      pady=10, font=("Arial", 24)).pack(fill=BOTH)
Label(root, text="fullname", fg="#222", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=fullname, width=50, borderwidth=5,
      bg="#999", fg="#111", relief=FLAT).pack()
Label(root, text="username", fg="#222", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=username, width=50, borderwidth=5,
      bg="#999", fg="#111", relief=FLAT).pack()
Label(root, text="password", fg="#222", pady=2, font=("Arial", 14)).pack()
Entry(root, textvar=password, width=50, show="*", borderwidth=5,
      bg="#999", fg="#111", relief=FLAT).pack()
Button(root, text="register", bg="green", border=0, font=("""Arial
                                                       """, 14), padx=10, pady=5, fg="#fff", activebackground="green", activeforeground="white", command=register).pack()
root.mainloop()
