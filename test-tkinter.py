import tkinter as tk
from tkinter import ttk, messagebox

menu = {
    'Burger': 51.00,
    'Pizza': 81.00,
    'Salad': 41.00,
    'Pasta': 71.00,
    'Soda': 11.00,
    'Water': 51.00
}

order = {}

def add_to_order():
    item = item_var.get()
    try:
        qty = int(qty_var.get())
        if qty <= 0:
            raise ValueError
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        update_bill()
        qty_var.set("")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid quantity.")

def update_bill():
    bill_text.delete('1.0', tk.END)
    total = 0
    bill_text.insert(tk.END, "--- Your Order ---\n")
    for item, qty in order.items():
        price = menu[item] * qty
        total += price
        bill_text.insert(tk.END, f"{item:10} x{qty} = Rs {price:.2f}\n")
    bill_text.insert(tk.END, f"Total bill: Rs {total:.2f}\n")
    bill_text.insert(tk.END, "--------------------------\nThank you for dining with us!")

def clear_order():
    order.clear()
    update_bill()

def exit_app():
    root.destroy()

# Main Window
root = tk.Tk()
root.title("Python Café - Restaurant Menu")
root.geometry("400x500")
root.resizable(False, False)

# Header
tk.Label(root, text="🍽️ Welcome to Python Café!", font=('Arial', 16, 'bold')).pack(pady=10)

# Menu Frame
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

tk.Label(menu_frame, text="Select Item:").grid(row=0, column=0, padx=5, pady=5)
item_var = tk.StringVar(value=list(menu.keys())[0])
item_menu = ttk.Combobox(menu_frame, textvariable=item_var, values=list(menu.keys()), state='readonly')
item_menu.grid(row=0, column=1, padx=5, pady=5)

tk.Label(menu_frame, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
qty_var = tk.StringVar()
qty_entry = tk.Entry(menu_frame, textvariable=qty_var)
qty_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add to Order", command=add_to_order).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear Order", command=clear_order).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Exit", command=exit_app).grid(row=0, column=2, padx=5)

# Bill Display
bill_text = tk.Text(root, height=15, width=45, font=('Courier', 10))
bill_text.pack(pady=10)

update_bill()  # initialize with empty order

root.mainloop()
