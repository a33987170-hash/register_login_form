import tkinter as tk
from change_password import open_change_password_window
from view_profile import open_view_profile_window


def open_profile_window(main_root, user_email, user_login):
    prof_win = tk.Toplevel()
    prof_win.title("Профіль")
    prof_win.geometry("500x400")
    prof_win.configure(bg="#111827")

    def on_close():
        prof_win.destroy()
        main_root.deiconify()

    prof_win.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(
        prof_win,
        text=f"Вітаємо, {user_login}!",
        font=("Arial", 16, "bold"),
        bg="#7C3AED",
        fg="#FFFFFF",
    ).pack(pady=20)

    tk.Button(
        prof_win,
        text="Переглянути профіль",
        bg="#4F46E5",
        fg="#FAFEFF",
        font=("Arial", 12, "bold"),
        width=20,
        pady=10,
        command=lambda: open_view_profile_window(prof_win, user_email, user_login),
    ).pack(pady=10)

    tk.Button(
        prof_win,
        text="Змінити пароль",
        bg="#4F46E5",
        fg="#F7F0F0",
        font=("Arial", 12, "bold"),
        width=20,
        pady=10,
        command=lambda: open_change_password_window(prof_win, user_email),
    ).pack(pady=10)

    tk.Button(
        prof_win,
        text="Вийти з облікового запису",
        bg="#4F46E5",
        fg="#F7F0F0",
        font=("Arial", 12, "bold"),
        width=20,
        pady=10,
        command=on_close,
    ).pack(pady=10)
