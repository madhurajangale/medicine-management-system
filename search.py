import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageOps
from category import create_category_page

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
    images = [
        'tablet.jpeg',
        'capsule.jpg',
        'syrup.jpeg',
        'cream.jpeg',
        'injection.jpeg',
        'others.jpeg'
    ]
    button_texts = ["Tablets", "Capsules", "Syrup", "Creams", "Injections", "Others"]

    # Dictionary to store frames
    frames = {}

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

        # Bind click event to the button
        button.config(command=lambda category=button_texts[i], frames=frames: on_button_click(category, frames))

        # Retain reference to the ImageTk object and frame
        canvas.image = image_tk
        frames[button_texts[i]] = frame

def on_button_click(category, frames):
    # Destroy other frames
    for key in frames:
        if key != category:
            frames[key].destroy()

    # Open a new window and execute code from category.py
    create_category_page(category)

if __name__ == "__main__":
    root = tk.Tk()
    create_home_page(root)
    root.mainloop()
