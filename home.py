from tkinter import *
from dealer import create_dealer_page
from page2 import create_stock_page
from page3 import create_home_page

def show_home_page():
    clear_current_page()
    create_home_page(main_frame)

def show_stock_page():
    clear_current_page()
    create_stock_page(main_frame)

def show_dealer_page():
    clear_current_page()
    create_dealer_page(main_frame)
    
def show_cust_page():
    clear_current_page()
    create_dealer_page(main_frame)
    
def show_ord_page():
    clear_current_page()
    create_dealer_page(main_frame)
    
def show_offer_page():
    clear_current_page()
    create_dealer_page(main_frame)
    
def show_acc_page():
    clear_current_page()
    create_dealer_page(main_frame)

def clear_current_page():
    for widget in main_frame.winfo_children():
        widget.destroy()
        


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
root.configure(bg="#DCF2F1")

root.title("Navbar Example")

navbar = Frame(root, bg="#365486")  # Set background color and height, replace with your desired color and height
navbar.pack(side="top", fill="x")

# Create buttons in the navbar
home_button = Button(navbar, text="Search",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=show_home_page)
home_button.pack(side="left")

stock_button = Button(navbar, text="Stock",width="30",bg="#365486",fg="#DCF2F1",height="2" ,command=show_stock_page)
stock_button.pack(side="left")

cust_button = Button(navbar, text="Customers",bg="#365486",width="30",fg="#DCF2F1",height="2" , command=show_home_page)
cust_button.pack(side="left")

deal_button = Button(navbar, text="Dealers",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=show_dealer_page)
deal_button.pack(side="left")

most_button = Button(navbar, text="Most Ordered",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=show_stock_page)
most_button.pack(side="left")

offers_button = Button(navbar, text="Offers",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=show_stock_page)
offers_button.pack(side="left")

acc_button = Button(navbar, text="My Account",bg="#365486",width="30",height="2",fg="#DCF2F1" , command=show_stock_page)
acc_button.pack(side="left")

navbar_height = 300  # Set your desired height
navbar.configure(height=navbar_height)




main_frame = Frame(root, bg="#DCF2F1")
main_frame.pack(fill="both", expand=True)



root.mainloop()
