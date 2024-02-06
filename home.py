from tkinter import*
from navbar import Navbar
from page1 import Page1
from page2 import Page2

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg="#DCF2F1")  # Replace "#00ff00" with your desired color code

def navigate_to_home():
    print("Navigate to Home")

def navigate_to_about():
    print("Navigate to About")

def navigate_to_contact():
    print("Navigate to Contact")

# Create the main window

root.title("Navbar Example")

# Create a navbar frame

navbar = Frame(root, bg="#365486")  # Set background color and height, replace with your desired color and height
navbar.pack(side="top", fill="x")

# Create buttons in the navbar
home_button = Button(navbar, text="Search",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=navigate_to_home)
home_button.pack(side="left")

stock_button = Button(navbar, text="Stock",width="30",bg="#365486",fg="#DCF2F1",height="2" ,command=navigate_to_about)
stock_button.pack(side="left")

cust_button = Button(navbar, text="Customers",bg="#365486",width="30",fg="#DCF2F1",height="2" , command=navigate_to_contact)
cust_button.pack(side="left")

deal_button = Button(navbar, text="Dealers",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=navigate_to_home)
deal_button.pack(side="left")

most_button = Button(navbar, text="Most Ordered",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=navigate_to_home)
most_button.pack(side="left")

offers_button = Button(navbar, text="Offers",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=navigate_to_home)
offers_button.pack(side="left")

acc_button = Button(navbar, text="My Account",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=navigate_to_home)
acc_button.pack(side="left")

navbar_height = 300  # Set your desired height
navbar.configure(height=navbar_height)

# Start the Tkinter event loop
root.mainloop()
