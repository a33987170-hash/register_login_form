import tkinter as tk
from login_logic.login import open_login_window
from registration_logic.registration import open_registration_window


main_root = tk.Tk()
main_root.title("Авторизація")
main_root.geometry("500x350")
main_root.configure(bg="#111827")

tk.Label(
    main_root,
    text="Вхід та реєстрація",
    font=("Arial", 16, "bold"),
    bg="#7C3AED",
    fg="#FFFFFF",
).pack(pady=40)

tk.Button(
    main_root,
    text="Реєстрація",
    bg="#4F46E5",
    fg="#FAFEFF",
    font=("Arial", 12, "bold"),
    width=20,
    pady=10,
    command=lambda: open_registration_window(main_root),
).pack(pady=10)

tk.Button(
    main_root,
    text="Вхід",
    bg="#4F46E5",
    fg="#F7F0F0",
    font=("Arial", 12, "bold"),
    width=20,
    pady=10,
    command=lambda: open_login_window(main_root),
).pack(pady=10)

tk.Button(
    main_root,
    text="Вихід",
    bg="#4F46E5",
    fg="#F7F0F0",
    font=("Arial", 12, "bold"),
    width=20,
    pady=10,
    command=main_root.quit,
).pack(pady=10)

main_root.mainloop()
