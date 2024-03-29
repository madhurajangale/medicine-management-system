import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import psycopg2
from datetime import datetime

def create_stock_page(parent):
    label = tk.Label(parent, text="Add Items to Database", font=("Cambria", 16))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    # Entry variables
    dealer_id_var = tk.StringVar()
    dealer_name_var = tk.StringVar()
    product_id_var = tk.StringVar()
    product_name_var = tk.StringVar()
    expiry_date_var = tk.StringVar()
    category_var = tk.StringVar()
    rack_no_var = tk.StringVar()
    units_var = tk.StringVar()

    # Labels and Entry widgets using grid
    tk.Label(parent, text="Dealer ID:", font=("Cambria", 20)).grid(row=1, column=0, padx=10, pady=5)
    dealer_id_entry = tk.Entry(parent, textvariable=dealer_id_var, font=("Cambria", 20), bg="SystemButtonFace")
    dealer_id_entry.grid(row=1, column=1, padx=10, pady=5)

    # Rest of the labels and entries...

    # Function to add item to the database...
    
    # Function to view products...

    # Function to update stock
    def update_stock():
        update_window = tk.Toplevel(parent)
        update_window.title("Update Stock")
        
        window_width = 600
        window_height = 400
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2
        geometry_string = f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}"
        update_window.geometry(geometry_string)
        # Function to search for the product
        def search_product():
            search_term = search_var.get()
            try:
                connection = psycopg2.connect(
                    database="register",
                    user="postgres",
                    password="7177",
                    host="localhost",
                    port="5432"
                )
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM products WHERE name ILIKE %s", ('%' + search_term + '%',))
                product = cursor.fetchone()
                connection.close()

                if product:
                    fields = [ "Product Name","Product id","Rack No", "Expiry Date","Dealer ID", "Category",  "Units"]
                    for i, field in enumerate(fields):
                        tk.Label(update_window, text=field + ":", font=("Cambria", 12)).grid(row=i+1, column=0, padx=10, pady=5)
                        entry = tk.Entry(update_window, font=("Cambria", 12))
                        entry.insert(0, product[i+1])  # Fill current value
                        entry.grid(row=i+1, column=1, padx=10, pady=5)
                        entry_fields.append(entry)

                    # Function to update stock in the database
                    def update_stock_in_db():
                        new_values = [entry.get() for entry in entry_fields] 
                        print("New values:", new_values)
                        print("Product ID:", new_values[2]) 
                        try:
                            connection = psycopg2.connect(
                                database="register",
                                user="postgres",
                                password="7177",
                                host="localhost",
                                port="5432"
                            )
                            cursor = connection.cursor()
                            expiry_date = new_values[3]
        # Ensure expiry_date is properly formatted as YYYY-MM-DD
                            expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').date()
                            cursor.execute("UPDATE products SET name=%s, pid=%s, rack_no=%s, expiry_date=CAST(%s AS DATE), dealer_id=%s, category=%s, units=%s WHERE pid=%s",
                                          (new_values[0], new_values[1], new_values[2], expiry_date, int(new_values[4]), new_values[5], int(new_values[6]), new_values[1]))

                            connection.commit()
                            connection.close()
                            tk.messagebox.showinfo("Success", "Stock updated successfully!")
                            update_window.destroy()
                        except Exception as e:
                            tk.messagebox.showerror("Error", f"Error updating stock: {str(e)}")

                    # Button to update stock
                    update_button = tk.Button(update_window, text="Update Product", command=update_stock_in_db, font=("Cambria", 12))
                    update_button.grid(row=len(fields) + 1, columnspan=2, padx=10, pady=5)
                else:
                    tk.messagebox.showinfo("Product Not Found", "No product found with that name.")

            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {str(e)}")

        search_var = tk.StringVar()
        tk.Label(update_window, text="Enter Product Name:", font=("Cambria", 12)).grid(row=0, column=0, padx=10, pady=5)
        search_entry = tk.Entry(update_window, textvariable=search_var, font=("Cambria", 12))
        search_entry.grid(row=0, column=1, padx=10, pady=5)

    # Button to search for product
        tk.Button(update_window, text="Search", command=search_product, font=("Cambria", 12)).grid(row=0, column=2, padx=10, pady=5)

    # List to store entry fields for each product detail
        entry_fields = []

        
    tk.Label(parent, text="Dealer Name:", font=("Cambria", 20)).grid(row=2, column=0, padx=10, pady=5)
    dealer_name_entry = tk.Entry(parent, textvariable=dealer_name_var, font=("Cambria", 20), bg="SystemButtonFace")
    dealer_name_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(parent, text="Product ID:", font=("Cambria", 20)).grid(row=3, column=0, padx=10, pady=5)
    product_id_entry = tk.Entry(parent, textvariable=product_id_var, font=("Cambria", 20), bg="SystemButtonFace")
    product_id_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(parent, text="Product Name:", font=("Cambria", 20)).grid(row=4, column=0, padx=10, pady=5)
    product_name_entry = tk.Entry(parent, textvariable=product_name_var, font=("Cambria", 20), bg="SystemButtonFace")
    product_name_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(parent, text="Expiry Date (YYYY-MM-DD):", font=("Cambria", 20)).grid(row=5, column=0, padx=10, pady=5)
    expiry_date_entry = tk.Entry(parent, textvariable=expiry_date_var, font=("Cambria", 20), bg="SystemButtonFace")
    expiry_date_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(parent, text="Category:", font=("Cambria", 20)).grid(row=6, column=0, padx=10, pady=5)
    category_entry = tk.Entry(parent, textvariable=category_var, font=("Cambria", 20), bg="SystemButtonFace")
    category_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(parent, text="Rack No:", font=("Cambria", 20)).grid(row=7, column=0, padx=10, pady=5)
    rack_no_entry = tk.Entry(parent, textvariable=rack_no_var, font=("Cambria", 20), bg="SystemButtonFace")
    rack_no_entry.grid(row=7, column=1, padx=10, pady=5)
    
    tk.Label(parent, text="Units:", font=("Cambria", 20)).grid(row=8, column=0, padx=10, pady=5)
    units_entry = tk.Entry(parent, textvariable=units_var, font=("Cambria", 20), bg="SystemButtonFace")
    units_entry.grid(row=8, column=1, padx=10, pady=5)

    # Function to add item to the database
    def add_to_database():
        try:
            connection = psycopg2.connect(
                database="register",
                user="postgres",
                password="7177",
                host="localhost",
                port="5432"
            )

            cursor = connection.cursor()

            # Retrieve values from entry widgets
            dealer_id = dealer_id_var.get()
            dealer_name = dealer_name_var.get()
            product_id = product_id_var.get()
            product_name = product_name_var.get()
            expiry_date = expiry_date_var.get()
            category = category_var.get()
            rack_no = rack_no_var.get()
            units = units_var.get()

            cursor.execute("INSERT INTO dealers (dealer_id, name) VALUES (%s, %s) RETURNING dealer_id",
                           (dealer_id, dealer_name))

            dealer_id = cursor.fetchone()[0]

            cursor.execute("INSERT INTO products (pid, name, dealer_id, expiry_date, category, rack_no,units) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (product_id, product_name, dealer_id, expiry_date, category, rack_no,units))

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
                password="7177",
                host="localhost",
                port="5432"
            )

            cursor = connection.cursor()

            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()

            products_listbox = tk.Listbox(new_window, height=10, width=50, font=("Cambria", 12))
            products_listbox.pack(padx=10, pady=10)

            for product in products:
                products_listbox.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Dealer ID: {product[2]}, Expiry Date: {product[3]}, Category: {product[4]}, Rack No: {product[5]},Units: {product[6]}")

            connection.close()

        except Exception as e:
            tk.messagebox.showerror("Error", f"Error: {str(e)}")

    # Buttons
    tk.Button(parent, text="Add to Database", command=add_to_database, font=("Cambria", 20)).grid(row=9, column=0, columnspan=2, pady=10)
    tk.Button(parent, text="Update Stock", command=update_stock, font=("Cambria", 20)).grid(row=11, column=0, columnspan=2, pady=10)
    tk.Button(parent, text="View Products", command=view_products, font=("Cambria", 20)).grid(row=10, column=0, columnspan=2, pady=10)

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

    root.attributes('-transparentcolor', 'gray')
    root.geometry(f"{desktop_width}x{desktop_height}")

if __name__ == "__main__":
    root = tk.Tk()

    set_bg_image(root)
    create_stock_page(root)
    root.mainloop()
