import tkinter as tk
from tkinter import messagebox


def view_profile_window(parent, user_email, user_login):
    messagebox.showinfo(
        "Профіль",
        f"Логін: {user_login}\nEmail: {user_email}",
        parent=parent,
    )
