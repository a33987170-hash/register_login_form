import tkinter as tk
from tkinter import messagebox
import hashlib

ITERATIONS = 600_000


def open_change_password_window(parent, user_email):
    window = tk.Toplevel(parent)
    window.title("Зміна пароля")
    window.geometry("500x350")
    window.configure(bg="#111827")
    window.resizable(False, False)

    tk.Label(
        window,
        text="Поточний пароль",
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="#F9FAFB",
    ).pack(pady=(15, 0))

    entry_current = tk.Entry(
        window,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=25,
        show="*",
    )
    entry_current.pack(pady=5)

    tk.Label(
        window,
        text="Новий пароль",
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="#F9FAFB",
    ).pack(pady=(10, 0))

    entry_new = tk.Entry(
        window,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=25,
        show="*",
    )
    entry_new.pack(pady=5)

    tk.Label(
        window,
        text="Підтвердити новий пароль",
        font=("Arial", 12, "bold"),
        bg="#111827",
        fg="#F9FAFB",
    ).pack(pady=(10, 0))

    entry_confirm = tk.Entry(
        window,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=25,
        show="*",
    )
    entry_confirm.pack(pady=5)

    def change_password():
        current_password = entry_current.get()
        new_password = entry_new.get()
        confirm_password = entry_confirm.get()

        if not current_password or not new_password or not confirm_password:
            messagebox.showwarning("Помилка", "Заповніть усі поля!", parent=window)
            return

        if new_password != confirm_password:
            messagebox.showwarning("Помилка", "Нові паролі не збігаються!", parent=window)
            return

        if len(new_password) < 8:
            messagebox.showwarning("Помилка", "Новий пароль має бути щонайменше 8 символів!", parent=window)
            return

        if " " in new_password:
            messagebox.showwarning("Помилка", "Пароль не повинен містити пробілів!", parent=window)
            return

        try:
            with open("data_users.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
        except FileNotFoundError:
            messagebox.showerror("Помилка", "Файл користувачів не знайдено!", parent=window)
            return

        hashed_current = hashlib.pbkdf2_hmac(
            "sha256", current_password.encode(), user_email.encode(), ITERATIONS
        ).hex()

        password_changed = False
        new_lines = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                new_lines.append(line)
                continue

            parts = stripped.split(":")
            if len(parts) >= 3:
                file_email = parts[0]
                file_password = parts[1]
                file_login = parts[2]

                if file_email.lower() == user_email.lower() and file_password == hashed_current:
                    hashed_new = hashlib.pbkdf2_hmac(
                        "sha256", new_password.encode(), file_email.encode(), ITERATIONS
                    ).hex()
                    new_lines.append(f"{file_email}:{hashed_new}:{file_login}\n")
                    password_changed = True
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)

        if not password_changed:
            messagebox.showerror("Помилка", "Поточний пароль невірний!", parent=window)
            return

        with open("data_users.txt", "w", encoding="utf-8") as file:
            file.writelines(new_lines)

        messagebox.showinfo("Успіх", "Пароль змінено!", parent=window)
        window.destroy()

    tk.Button(
        window,
        text="Змінити пароль",
        bg="#4F46E5",
        fg="#FFFFFF",
        font=("Arial", 12, "bold"),
        command=change_password,
    ).pack(pady=20)
