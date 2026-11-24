import tkinter as tk
from tkinter import messagebox
import hashlib
from user_profil_logic.profile_menu import open_profile_window
from BD_logic.connect_db import check_user_exists, register_user

ITERATIONS = 600_000


def open_registration_window(main_root):
    main_root.withdraw()

    reg_win = tk.Toplevel()
    reg_win.title("Реєстрація")
    reg_win.geometry("500x430")
    reg_win.configure(bg="#111827")

    def on_close():
        reg_win.destroy()
        main_root.deiconify()

    reg_win.protocol("WM_DELETE_WINDOW", on_close)

    tk.Label(
        reg_win,
        text="Електронна пошта",
        font=("Arial", 12, "bold"),
        bg="#1F2937",
        fg="#F9FAFB",
    ).pack(pady=(15, 0))

    entry_email = tk.Entry(
        reg_win,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=20,
    )
    entry_email.pack(pady=5)

    tk.Label(
        reg_win,
        text="Логін",
        font=("Arial", 12, "bold"),
        bg="#1F2937",
        fg="#F9FAFB",
    ).pack(pady=(10, 0))

    entry_login = tk.Entry(
        reg_win,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=20,
    )
    entry_login.pack(pady=5)

    tk.Label(
        reg_win,
        text="Пароль",
        font=("Arial", 12, "bold"),
        bg="#1F2937",
        fg="#F9FAFB",
    ).pack(pady=(10, 0))

    entry_password = tk.Entry(
        reg_win,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=20,
        show="*",
    )
    entry_password.pack(pady=5)

    tk.Label(
        reg_win,
        text="Повторити пароль",
        font=("Arial", 12, "bold"),
        bg="#1F2937",
        fg="#F9FAFB",
    ).pack(pady=(10, 0))

    entry_password_repeat = tk.Entry(
        reg_win,
        font=("Arial", 14),
        bg="#1F2937",
        fg="#F9FAFB",
        insertbackground="white",
        width=20,
        show="*",
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
            messagebox.showwarning("Помилка", "Електронна пошта повинна містити @ та крапку!")
            return

        if " " in email:
            messagebox.showwarning("Помилка", "Електронна пошта не повинна містити пробілів!")
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
            existing_user = check_user_exists(email, login)
            if existing_user:
                db_email, db_login = existing_user
                if db_email.lower() == email.lower():
                    messagebox.showwarning("Помилка", "Така електронна пошта вже зареєстрована!")
                    return
                if db_login.lower() == login.lower():
                    messagebox.showwarning("Помилка", "Такий логін вже зайнятий!")
                    return
        except Exception as e:
            messagebox.showerror("Помилка", f"Помилка бази даних: {e}")
            return

        hashed_password = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            email.encode(),
            ITERATIONS,
        ).hex()

        try:
            register_user(email, hashed_password, login)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти користувача: {e}")
            return

        messagebox.showinfo("Успіх", "Реєстрацію завершено!")
        reg_win.destroy()
        open_profile_window(main_root, email, login)

    tk.Button(
        reg_win,
        text="Зареєструватися",
        bg="#4F46E5",
        fg="#FFFFFF",
        font=("Arial", 12, "bold"),
        command=register,
    ).pack(pady=15)
