import tkinter as tk
from tkinter import *
from tkinter import messagebox
import psycopg2
from datetime import date
from dealer import create_dealer_page
from page2 import create_stock_page
from myacc import create_myacc_page
from search import create_home_page
from notify import check_expiry_notifications
from PIL import Image, ImageTk

def show_home_page():
    clear_current_page()
    bg_label.pack_forget() 
    # Call the function to create the home page from the search.py file
    create_home_page(main_frame)

def show_stock_page():
    clear_current_page()
    bg_label.pack_forget() 
    # Call the function to create the stock page from the page2.py file
    create_stock_page(main_frame)

def show_dealer_page():
    clear_current_page()
    bg_label.pack_forget() 
    # Call the function to create the dealer page from the dealer.py file
    create_dealer_page(main_frame)
    
def show_myacc_page(username):
    clear_current_page()
    bg_label.pack_forget() 
    # Call the function to create the My Account page from the myacc.py file
    create_myacc_page(main_frame, username)
 
def show_offer_page():
    clear_current_page()
    bg_label.pack_forget() 
    # Call the function to create the Offer page from the dealer.py file
    #check_offer_today(main_frame)

def show_expiry_today():
    clear_current_page()
    bg_label.pack_forget() 
    # Connect to the database
    conn = psycopg2.connect(
         user="postgres",
            password="#Shravani2509",
            host="localhost",
            port="5432",
            database="register"
    )
    cursor = conn.cursor()

    # Call the function to check expiry notifications from notify.py
    check_expiry_notifications(cursor)

    # Close the cursor and connection
    cursor.close()
    conn.close()

def clear_current_page():
    for widget in main_frame.winfo_children():
        widget.destroy()

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg="#DCF2F1")
root.title("Navbar Example")

navbar = Frame(root, bg="#365486")
navbar.pack(side="top", fill="x")

medicino_label = Label(navbar, text="Medicine Management", bg="#365486", fg="#DCF2F1", font=("Baskerville", 16))
medicino_label.pack(side="left", padx=40)

home_button = Button(navbar, text="Search", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=show_home_page)
home_button.pack(side="left")

stock_button = Button(navbar, text="Stock", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=show_stock_page)
stock_button.pack(side="left")

deal_button = Button(navbar, text="Dealers", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=show_dealer_page)
deal_button.pack(side="left")

graph_button = Button(navbar, text="Graph", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=show_offer_page)
graph_button.pack(side="left")

check_expiry_button = Button(navbar, text="Check Expiry Today", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=show_expiry_today)
check_expiry_button.pack(side="left")

# Assuming username is retrieved and stored in a variable called 'username'
# Configure the "My acc" button to call show_myacc_page with the username
u = "your_username"  # Replace "your_username" with the actual username
cust_button = Button(navbar, text="My account", bg="#365486", width="16", height="2", fg="#DCF2F1", font=("Baskerville", 16), command=lambda: show_myacc_page(u))
cust_button.pack(side="left")
    
navbar_height = 300
navbar.configure(height=navbar_height)

main_frame = Frame(root, bg="#DCF2F1")
main_frame.pack(fill="both", expand=True)

def set_bg_image():
    global photo
    desktop_width = root.winfo_screenwidth()
    desktop_height = root.winfo_screenheight()

    image = Image.open(r"w2.png")
    image = image.resize((desktop_width, desktop_height))

    alpha = Image.new('L', image.size, 200)
    image.putalpha(alpha)

    photo = ImageTk.PhotoImage(image)
    bg_label.config(image=photo)
    bg_label.image = photo

bg_label = tk.Label(root)
bg_label.pack(fill="both", expand=True)
set_bg_image()

root.mainloop()
