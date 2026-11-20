import tkinter as tk
from tkinter import messagebox
import hashlib
from user_profil import profile_window


def login_window(main_root):
    login_win = tk.Toplevel(main_root)
    login_win.title("Вхід")
    login_win.geometry("500x300")
    login_win.configure(bg="#111827")

    tk.Label(
        login_win, text="Email",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(15, 0))
    entry_email = tk.Entry(
        login_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20,
    )
    entry_email.pack(pady=5)

    tk.Label(
        login_win, text="Password",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(10, 0))
    entry_password = tk.Entry(
        login_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20, show="*",
    )
    entry_password.pack(pady=5)

    tk.Label(
        login_win, text="Login",
        font=("Arial", 12, "bold"), bg="#1F2937", fg="#F9FAFB",
    ).pack(pady=(10, 0))
    entry_login = tk.Entry(
        login_win, font=("Arial", 14),
        bg="#1F2937", fg="#F9FAFB", insertbackground="white", width=20,
    )
    entry_login.pack(pady=5)

    attempts = [0]

    def logining():
        email = entry_email.get().strip()
        password = entry_password.get()
        login = entry_login.get().strip()

        if not email or not password or not login:
            messagebox.showwarning("Помилка", "Заповніть усі поля!")
            return

    
        found_login = ""
        try:
            with open("data_users.txt", "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(":")
                    if len(parts) >= 3:
                        file_email = parts[0]
                        file_password = parts[1]
                        file_login = parts[2]
                        hashed_input = hashlib.sha256(password.encode()).hexdigest()
                        if file_email.lower() == email.lower() and file_password == hashed_input:
                            found_login = file_login
                            break
        except FileNotFoundError:
            messagebox.showerror("Помилка", "Файл користувачів не знайдено!")
            return

        if found_login:
            messagebox.showinfo("Успіх", "Вхід виконано!")
            login_win.destroy()
            
            profile_window(main_root, email, found_login)
        else:
            attempts[0] += 1
            if attempts[0] >= 3:
                messagebox.showwarning(
                    "Помилка",
                    "3 невдалі спроби. Повернення до головного вікна."
                )
                login_win.destroy()
            else:
                messagebox.showwarning(
                    "Помилка",
                    f"Невірний email або пароль! (Спроба {attempts[0]} з 3)"
                )

    tk.Button(
        login_win, text="Увійти",
        bg="#4F46E5", fg="#FFFFFF", font=("Arial", 12, "bold"),
        command=logining,
    ).pack(pady=15)
