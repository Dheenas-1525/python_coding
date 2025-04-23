from tkinter import *

def calculate_total():
    total = (int(entry_qty.get()) * int(entry_price.get()))
    label_total.config(text="Total: ₹" + str(total))

# Window
root = Tk()
root.title("Supermarket Billing System")

# Labels & Entries
Label(root, text="Product Name:").grid(row=0, column=0)
entry_product = Entry(root)
entry_product.grid(row=0, column=1)

Label(root, text="Quantity:").grid(row=1, column=0)
entry_qty = Entry(root)
entry_qty.grid(row=1, column=1)

Label(root, text="Price per item:").grid(row=2, column=0)
entry_price = Entry(root)
entry_price.grid(row=2, column=1)

# Button
Button(root, text="Calculate Total", command=calculate_total).grid(row=3, column=0, columnspan=2)

# Total label
label_total = Label(root, text="Total: ₹0")
label_total.grid(row=4, column=0, columnspan=2)

# Run
root.mainloop()
