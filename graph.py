import tkinter as tk
from tkinter import messagebox
import psycopg2
from datetime import date, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

def fetch_expiry_data():
    conn = psycopg2.connect(
        user="postgres",
        password="7177",
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

def plot_double_bar_graph(current_month_data, next_month_data):
    fig, ax = plt.subplots()
    
    categories = ['Tablets', 'Capsules', 'Syrup', 'Injections','Creams','Others']  # Specify the category names
    bar_width = 0.35
    index = range(len(categories))
    
    current_bars = ax.bar(index, [current_month_data[cat] for cat in categories], bar_width, label='Current Month', color='b')  # Blue color for current month
    next_bars = ax.bar([i + bar_width for i in index], [next_month_data[cat] for cat in categories], bar_width, label='Next Month', color='r')  # Red color for next month
    
    ax.set_xlabel('Category')
    ax.set_ylabel('Percentage')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(categories)
    ax.legend()
    
    ax.set_yticks(range(0, 101, 20))  # Set y-axis ticks at intervals of 20%
    
    # Add labels to the bars
    for bars in [current_bars, next_bars]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate('{}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    
    return fig



def check_offer_today(parent):
    expiry_data = fetch_expiry_data()
    current_month = date.today().month
    next_month = date.today().replace(day=28) + timedelta(days=4)  # Get the last day of the next month
    next_month_data = process_expiry_data(expiry_data, next_month.month)
    current_month_data = process_expiry_data(expiry_data, current_month)
    fig = plot_double_bar_graph(current_month_data, next_month_data)
    
    graph_window = tk.Toplevel()
    graph_window.title("Expiry Double Bar Graph")
    graph_canvas = FigureCanvasTkAgg(fig, master=graph_window)
    graph_canvas.draw()
    graph_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Center the window on the screen
    parent.update_idletasks()
    window_width = 800  # Adjusted width
    window_height = 600  # Adjusted height
    position_right = int(graph_window.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(graph_window.winfo_screenheight() / 2 - window_height / 2)
    graph_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

    # Close the PostgreSQL connection when the GUI is closed
    graph_window.protocol("WM_DELETE_WINDOW", graph_window.destroy)
    
    toolbar = NavigationToolbar2Tk(graph_canvas, graph_window)
    toolbar.update()
    toolbar.pack(side=tk.BOTTOM, fill=tk.BOTH)  # Pack the toolbar at the bottom of the window

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Expiry Notification System")
    root.configure(bg="#F0F0F0")

    # Call function to show the graph
    check_offer_today(root)

    root.mainloop()
