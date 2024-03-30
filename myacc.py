import tkinter as tk
from PIL import Image, ImageTk
import psycopg2
global username

def create_myacc_page(parent, username):
    # Function to display user data
    def display_user_data(username):
        # Connect to the database
        conn = psycopg2.connect(
            dbname="register",
            user="postgres",
            password="7177",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Fetch data for the specific user
        cursor.execute("SELECT name,username,staff_id,phone_number,email,age FROM user_data WHERE username = %s", (username,))
        user_data = cursor.fetchone()  # Assuming username is unique

        # Close the connection
        cursor.close()
        conn.close()

        if user_data:
            # Load and display the image
            image = Image.open("acc4.png")  # Replace with the actual path to your image
            image = image.resize((220, 220))
            
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(parent, image=photo)
            image_label.image = photo
            image_label.pack(pady=(100, 50))

            # Display user data
            user_info = f"Name: {user_data[0]}\n\nUsername: {user_data[1]}\n\nStaff ID: {user_data[2]}\n\nPhone No: {user_data[3]}\n\nEmail: {user_data[4]}\n\nAge: {user_data[5]}"
            user_label = tk.Label(parent, text=user_info, font=("Helvetica", 14))  # Left justify text
            user_label.pack(pady=5, padx=10)
            user_label.pack()
        else:
            error_label = tk.Label(parent, text="User not found")
            error_label.pack()

    # Call the function to display user data
    display_user_data(username)
