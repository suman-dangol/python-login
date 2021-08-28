from tkinter import *


def registerView(register_frame, fullname,  username, password, register):
    Label(register_frame, text="Register", fg="#999", padx=10,
          pady=10, font=("Arial", 24)).pack(fill=BOTH)
    Label(register_frame, text="fullname", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(register_frame, textvar=fullname, width=50, borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Label(register_frame, text="username", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(register_frame, textvar=username, width=50, borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Label(register_frame, text="password", fg="#222",
          pady=2, font=("Arial", 14)).pack()
    Entry(register_frame, textvar=password, width=50, show="*", borderwidth=5,
          bg="#999", fg="#111", relief=FLAT).pack()
    Button(register_frame, text="register", bg="green", border=0, font=("""Arial
        =""", 14), padx=10, pady=5, fg="#fff", activebackground="green", activeforeground="white", command=register).pack()
