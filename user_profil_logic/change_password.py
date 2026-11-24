import tkinter as tk
from tkinter import messagebox
import hashlib
from BD_logic.connect_db import get_user_by_email, update_user_password

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
            user = get_user_by_email(user_email)
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка бази даних: {e}", parent=window)
            return

        if not user:
            messagebox.showerror("Помилка", "Користувача не знайдено!", parent=window)
            return

        user_id, db_login, db_email, db_password = user
        hashed_current = hashlib.pbkdf2_hmac(
            "sha256",
            current_password.encode(),
            user_email.encode(),
            ITERATIONS,
        ).hex()

        if db_password != hashed_current:
            messagebox.showerror("Помилка", "Поточний пароль невірний!", parent=window)
            return

        hashed_new = hashlib.pbkdf2_hmac(
            "sha256",
            new_password.encode(),
            user_email.encode(),
            ITERATIONS,
        ).hex()

        try:
            update_user_password(user_email, hashed_new)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося оновити пароль: {e}", parent=window)
            return

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
