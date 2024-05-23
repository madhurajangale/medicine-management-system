import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_home_page(parent):
    # Function to create circular buttons with images
    
    def create_circular_button(canvas, x, y, image_path, command):
        # Load and resize image
        img = Image.open(image_path)
        img = img.resize((70, 70), Image.LANCZOS)  # Using LANCZOS resampling method
        photo = ImageTk.PhotoImage(img)

        # Draw circular shape
        button_size = 80
        canvas.create_oval(50, 50, 50, 50, fill="#DCF2F1", outline="black")

        # Place resized image inside the circular button
        canvas.create_image(x + button_size // 2, y + button_size // 2, image=photo)

        # Create button and bind command
        button = tk.Button(canvas, command=command, image=photo, width=button_size, height=button_size, bd=0, bg="white")
        button.image = photo  # Keep a reference to avoid garbage collection
        canvas.create_window(x + button_size // 2, y + button_size // 2, window=button)

    # Create Canvas widget
    canvas = tk.Canvas(parent, width=1500, height=900, bg='#DCF2F1')
    canvas.pack()

    # Create circular buttons with images
    create_circular_button(canvas, 50, 50, "homeimg.png", command1)
    create_circular_button(canvas, 200, 50, "homeimg.png", command2)
    create_circular_button(canvas, 350, 50, "homeimg.png", command3)
    create_circular_button(canvas, 50, 150, "homeimg.png", command4)
    create_circular_button(canvas, 200, 150, "homeimg.png", command5)
    create_circular_button(canvas, 350, 150, "homeimg.png", command6)

# Example command functions for buttons
def command1():
    print("Button 1 clicked")

def command2():
    print("Button 2 clicked")

def command3():
    print("Button 3 clicked")

def command4():
    print("Button 4 clicked")

def command5():
    print("Button 5 clicked")

def command6():
    print("Button 6 clicked")