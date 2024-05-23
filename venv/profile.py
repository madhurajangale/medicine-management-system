import tkinter as tk
from tkinter import messagebox
import psycopg2
from PIL import Image, ImageTk

def display_profile(username):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="#Shravani2509",
            host="localhost",
            port="5432",
            database="register"
        )

        cursor = connection.cursor()

        # Retrieve user data from the database
        cursor.execute("SELECT * FROM user_data WHERE username = %s", (username,))
        user_data = cursor.fetchone()

        if user_data:
            # Create a new window for displaying profile
            profile_window = tk.Toplevel()
            profile_window.title("My Profile")
            profile_window.geometry('400x300')
            profile_window.resizable(False, False)

            # Display user details
            tk.Label(profile_window, text="Name: " + user_data[0]).pack()
            tk.Label(profile_window, text="Username: " + user_data[1]).pack()
            tk.Label(profile_window, text="Staff ID: " + user_data[3]).pack()
            tk.Label(profile_window, text="Phone Number: " + user_data[4]).pack()
            tk.Label(profile_window, text="Email: " + user_data[5]).pack()
            tk.Label(profile_window, text="Age: " + str(user_data[6])).pack()
        else:
            messagebox.showerror("Error", "User not found")

    except Exception as error:
        messagebox.showerror("Error", f"An error occurred: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()

# Function to open "My Profile" page
def open_profile():
    username = username_entry.get()
    if username:
        display_profile(username)
    else:
        messagebox.showerror("Error", "Please enter your username")

# Create the main window
root = tk.Tk()
root.title("My Profile")
root.geometry('300x150')
root.resizable(False, False)

# Set background color
root.configure(bg="#DCF2F1")

# Create a frame for widgets
frame = tk.Frame(root, bg="#DCF2F1")
frame.pack(padx=20, pady=20)

# Add a label and entry field for username
tk.Label(frame, text="Username:", bg="#DCF2F1").grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(frame, bg="#7FC7D9")
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Add a button to open "My Profile" page
open_button = tk.Button(frame, text="Open Profile", command=open_profile, bg="#0F1035", fg="white")
open_button.grid(row=1, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
