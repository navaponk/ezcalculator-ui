#Navapon Kraitat (Earth) Coursework Project

import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "The calculation is undefined.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        result_label.config(text="Result: {:.2f}".format(result))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# window
window = tk.Tk()
window.title("Ezcalculator")
window.geometry("600x600")
window.configure(bg="#ffffff")

# style
style = ttk.Style()
style.configure("TButton", font=('Helvetica', 14), padding=10)
style.configure("TLabel", font=('Helvetica', 14), padding=10)
style.configure("TEntry", font=('Helvetica', 14))

# numbers entry
label_num1 = ttk.Label(window, text="Enter the first number:", style="TLabel")
label_num1.pack(pady=10)
entry_num1 = ttk.Entry(window, font=('Helvetica', 14))
entry_num1.pack(pady=10)

label_num2 = ttk.Label(window, text="Enter the second number:", style="TLabel")
label_num2.pack(pady=10)
entry_num2 = ttk.Entry(window, font=('Helvetica', 14))
entry_num2.pack(pady=10)

# dropdown
label_operation = ttk.Label(window, text="Select operation:", style="TLabel")
label_operation.pack(pady=10)
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar(window)
operation_var.set(operations[0])
operation_menu = ttk.Combobox(window, textvariable=operation_var, values=operations, font=('Helvetica', 12))
operation_menu.pack(pady=10)

# button
calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=20)

# result
result_label = ttk.Label(window, text="Result:", style="TLabel")
result_label.pack(pady=10)

# loop
window.mainloop()