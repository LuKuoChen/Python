import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# 创建主窗口
window = tk.Tk()
window.title("计算器")

# 创建输入框
entry = tk.Entry(window, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "/"
]

row = 1
col = 0

for button_text in buttons:
    if button_text == "=":
        tk.Button(window, text=button_text, padx=20, pady=20, command=calculate).grid(row=row, column=col)
    elif button_text == "C":
        tk.Button(window, text=button_text, padx=20, pady=20, command=clear).grid(row=row, column=col)
    else:
        tk.Button(window, text=button_text, padx=20, pady=20, command=lambda btn=button_text: button_click(btn)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行主循环
window.mainloop()