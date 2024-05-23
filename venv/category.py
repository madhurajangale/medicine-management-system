import tkinter as tk
from tkinter import font as tkFont
import psycopg2
from PIL import Image, ImageTk
import tkinter.ttk as ttk

def search_elements(event=None, category=None):
    search_query = entry.get().strip().lower()  # Get the search query from the Entry widget
    if search_query:
        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
                 user="postgres",
            password="#Shravani2509",
            host="localhost",
            port="5432",
            database="register"
                
            )
            cursor = conn.cursor()

            # Query to fetch product names matching the search query and category
            query = """
                SELECT name 
                FROM products 
                WHERE LOWER(name) LIKE %s AND category = %s
                ORDER BY name ASC
            """
            cursor.execute(query, ('%' + search_query + '%', category))
            results = cursor.fetchall()

            # Clear the existing search results
            listbox.delete(0, tk.END)

            # Display the search results in the listbox
            for result in results:
                listbox.insert(tk.END, result[0])

            # Show the listbox
            listbox.place(relx=0.5, rely=0.15, anchor="n")  # Adjust placement if necessary
        except psycopg2.Error as e:
            print("Error executing SQL query:", e)
    else:
        # Hide the listbox when search query is empty
        listbox.place_forget()

def show_product_details(event):
    # Get the index of the selected item
    selection = listbox.curselection()
    if selection:
        index = selection[0]

        # Get the name of the selected product
        selected_product = listbox.get(index)

        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(
            user="postgres",
            password="#Shravani2509",
            host="localhost",
            port="5432",
            database="register"
            )
            cursor = conn.cursor()

            # Query to fetch product details based on the selected product
            query = """
                SELECT * 
                FROM products 
                WHERE name = %s
            """
            cursor.execute(query, (selected_product,))
            product_details = cursor.fetchone()

            # Clear existing product details
            for widget in product_details_frame.winfo_children():
                widget.destroy()

            if product_details:
                # Add separators and display product details
                for key, value in zip(["name", "ID", "Rack Number", "Expiry Date", "Dealer id"], product_details[1:]):
                    ttk.Separator(product_details_frame, orient="horizontal").pack(fill="x", pady=5, padx=10)
                    detail_label = tk.Label(product_details_frame, text=f"{key}: {value}", font=("Helvetica", 12))
                    detail_label.pack(padx=10, pady=5, anchor="w")

                # Make the product details frame visible
                product_details_frame.place(relx=0.5, rely=0.7, anchor="center", width=400, height=280)  # Adjust placement as needed

        except psycopg2.Error as e:
            print("Error executing SQL query:", e)

def on_entry_click(event):
    """Function to handle click event on the search entry."""
    if entry.get() == 'Search here':
        entry.delete(0, tk.END)  # Delete the default text
        entry.config(fg='black')  # Change text color to black

def create_category_page(category):
    global entry, listbox, product_details_frame

    # Create a new window
    category_window = tk.Toplevel()

    # Load background image
    bg_image = Image.open("w2.png")
    bg_image = bg_image.resize((category_window.winfo_screenwidth(), category_window.winfo_screenheight()), Image.LANCZOS)  # Resize the image to fit the window
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a canvas to display the background image
    canvas = tk.Canvas(category_window, width=category_window.winfo_screenwidth(), height=category_window.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor="nw", image=bg_photo)

    # Add search bar
    entry_font = tkFont.Font(size=12)  # Font for the entry widget
    entry = tk.Entry(category_window, width=50, font=entry_font, fg='grey', bd=2, highlightbackground="#000000", highlightthickness=1)  # Add border
    entry.insert(0, 'Search here')  # Insert default text
    entry.bind("<FocusIn>", on_entry_click)  # Bind the click event
    entry.bind("<KeyRelease>", lambda event, category=category: search_elements(event, category))  # Bind the search function to text modification events
    entry.place(relx=0.5, rely=0.1, anchor="n")

    # Create a listbox to display search results
    listbox = tk.Listbox(category_window, width=50, height=10, font=entry_font, bd=2, highlightbackground="#000000", highlightthickness=1, bg="#FFFFFF")  # Add border and white background
    listbox.place(relx=0.5, rely=0.2, anchor="n")  # Adjust the rely parameter to reduce distance

    # Hide the listbox by default
    listbox.place_forget()

    # Create a frame to display product details
    product_details_frame = tk.Frame(category_window, bg="#FFFFFF", bd=2, highlightbackground="#000000", highlightthickness=1)  # White background with border

    # Ensure the image is retained by keeping a reference
    canvas.bg_photo = bg_photo

    # Bind the listbox selection event to show product details
    listbox.bind("<<ListboxSelect>>", show_product_details)

    # Finally, start the main loop
    category_window.mainloop()

# Example usage:
if __name__ == "__main__":
    create_category_page("Tablet")  # Example category