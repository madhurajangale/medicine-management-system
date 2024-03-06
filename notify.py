import tkinter as tk
from tkinter import messagebox
import psycopg2
from datetime import date

# Connect to PostgreSQL (replace with your database credentials)
conn = psycopg2.connect(
    user="postgres",
    password="#Shravani2509",
    host="localhost",
    port="5432",
    database="register"
)
cursor = conn.cursor()

# Create the products table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        expiry_date DATE NOT NULL
    )
''')
conn.commit()

# Function to check and show notifications for expiring products
def check_expiry_notifications():
    today = date.today()

    # Retrieve products that expire today
    cursor.execute('SELECT name FROM products WHERE expiry_date = %s', (today,))
    expiring_products = cursor.fetchall()

    if expiring_products:
        products_list = "\n".join([product[0] for product in expiring_products])
        messagebox.showinfo("Expiry Notification", f"The following products will expire today:\n\n{products_list}")

# Function to add a new product to the database
def add_product():
    name = entry_name.get()
    expiry_date = entry_expiry_date.get()

    # Insert the new product into the database
    cursor.execute('INSERT INTO products (name, expiry_date) VALUES (%s, %s)', (name, expiry_date))
    conn.commit()

    # Show a confirmation message
    messagebox.showinfo("Product Added", "Product added successfully!")

    # Clear the entry fields
    entry_name.delete(0, tk.END)
    entry_expiry_date.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Expiry Notification System")

# Set background color
root.configure(bg="#F0F0F0")  # Change to your preferred color

# Entry fields for product information
label_name = tk.Label(root, text="Product Name:", bg="#F0F0F0", font=("Helvetica", 20))  # Change to your preferred color and font size
entry_name = tk.Entry(root, font=("Helvetica", 20))

label_expiry_date = tk.Label(root, text="Expiry Date (YYYY-MM-DD):", bg="#F0F0F0", font=("Helvetica", 20))  # Change to your preferred color and font size
entry_expiry_date = tk.Entry(root, font=("Helvetica", 20))

# Button to add a new product
btn_add_product = tk.Button(root, text="Add Product", command=add_product, bg="#2196F3", fg="white", font=("Helvetica", 20))  # Change to your preferred colors and font size

# Button to check and show expiry notifications
btn_check_expiry = tk.Button(root, text="Check Expiry Notifications", command=check_expiry_notifications, bg="#2196F3", fg="white", font=("Helvetica", 20))  # Change to your preferred colors and font size

# Grid layout for the GUI components
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_expiry_date.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_expiry_date.grid(row=1, column=1, padx=10, pady=5)

btn_add_product.grid(row=2, column=0, columnspan=2, pady=10)
btn_check_expiry.grid(row=3, column=0, columnspan=2, pady=10)

# Center the window on the screen
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry(f"+{position_right}+{position_down}")

# Start the Tkinter event loop
root.mainloop()

# Close the PostgreSQL connection when the GUI is closed
conn.close()
