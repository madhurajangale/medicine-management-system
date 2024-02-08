import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps

def create_circular_image(image_path, output_path, size):
    # Open the original image
    original_image = Image.open(image_path)

    # Resize the image if desired
    original_image = original_image.resize((size, size), resample=Image.BICUBIC)

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply the circular mask to the original image
    circular_image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    circular_image.paste(original_image, (0, 0), mask)

    # Save the circular image
    circular_image.save(output_path)

def is_within_circle(x, y, center_x, center_y, radius):
    return (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2

def on_canvas_click(event):
    global search_bar
    if is_within_circle(event.x, event.y, canvas_width // 2, canvas_height // 2, radius):
        search_bar.pack()  # Pack the search bar when the circular image is clicked

def create_home_page(parent):
    global canvas_width, canvas_height, radius, search_bar

    # Create a circular image
    create_circular_image('dealer2.jpg', 'dealer2_circular.png', 200)

    # Load the circular image as an ImageTk object
    image = Image.open('dealer2_circular.png')
    image = ImageOps.fit(image, (200, 200))
    image_tk = ImageTk.PhotoImage(image)

    # Create a canvas to display the image
    canvas_width, canvas_height = image_tk.width(), image_tk.height()
    canvas = tk.Canvas(parent, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Add the image to the canvas
    canvas.create_image(canvas_width // 2, canvas_height // 2, image=image_tk)

    # Retain reference to the ImageTk object
    canvas.image = image_tk

    # Bind click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    # Create search bar (initially hidden)
    search_bar = tk.Entry(parent)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Home Page")

    # Set global variables
    canvas_width, canvas_height, radius = 200, 200, 100
    search_bar = None

    # Create the home page
    create_home_page(root)

    root.mainloop()
