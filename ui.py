from tkinter import *
from tkinter import ttk
import sqlite3

def fetch_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def load_products():
    for row in fetch_products():
        product_table.insert("", "end", values=row)

# Window setup
root = Tk()
root.title("Supermarket Billing System")
root.geometry("800x500")

# Title
Label(root, text="Supermarket Billing System", font=("Arial", 20, "bold")).pack(pady=10)

# Product Table
columns = ("Product ID", "Name", "Category", "Price", "Stock", "GST %")
product_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    product_table.heading(col, text=col)
    product_table.column(col, width=100)

product_table.pack(pady=20, fill=X)
load_products()

# Exit Button
Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
