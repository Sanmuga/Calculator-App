import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
        else:
            messagebox.showerror("Error", "Invalid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create and place widgets
entry_num1 = tk.Entry(window, width=15)
entry_num1.grid(row=0, column=0, padx=10, pady=10)

operation_var = tk.StringVar()
operation_choices = ['+', '-', '*', '/']
operation_menu = tk.OptionMenu(window, operation_var, *operation_choices)
operation_var.set('+')  # default operation
operation_menu.grid(row=0, column=1, padx=10, pady=10)

entry_num2 = tk.Entry(window, width=15)
entry_num2.grid(row=0, column=2, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, pady=10)

result_label = tk.Label(window, text="Result: ")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
window.mainloop()
