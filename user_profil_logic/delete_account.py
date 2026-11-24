from tkinter import messagebox
from BD_logic.connect_db import delete_user_by_email


def handle_delete_account(prof_win, main_root, user_email):
    confirm = messagebox.askyesno(
        "Підтвердження",
        "Ви дійсно бажаєте видалити свій обліковий запис?",
        parent=prof_win,
    )
    if not confirm:
        return

    try:
        delete_user_by_email(user_email)
        messagebox.showinfo(
            "Успіх",
            "Обліковий запис успішно видалено!",
            parent=prof_win,
        )
        prof_win.destroy()
        main_root.deiconify()
    except Exception as e:
        messagebox.showerror(
            "Помилка",
            f"Не вдалося видалити обліковий запис: {e}",
            parent=prof_win,
        )
