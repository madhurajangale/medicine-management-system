import tkinter as tk
from tkinter import Canvas, Toplevel
from tkinter import messagebox
import psycopg2
from datetime import date, timedelta
from collections import defaultdict

def fetch_expiry_data():
    conn = psycopg2.connect(
        user="postgres",
        password="#Shravani2509",
        host="localhost",
        port="5432",
        database="register"
    )
    cursor = conn.cursor()

    # Fetch month and category for each product
    cursor.execute("SELECT EXTRACT(month FROM expiry_date) AS month, category FROM products")
    expiry_data = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return expiry_data

def process_expiry_data(expiry_data, target_month):
    # Group expiry data by category and month
    category_month_expiry = defaultdict(int)
    
    for month, category in expiry_data:
        if month == target_month:
            category_month_expiry[category] += 1
    
    return category_month_expiry

def create_bars(canvas, data, color, bar_width, categories):
    total = sum(data.values())
    x_offset = 50
    y_scale = 10  # Adjust the scale for bigger plots
    font_size = 12  # Adjust font size
    
    for i, (category, value) in enumerate(data.items()):
        x0 = x_offset + i * 100
        y0 = 600  # Adjust the y position for bigger plots
        x1 = x0 + bar_width
        y1 = y0 - value * y_scale
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.create_text((x0 + x1) / 2, y0 + 20, text=f"{category}\n({value})", anchor="n", font=("Helvetica", font_size))

def check_offer_today(parent):
    expiry_data = fetch_expiry_data()
    current_month = date.today().month
    next_month = date.today().replace(day=28) + timedelta(days=4)  # Get the last day of the next month
    next_month_data = process_expiry_data(expiry_data, next_month.month)
    current_month_data = process_expiry_data(expiry_data, current_month)
    
    canvas_width = 800  # Adjust canvas width
    canvas_height = 700  # Adjust canvas height
    
    graph_window = Toplevel(parent)
    graph_window.title("Expiry Double Bar Graph")
    
    canvas = Canvas(graph_window, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()
    
    # Draw bars for current month
    create_bars(canvas, current_month_data, "blue", 50, ['Tablets', 'Capsules', 'Syrup', 'Injections', 'Creams', 'Others'])
    
    # Draw bars for next month
    create_bars(canvas, next_month_data, "red", 50, ['Tablets', 'Capsules', 'Syrup', 'Injections', 'Creams', 'Others'])
    
    # Center the window on the screen
    graph_window.update_idletasks()
    window_width = graph_window.winfo_width()
    window_height = graph_window.winfo_height()
    position_right = int(graph_window.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(graph_window.winfo_screenheight() / 2 - window_height / 2)
    graph_window.geometry(f"+{position_right}+{position_down}")

    # Close the PostgreSQL connection when the GUI is closed
    graph_window.protocol("WM_DELETE_WINDOW", graph_window.destroy)

if __name__ == "__main__":
    # If you want to test this script independently
    root = tk.Tk()
    root.title("Expiry Notification System")
    root.configure(bg="#F0F0F0")

    # Call function to show the graph
    check_offer_today(root)

    root.mainloop()
