import tkinter as tk
from tkinter import ttk
import psycopg2

# Function to fetch data from PostgreSQL database
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

# Function to display data in the Tkinter window
def display_data():
    # Fetch data from PostgreSQL
    data = fetch_data()
    print("Fetched data:", data)  # Check if data is fetched correctly

    # Clear previous data if any
    for row in tree.get_children():
        tree.delete(row)

    # Display data in the Treeview
    current_dealer = None
    for dealer_name, product_name in data:
        if dealer_name != current_dealer:
            # Insert dealer name and first product in the same row
            dealer_row_id = tree.insert("", "end", text=dealer_name, tags=("dealer",))
            tree.item(dealer_row_id, open=True)  # Open the dealer row
            product_row_id = tree.insert(dealer_row_id, "end", text=product_name, tags=("product",))
            current_dealer = dealer_name
        else:
            # Insert subsequent products of the same dealer in rows below
            tree.insert(dealer_row_id, "end", text=product_name, tags=("product",))

# Function to open a new window
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x200")
    new_window.mainloop()

# Function to handle navigation to home
def navigate_to_home():
    print("Navigate to Home")

# Function to handle navigation to about
def navigate_to_about():
    print("Navigate to About")

# Function to handle navigation to contact
def navigate_to_contact():
    print("Navigate to Contact")

# Create Tkinter window
root = tk.Tk()
root.title("Dealer Products")
root.geometry("800x600") # Set initial size of the window
root.configure(bg="#7FC7D9")  # Set background color

# Create the navbar frame
navbar = tk.Frame(root, bg="#365486", height=50)
navbar.pack(side="top", fill="x")

# Create buttons in the navbar
buttons = [
    ("Search", navigate_to_home),
    ("Stock", navigate_to_about),
    ("Customers", navigate_to_contact),
    ("Dealers", navigate_to_home),
    ("Most Ordered", navigate_to_home),
    ("Offers", navigate_to_home),
    ("My Account", navigate_to_home)
]

for text, command in buttons:
    btn = tk.Button(navbar, text=text, bg="#365486", fg="#DCF2F1", height=2, width=15, command=command)
    btn.pack(side="left", padx=5, pady=5)

# Heading "Dealers"
heading_label = tk.Label(root, text="Dealers",bg="#7FC7D9", fg="#365486", font=("Helvetica", 30, "bold"))
heading_label.pack(pady=20)

# Create a frame for the Treeview widget
frame = tk.Frame(root, bg="#7FC7D9")  # Set background color
frame.pack(fill="both", expand=True)

# Create a Treeview widget
tree = ttk.Treeview(frame, columns=("Product Purchased",), show="tree")
tree.heading("#0", text="Dealer Name / Product Purchased")
tree.column("#0", width=300, anchor="center")
tree.tag_configure("dealer", background="#b0c4de")  # Light blue background for dealer rows
tree.tag_configure("product", background="#dcdcdc")
tree.pack(padx=400, pady=15, fill="both", expand=True)

# Add grid lines
style = ttk.Style()
style.configure("Treeview", background="#DCF2F1", foreground="black", rowheight=25, fieldbackground="#DCF2F1")
style.map("Treeview", background=[('selected', '#365486')])

# Fetch and display data directly when the code is run
display_data()

# Create a plus button to open a new window
plus_button = tk.Button(root, text="+", command=open_new_window, width=5, height=2, bg="#365486", fg="#DCF2F1")
plus_button.place(relx=1, rely=1, anchor="se", x=-420, y=-40)

# Display the window
root.mainloop()
