import tkinter as tk
from tkinter import messagebox
import base64
import hashlib
import hmac
import secrets

ITERATIONS = 600_000

def registration_window(main_root):
    reg_win = tk.Toplevel(main_root)
    reg_win.title("Registration")
    reg_win.geometry("500x400")
    reg_win.configure(bg="#111827")

    tk.Label(
        reg_win, text="Email",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(15, 0))
    entry_email = tk.Entry(
        reg_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20,
    )
    entry_email.pack(pady=5)

    tk.Label(
        reg_win, text="Login",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(10, 0))
    entry_login = tk.Entry(
        reg_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20,
    )
    entry_login.pack(pady=5)

    tk.Label(
        reg_win, text="Password",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(10, 0))
    entry_password = tk.Entry(
        reg_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20, show="*",
    )
    entry_password.pack(pady=5)

    tk.Label(
        reg_win, text="Password repeat",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(10, 0))
    entry_password_repeat = tk.Entry(
        reg_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20, show="*",
    )
    entry_password_repeat.pack(pady=5)

    def register():
        email = entry_email.get().strip()
        login = entry_login.get().strip()
        password = entry_password.get()
        confirm = entry_password_repeat.get()

      

        if not email or not login or not password or not confirm:
            messagebox.showwarning("Помилка", "Заповніть усі поля!")
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning("Помилка", "Email повинен містити @ і крапку!")
            return

        if " " in email:
            messagebox.showwarning("Помилка", "Email не повинен містити пробілів!")
            return

        if len(login) < 4 or len(login) > 20:
            messagebox.showwarning("Помилка", "Логін має бути від 4 до 20 символів!")
            return

        if len(password) < 8:
            messagebox.showwarning("Помилка", "Пароль має бути щонайменше 8 символів!")
            return

        if " " in password:
            messagebox.showwarning("Помилка", "Пароль не повинен містити пробілів!")
            return

        if password != confirm:
            messagebox.showwarning("Помилка", "Паролі не збігаються!")
            return

        
        try:
            with open("data_users.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(":")
                    if len(parts) >= 3:
                        file_email = parts[0]
                        file_login = parts[2]
                        if file_email.lower() == email.lower():
                            messagebox.showwarning("Помилка", "Такий email вже зареєстрований!")
                            return
                        if file_login.lower() == login.lower():
                            messagebox.showwarning("Помилка", "Такий логін вже зайнятий!")
                            return
        except FileNotFoundError:
            pass

       
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open("data_users.txt", "a", encoding="utf-8") as file:
            file.write(f"{email}:{hashed_password}:{login}\n")

        messagebox.showinfo("Успіх", "Реєстрація завершена!")
        reg_win.destroy()

    tk.Button(
        reg_win, text="Зареєструватися",
        bg="#4F46E5", fg="#FFFFFF", font=("Arial", 12, "bold"),
        command=register,
    ).pack(pady=15)
