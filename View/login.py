from tkinter import *


def loginView(login_frame, fullname, username, password, login):
    Label(login_frame, text="Login", fg="#999", padx=10,
          pady=10, font=("Arial", 24)).pack(fill=BOTH)
    Label(login_frame, text="fullname", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(login_frame, textvar=fullname, width=50, borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Label(login_frame, text="username", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(login_frame, textvar=username, width=50, borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Label(login_frame, text="password", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(login_frame, textvar=password, width=50, show="*", borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Button(login_frame, text="Login", bg="blue", border=0, font=("""Arial
         """, 14), padx=10, pady=5, fg="#fff", activebackground="green", activeforeground="white", command=login).pack()
