import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps

def create_circular_image(image_path, output_path, size):
    try:
        # Open the original image
        original_image = Image.open(image_path)

        # Resize the image if desired
        original_image = original_image.resize((size, size), resample=Image.BICUBIC)

        # Create a circular mask with a slightly larger radius
        mask_size = (size, size)
        mask = Image.new("L", mask_size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        # Apply the circular mask to the original image
        circular_image = Image.new("RGBA", mask_size, (255, 255, 255, 0))
        circular_image.paste(original_image, (0, 0), mask)

        # Replace white areas with background color (#DCF2F1)
        background_color = (220, 242, 241, 255)  # RGB values for #DCF2F1
        for x in range(size):
            for y in range(size):
                r, g, b, a = circular_image.getpixel((x, y))
                if r == 255 and g == 255 and b == 255:
                    circular_image.putpixel((x, y), background_color)

        # Save the circular image
        circular_image.save(output_path)
    except Exception as e:
        print("Error creating circular image:", e)

def create_home_page(parent):
    global canvas_width, canvas_height, radius

    images = [
        'tablet.jpeg',
        'capsule.jpg',
        'syrup.jpeg',
        'cream.jpeg',
        'injection.jpeg',
        'others.jpeg'
    ]
    button_texts = ["Tablets", "Capsule", "Syrup", "Cream", "Injection", "Others"]

    # Create a frame to hold all the images
    main_frame = tk.Frame(parent, bg="#DCF2F1")
    main_frame.pack(expand=True)

    # Create frames for each image and button pair
    for i, image_path in enumerate(images):
        row = i // 3  # Determine row
        col = i % 3   # Determine column

        # Create a circular image
        create_circular_image(image_path, f'dealer{i+1}_circular.png', 200)

        # Load the circular image as an ImageTk object
        image = Image.open(f'dealer{i+1}_circular.png')
        image = ImageOps.fit(image, (200, 200))
        image_tk = ImageTk.PhotoImage(image)

        # Create a frame to hold the image and button
        frame = tk.Frame(main_frame, bg="#DCF2F1")  # Set background color to #DCF2F1
        frame.grid(row=row, column=col, padx=30, pady=10)

        # Create a canvas to display the image with background color
        canvas = tk.Canvas(frame, width=image_tk.width(), height=image_tk.height(), bg="#DCF2F1")
        canvas.pack()
        canvas.create_image(image_tk.width() // 2, image_tk.height() // 2, image=image_tk)

        # Create a button below the image with background color
        button = tk.Button(frame, text=button_texts[i], background="#DCF2F1", pady=10, padx=20)
        button.pack(pady=(0, 10))  # Add padding only below the button

        # Bind click event to the canvas
        canvas.bind("<Button-1>", lambda event, search_bar=button: on_canvas_click(event, search_bar))

        # Retain reference to the ImageTk object
        canvas.image = image_tk

def on_canvas_click(event, search_bar):
    search_bar.pack()  # Pack the search bar when the circular image is clicked

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Home Page")

    # Set global variables
    canvas_width, canvas_height, radius = 200, 200, 100

    # Create the home page
    create_home_page(root)

    root.mainloop()
