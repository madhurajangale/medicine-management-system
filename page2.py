import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import psycopg2

def create_stock_page(parent):
    label = tk.Label(parent, text="Add Items to Database", font=("Cambria", 16))  # Set background color
    label.pack(pady=10)  # Adjust padding

    # Entry variables
    dealer_id_var = tk.StringVar()
    dealer_name_var = tk.StringVar()
    product_id_var = tk.StringVar()
    product_name_var = tk.StringVar()
    expiry_date_var = tk.StringVar()  # New entry for product expiry date

    # Labels and Entry widgets
    tk.Label(parent, text="Dealer ID:", font=("Cambria", 20)).pack()
    dealer_id_entry = tk.Entry(parent, textvariable=dealer_id_var, font=("Cambria", 20), bg="SystemButtonFace")
    dealer_id_entry.pack()

    tk.Label(parent, text="Dealer Name:", font=("Cambria", 20)).pack()
    dealer_name_entry = tk.Entry(parent, textvariable=dealer_name_var, font=("Cambria", 20), bg="SystemButtonFace")
    dealer_name_entry.pack()

    tk.Label(parent, text="Product ID:", font=("Cambria", 20)).pack()
    product_id_entry = tk.Entry(parent, textvariable=product_id_var, font=("Cambria", 20), bg="SystemButtonFace")
    product_id_entry.pack()

    tk.Label(parent, text="Product Name:", font=("Cambria", 20)).pack()
    product_name_entry = tk.Entry(parent, textvariable=product_name_var, font=("Cambria", 20), bg="SystemButtonFace")
    product_name_entry.pack()

    tk.Label(parent, text="Expiry Date (YYYY-MM-DD):", font=("Cambria", 20)).pack()  # New label for expiry date
    expiry_date_entry = tk.Entry(parent, textvariable=expiry_date_var, font=("Cambria", 20), bg="SystemButtonFace")
    expiry_date_entry.pack()

    # Function to add item to the database
    def add_to_database():
        try:
            connection = psycopg2.connect(
                database="register",
                user="postgres",
                password="#Shravani2509",
                host="localhost",
                port="5432"
            )

            cursor = connection.cursor()

            # Retrieve values from entry widgets
            dealer_id = dealer_id_var.get()
            dealer_name = dealer_name_var.get()
            product_id = product_id_var.get()
            product_name = product_name_var.get()
            expiry_date = expiry_date_var.get()  # Retrieve expiry date

            # Insert values into the dealers table
            cursor.execute("INSERT INTO dealers (id, name) VALUES (%s, %s) RETURNING id",
                           (dealer_id, dealer_name))

            # Fetch the last inserted dealer_id
            dealer_id = cursor.fetchone()[0]

            # Insert values into the products table with the foreign key dealer_id
            cursor.execute("INSERT INTO products (id, name, dealer_id, expiry_date) VALUES (%s, %s, %s, %s)",
                           (product_id, product_name, dealer_id, expiry_date))  # Fix: Use product_id instead of id

            connection.commit()
            connection.close()

            tk.messagebox.showinfo("Success", "Item added to the database successfully!")

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {str(e)}")

    # Function to view products
    def view_products():
        new_window = tk.Toplevel(parent)
        new_window.title("View Products")

        try:
            connection = psycopg2.connect(
                database="register",
                user="postgres",
                password="#Shravani2509",
                host="localhost",
                port="5432"
            )

            cursor = connection.cursor()

            # Execute a SELECT query to retrieve all products
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            # Create a Listbox to display products
            products_listbox = tk.Listbox(new_window, height=10, width=50, font=("Cambria", 12))
            products_listbox.pack(padx=10, pady=10)

            # Insert products into the Listbox
            for product in products:
                products_listbox.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Dealer ID: {product[2]}, Expiry Date: {product[3]}")

            connection.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {str(e)}")

    # Buttons
    tk.Button(parent, text="Add to Database", command=add_to_database, font=("Cambria", 20)).pack(pady=10)
    tk.Button(parent, text="View Products", command=view_products, font=("Cambria", 20)).pack(pady=10)

def set_bg_image(root):
    global photo
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    image = Image.open(r"w2.png")
    image = image.resize((desktop_width, desktop_height))

    alpha = Image.new('L', image.size, 200)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=photo)
    bg_label.place(relwidth=1, relheight=1)

    root.attributes('-transparentcolor', 'gray')  # Adjust the transparent color as needed
    root.geometry(f"{desktop_width}x{desktop_height}")

if __name__ == "__main__":
    root = tk.Tk()

    set_bg_image(root)
    create_stock_page(root)
    root.mainloop()
