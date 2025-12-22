import tkinter as tk

window = tk.Tk()
window.title("Responsive Calculator")
window.geometry("320x450")  # initial size
window.minsize(320, 450)    # minimum size
window.resizable(True, True)  # allow maximize

# Entry box
entry = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

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
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('=',)
]

# Colors
num_color = "#f0f0f0"
op_color = "#ffb347"
clear_color = "#ff6961"

# Configure grid weights to make it responsive
for i in range(5):  # 5 rows (0=entry, 1-4 buttons, 5 for '=')
    window.rowconfigure(i, weight=1)
for i in range(4):  # 4 columns
    window.columnconfigure(i, weight=1)

# Create buttons
for r, row in enumerate(buttons, start=1):
    for c, btn in enumerate(row):
        if btn == "=":
            tk.Button(window, text=btn, bg=op_color, font=("Arial", 18),
                      command=calculate).grid(row=r, column=0, columnspan=2,
                                              sticky="nsew", padx=3, pady=3)
        elif btn == "C":
            tk.Button(window, text=btn, bg=clear_color, font=("Arial", 18),
                      command=clear).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
        elif btn in "+-*/":
            tk.Button(window, text=btn, bg=op_color, font=("Arial", 18),
                      command=lambda b=btn: click(b)).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)
        else:
            tk.Button(window, text=btn, bg=num_color, font=("Arial", 18),
                      command=lambda b=btn: click(b)).grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

window.mainloop()
