import tkinter as tk
from tkinter import ttk
import psycopg2

def create_dealer_page(parent):
    def fetch_data():
        try:
            conn = psycopg2.connect(
                database="register",
                user="postgres",
                password="7177",
                host="localhost",
                port="5432"
            )
            cur = conn.cursor()

            # Fetch dealers and their purchased products
            cur.execute("SELECT d.name, p.name FROM dealers d JOIN products p ON d.dealer_id = p.dealer_id")
            data = cur.fetchall()

            # Close cursor and connection
            cur.close()
            conn.close()

            return data
        except psycopg2.Error as e:
            print("Error fetching data from PostgreSQL:", e)
            return []

    def display_data(dealers):
        # Clear previous data if any
        tree.delete(*tree.get_children())

        if search_var.get().strip():  # Check if search query is not empty
            result_frame.pack(fill="both", expand=True)  # Display the result frame

            # Fetch data from PostgreSQL
            data = fetch_data()
            print("Fetched data:", data)  # Check if data is fetched correctly

            # Initialize a dictionary to store products by dealer
            dealer_products = {}

            # Organize data by dealer
            for dealer_name, product_name in data:
                if dealer_name not in dealer_products:
                    dealer_products[dealer_name] = []
                dealer_products[dealer_name].append(product_name)

            # Display dealers in the Treeview
            for dealer_name in sorted(dealers):
                if dealer_name in dealer_products:
                    dealer_row_id = tree.insert("", "end", text=dealer_name, tags=("dealer",))
                    for product_name in dealer_products[dealer_name]:
                        # Insert products under respective dealer rows but initially hide them
                        tree.insert(dealer_row_id, "end", text=product_name, tags=("product",))
                        tree.item(dealer_row_id, open=False)  # Hide product rows initially
        else:
            result_frame.pack_forget()  # Hide the result frame if search query is empty

    def search_dealer(event=None):
        query = search_var.get().lower().strip()
        dealers = [dealer for dealer in all_dealers if query in dealer.lower()]
        display_data(dealers)

    # Fetch all dealer names
    data = fetch_data()
    all_dealers = sorted(set([dealer_name for dealer_name, _ in data]))

    # Destroy existing widgets if any
    for widget in parent.winfo_children():
        widget.destroy()

    # Create a frame for the search bar
    search_frame = tk.Frame(parent)
    search_frame.pack(padx=10, pady=10, fill="x")

    # Search Bar
    search_var = tk.StringVar()
    search_var.set("Search Here")
    search_var.trace_add("write", lambda name, index, mode, sv=search_var: search_dealer())
    search_entry = ttk.Entry(search_frame, textvariable=search_var, width=40, font=("Arial", 14))  # Increase font size and width
    search_entry.pack(side="left", padx=(0, 5), fill="x", expand=True, ipady=10)
    search_entry.bind("<FocusIn>", lambda event: search_entry.select_range(0, tk.END))

    # Create a frame to display search results
    result_frame = tk.Frame(parent, bg="#DCF2F1")

    # Create a Treeview widget
    tree = ttk.Treeview(result_frame, columns=("Product Purchased",), show="tree",height=10)
    tree.heading("#0", text="Dealer Name / Product Purchased")
    tree.column("#0", width=300, anchor="center")
    tree.tag_configure("dealer", background="#0F1035",foreground="white", font=("Arial", 13, "bold"))  # Font size increased for dealer rows
    tree.tag_configure("product", background="#DCF2F1", font=("Arial", 13))
    tree.pack(padx=10, pady=10, fill="both", expand=True)

    # Add grid lines
    style = ttk.Style()
    style.configure("Treeview", background="#DCF2F1", foreground="black", rowheight=35, fieldbackground="#DCF2F1")
    style.map("Treeview", background=[('selected', '#365486')])

# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    create_dealer_page(root)
    root.mainloop()
