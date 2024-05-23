import tkinter as tk
from tkinter import messagebox
import psycopg2
from datetime import date

def check_expiry_notifications(cursor):
    today = date.today()

    # Retrieve products that expire today
    cursor.execute('SELECT name FROM products WHERE expiry_date = %s', (today,))
    expiring_products = cursor.fetchall()

    if expiring_products:
        products_list = "\n".join([product[0] for product in expiring_products])
        messagebox.showinfo("Expiry Notification", f"The following products will expire today:\n\n{products_list}")
    else:
        messagebox.showinfo("Expiry Notification", "No products expiring today.")

def create_notify_page(cursor):
    # GUI setup
    root = tk.Tk()
    root.title("Expiry Notification System")
    root.configure(bg="#F0F0F0")

    def check_expiry():
        check_expiry_notifications(cursor)

    btn_check_expiry = tk.Button(root, text="Check Expiry Notifications", command=check_expiry, bg="#2196F3", fg="white", font=("Helvetica", 20))
    btn_check_expiry.grid(row=0, column=0, padx=10, pady=10)

    # Center the window on the screen
    root.update_idletasks()
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
    root.geometry(f"+{position_right}+{position_down}")

    root.mainloop()

    # Close the PostgreSQL connection when the GUI is closed
    cursor.close()
    conn.close()

if __name__ == "__main__":
    conn = psycopg2.connect(
        user="postgres",
        password="#Shravani2509",
        host="localhost",
        port="5432",
        database="register"
    )
    cursor = conn.cursor()
    create_notify_page(cursor)
