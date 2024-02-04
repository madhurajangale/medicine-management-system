import psycopg2
from psycopg2 import sql
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFilter

# Function to insert data into the PostgreSQL database
def insert_into_database():
    # Get user input from the entry fields
    name=name_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    staff_id = staff_id_entry.get()
    phonenumber = phonenumber_entry.get()
    email = email_entry.get()
    age = age_entry.get()

    try:
        # Update the following parameters with your PostgreSQL connection details
        connection = psycopg2.connect(
            database="register",
            user="postgres",
            password="rujutamedhi@04",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        # Create a table if not exists
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_data (
            name VARCHAR(255),
	        username VARCHAR(20),
	        password VARCHAR(255),
	        staff_id VARCHAR(20),
            phonenumber VARCHAR(15),
            email VARCHAR(255),
            age INTEGER
        );
        """
        cursor.execute(create_table_query)

        # Insert data into the table
        insert_query = sql.SQL("""
            INSERT INTO user_data (name,username, password,staff_id,phonenumber, email,age)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """)
        cursor.execute(insert_query, (name, username, password,staff_id, phonenumber, email,age))

        connection.commit()
        messagebox.showinfo("Welcome!", "Account created successfully")

    except Exception as error:
        messagebox.showerror("Error", f"An error occurred: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()

# Create the main window

root = tk.Tk()
root.title("User Registration")
root.geometry('950x500+300+200')
root.resizable(False,False)
# Load the JPEG image and apply Gaussian blur filter
image = Image.open("registerfinal.jpeg")
#blurred_image = image.filter(ImageFilter.GaussianBlur(3))  # Adjust the blur radius as needed
#photo = ImageTk.PhotoImage(blurred_image)
photo = ImageTk.PhotoImage(image)

# Keep a reference to the PhotoImage object
#root.photo = photo
#Label(root,image=img,bg='#DCF2F1').place(x=2,y=50)
# Create a label to display the blurred image as the background
background_label = tk.Label(root, image=photo)
background_label.place(x=2, y=50)

# Create a container frame
container = tk.Frame(root,width=300,height=350 ,bg="#DCF2F1", highlightthickness=2, highlightbackground="#365486", highlightcolor="#365486")
container.place(x=620,y=70)

# Add heading "Register here"
heading = tk.Label(container, text="Register here", font=("Helvetica", 16, "bold"), bg="#DCF2F1")
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Set background colors of labels and entry fields
bg_color = "#7FC7D9"  # Light blue
label_bg_color = "#DCF2F1"  # Dark blue
tk.Label(container, text="Name:", bg=label_bg_color).grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(container, bg=bg_color)
name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Username:", bg=label_bg_color).grid(row=2, column=0, padx=5, pady=5)
username_entry = tk.Entry(container, bg=bg_color)
username_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Password:", bg=label_bg_color).grid(row=3, column=0, padx=5, pady=5)
password_entry = tk.Entry(container, show="*", bg=bg_color)
password_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Staff ID:", bg=label_bg_color).grid(row=4, column=0, padx=5, pady=5)
staff_id_entry = tk.Entry(container, bg=bg_color)
staff_id_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Phone Number:", bg=label_bg_color).grid(row=5, column=0, padx=5, pady=5)
phonenumber_entry = tk.Entry(container, bg=bg_color)
phonenumber_entry.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Email:", bg=label_bg_color).grid(row=6, column=0, padx=5, pady=5)
email_entry = tk.Entry(container, bg=bg_color)
email_entry.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

tk.Label(container, text="Age:", bg=label_bg_color).grid(row=7, column=0, padx=5, pady=5)
age_entry = tk.Entry(container, bg=bg_color)
age_entry.grid(row=7, column=1, padx=5, pady=5, sticky="ew")

# Button to insert data into the database
insert_button = tk.Button(container, text="Create Account", command=insert_into_database, bg="#0F1035", fg="white")  # Set button background color to dark blue and foreground color to white
insert_button.grid(row=8, columnspan=2, padx=5, pady=10, sticky="ew")

# Start the GUI event loop
root.mainloop()
