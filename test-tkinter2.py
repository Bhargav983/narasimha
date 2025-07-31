import tkinter as tk
from tkinter import messagebox

menu = {
    'Burger': 51.00,
    'Pizza': 81.00,
    'Salad': 41.00,
    'Pasta': 71.00,
    'Soda': 11.00,
    'Water': 51.00
}

# Stores the entry widgets for quantity
qty_entries = {}

def generate_bill():
    f = open("bill.txt","a")
    order = {}
    total = 0
    bill_text.delete('1.0', tk.END)
    bill_text.insert(tk.END, "--- Your Order ---\n")
    f.write("--- Your Order ---\n")
    for item, entry in qty_entries.items():
        qty_str = entry.get()
        if qty_str.strip():
            try:
                qty = int(qty_str)
                if qty > 0:
                    order[item] = qty
                    price = menu[item] * qty
                    total += price
                    bill_text.insert(tk.END, f"{item:10} x{qty} = Rs {price:.2f}\n")
                    f.write(f"{item:10} x{qty} = Rs {price:.2f}\n")
            except ValueError:
                messagebox.showerror("Invalid Input", f"Please enter a valid number for {item}.")
                return
    
    bill_text.insert(tk.END, f"\nTotal bill: Rs {total:.2f}\n")
    f.write(f"\nTotal bill: Rs {total:.2f}\n")
    bill_text.insert(tk.END, "--------------------------\nThank you for dining with us!")
    f.write("--------------------------\nThank you for dining with us!\n")
    f.close()

def clear_all():
    for entry in qty_entries.values():
        entry.delete(0, tk.END)
    bill_text.delete('1.0', tk.END)

def exit_app():
    root.destroy()

# Main window
root = tk.Tk()
root.title("Python Café - Restaurant Menu")
root.geometry("420x550")
root.resizable(False, False)

tk.Label(root, text="🍽️ Welcome to Python Café!", font=('Arial', 16, 'bold')).pack(pady=10)

# Menu section
menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

tk.Label(menu_frame, text="Item", font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=10)
tk.Label(menu_frame, text="Price (Rs)", font=('Arial', 12, 'bold')).grid(row=0, column=1, padx=10)
tk.Label(menu_frame, text="Qty", font=('Arial', 12, 'bold')).grid(row=0, column=2, padx=10)

for i, (item, price) in enumerate(menu.items(), start=1):
    tk.Label(menu_frame, text=item, font=('Arial', 11)).grid(row=i, column=0, pady=5)
    tk.Label(menu_frame, text=f"{price:.2f}", font=('Arial', 11)).grid(row=i, column=1)
    
    qty_entry = tk.Entry(menu_frame, width=5)
    qty_entry.grid(row=i, column=2)
    qty_entries[item] = qty_entry

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Generate Bill", command=generate_bill).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Clear", command=clear_all).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Exit", command=exit_app).grid(row=0, column=2, padx=10)

# Bill area
bill_text = tk.Text(root, height=12, width=50, font=('Courier', 10))
bill_text.pack(pady=10)

root.mainloop()
