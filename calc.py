import tkinter as tk


def click(key):
    if key == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Ошибка")
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

def press_enter(event):
    click('=')
    return "break"

def validate_input(action, value_if_allowed):
    if action == '1':
        allowed_chars = "0123456789+-*/."
        return all(char in allowed_chars for char in value_if_allowed)
    return True

root = tk.Tk()
root.title("🌑Калькулятор🌑")
root.geometry("340x360")
root.resizable(False, False)
root.minsize(340, 360)

root.bind('<Return>', press_enter)
root.bind('<KP_Enter>', press_enter)

vcmd = (root.register(validate_input), '%d', '%P')

entry = tk.Entry(
    root,
    font=("Arial", 20),
    justify="right",
    validate="key",
    validatecommand=vcmd
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, font=("Arial", 14), width=5, height=2,
        command=lambda b=button: click(b)
    ).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()