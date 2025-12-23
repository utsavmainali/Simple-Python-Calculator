import tkinter as tk

window = tk.Tk()
window.title("ios style Calculator")
window.geometry("320x450")  # initial size
window.minsize(320, 450)    # minimum size
window.configure(bg="black")
window.resizable(True, True)  # allow maximize

# Entry display
entry = tk.Entry(
    window,
    font=("Helvetica", 32),
    bg="black",
    fg="white",
    bd=0,
    justify="right",
)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ("C", "±", "%", "/"),
    ("7", "8", "9", "*"),
    ("4", "5", "6", "-"),
    ("1", "2", "3", "+"),
    ("0", ".", "="),
]

# Colors
num_bg = "#333333"
op_bg = "#ff9f0a"
func_bg = "#a5a5a5"
num_fg = "white"
func_fg = "black"

# Configure grid weights to make it responsive
for i in range(6):  # 5 rows (0=entry, 1-4 buttons, 5 for '=')
    window.rowconfigure(i, weight=1)
for i in range(4):  # 4 columns
    window.columnconfigure(i, weight=1)

# Create buttons
for r, row in enumerate(buttons, start=1):
    c = 0
    for btn in row:
        if btn == "0":
            tk.Button(
                window, text=btn, font=("Helvetica", 20),
                bg=num_bg, fg=num_fg, bd=0,
                command=lambda b=btn: click(b)
            ).grid(row=r, column=c, columnspan=2, sticky="nsew", padx=5, pady=5)
            c += 2

        elif btn == "=":
            tk.Button(
                window, text=btn, font=("Helvetica", 20),
                bg=op_bg, fg="white", bd=0,
                command=calculate
            ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            c += 1

        elif btn == "C":
            tk.Button(
                window, text=btn, font=("Helvetica", 20),
                bg=func_bg, fg=func_fg, bd=0,
                command=clear
            ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            c += 1

        elif btn in "+-*/":
            tk.Button(
                window, text=btn, font=("Helvetica", 20),
                bg=op_bg, fg="white", bd=0,
                command=lambda b=btn: click(b)
            ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            c += 1

        else:
            tk.Button(
                window, text=btn, font=("Helvetica", 20),
                bg=num_bg, fg=num_fg, bd=0,
                command=lambda b=btn: click(b)
            ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
            c += 1

window.mainloop()
