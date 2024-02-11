import tkinter as tk
from tkinter import messagebox
import psycopg2

def create_stock_page(parent):
    label = tk.Label(parent, text="Add Items to Database")
    label.pack()

    # Entry variables
    dealer_id_var = tk.StringVar()
    dealer_name_var = tk.StringVar()
    product_id_var = tk.StringVar()
    product_name_var = tk.StringVar()

    # Labels and Entry widgets
    tk.Label(parent, text="Dealer ID:").pack()
    dealer_id_entry = tk.Entry(parent, textvariable=dealer_id_var)
    dealer_id_entry.pack()

    tk.Label(parent, text="Dealer Name:").pack()
    dealer_name_entry = tk.Entry(parent, textvariable=dealer_name_var)
    dealer_name_entry.pack()

    tk.Label(parent, text="Product ID:").pack()
    product_id_entry = tk.Entry(parent, textvariable=product_id_var)
    product_id_entry.pack()

    tk.Label(parent, text="Product Name:").pack()
    product_name_entry = tk.Entry(parent, textvariable=product_name_var)
    product_name_entry.pack()

    # Button to add item to the database
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

            # Insert values into the dealers table
            cursor.execute("INSERT INTO dealers (id, name) VALUES (%s, %s) RETURNING id",
                           (dealer_id, dealer_name))

            # Fetch the last inserted dealer_id
            dealer_id = cursor.fetchone()[0]

            # Insert values into the products table with the foreign key dealer_id
            cursor.execute("INSERT INTO products (id, name, dealer_id) VALUES (%s, %s, %s)",
                           (product_id, product_name, dealer_id))

            connection.commit()
            connection.close()

            tk.messagebox.showinfo("Success", "Item added to database successfully!")

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {str(e)}")

    tk.Button(parent, text="Add to Database", command=add_to_database).pack()


if __name__ == "__main__":
    root = tk.Tk()
    create_stock_page(root)
    root.mainloop()
