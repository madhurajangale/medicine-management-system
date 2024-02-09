import tkinter as tk
from tkinter import ttk
import psycopg2

def create_dealer_page(parent):
    def fetch_data():
        try:
            conn = psycopg2.connect(
                database="dealer",
                user="postgres",
                password="rujutamedhi@04",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()

            # Fetch dealers and their purchased products
            cur.execute("SELECT d.name, p.name FROM dealers d JOIN products p ON d.id = p.dealer_id")
            data = cur.fetchall()

            # Close cursor and connection
            cur.close()
            conn.close()

            return data
        except psycopg2.Error as e:
            print("Error fetching data from PostgreSQL:", e)
            return []

    def display_data():
        # Fetch data from PostgreSQL
        data = fetch_data()
        print("Fetched data:", data)  # Check if data is fetched correctly

        # Clear previous data if any
        for row in tree.get_children():
            tree.delete(row)

        # Initialize a dictionary to store products by dealer
        dealer_products = {}

        # Organize data by dealer
        for dealer_name, product_name in data:
            if dealer_name not in dealer_products:
                dealer_products[dealer_name] = []
            dealer_products[dealer_name].append(product_name)

        # Display dealers in the Treeview
        for dealer_name, products in dealer_products.items():
            dealer_row_id = tree.insert("", "end", text=dealer_name, tags=("dealer",))
            tree.item(dealer_row_id, open=True)  # Open the dealer row
            for product_name in products:
                # Insert products under respective dealer rows but initially hide them
                tree.insert(dealer_row_id, "end", text=product_name, tags=("product",))
                tree.item(dealer_row_id, open=False)  # Hide product rows initially

    # Heading "Dealers"
    heading_label = tk.Label(parent, text="Dealers", bg="#DCF2F1", fg="#365486", font=("Helvetica", 30, "bold"))
    heading_label.pack(pady=20)

    # Create a frame for the Treeview widget
    frame = tk.Frame(parent, bg="#365486")  # Set background color
    frame.pack(fill="both", expand=True)

    # Create a Treeview widget
    tree = ttk.Treeview(frame, columns=("Product Purchased",), show="tree")
    tree.heading("#0", text="Dealer Name / Product Purchased")
    tree.column("#0", width=300, anchor="center")
    tree.tag_configure("dealer", background="#0F1035",foreground="white")  # Light blue background for dealer rows
    tree.tag_configure("product", background="#DCF2F1")
    tree.pack(padx=400, pady=15, fill="both", expand=True)

    # Add grid lines
    style = ttk.Style()
    style.configure("Treeview", background="#DCF2F1", foreground="black", rowheight=25, fieldbackground="#DCF2F1")
    style.map("Treeview", background=[('selected', '#365486')])

    # Bind a function to the Treeview to display products when a dealer is clicked
    tree.bind("<Button-1>", lambda event: display_data())

    # Fetch and display data directly when the code is run
    display_data()

# Create the main Tkinter window

