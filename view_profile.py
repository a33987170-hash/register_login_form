import tkinter as tk


def open_view_profile_window(parent, user_email, user_login):
    view_win = tk.Toplevel(parent)
    view_win.title("Перегляд профілю")
    view_win.geometry("400x250")
    view_win.configure(bg="#111827")
    view_win.resizable(False, False)

    tk.Label(
        view_win,
        text="Ваш профіль",
        font=("Arial", 16, "bold"),
        bg="#7C3AED",
        fg="#FFFFFF",
    ).pack(pady=(20, 15))

    tk.Label(
        view_win,
        text=f"Логін:  {user_login}",
        font=("Arial", 13),
        bg="#111827",
        fg="#F9FAFB",
        anchor="w",
    ).pack(padx=40, fill="x", pady=5)

    tk.Label(
        view_win,
        text=f"Електронна пошта:  {user_email}",
        font=("Arial", 13),
        bg="#111827",
        fg="#F9FAFB",
        anchor="w",
    ).pack(padx=40, fill="x", pady=5)

    tk.Button(
        view_win,
        text="Закрити",
        bg="#4F46E5",
        fg="#FFFFFF",
        font=("Arial", 12, "bold"),
        command=view_win.destroy,
    ).pack(pady=20)
