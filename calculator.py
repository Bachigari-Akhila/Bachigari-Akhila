import tkinter as tk

def on_button_click(value):
    current = result_var.get()
    if value == "C":
        result_var.set("")
    elif value == "=":
        try:
            result_var.set(eval(current))
        except Exception:
            result_var.set("Error")
    else:
        result_var.set(current + value)

def clear_all():
    result_var.set("")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create a variable to hold the result
result_var = tk.StringVar()
result_var.set("")

# Create the result display area
result_label = tk.Label(app, textvariable=result_var, font=("Helvetica", 20))
result_label.grid(row=0, column=0, columnspan=4)

# Define the calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)  # Clear button
]

# Create and place the calculator buttons
for text, row, col in buttons:
    button = tk.Button(app, text=text, padx=20, pady=10, font=("Helvetica", 15),
                       command=lambda value=text: on_button_click(value))
    button.grid(row=row, column=col)

# Start the main event loop
app.mainloop()