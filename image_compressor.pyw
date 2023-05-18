import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def compress_image():
    input_path = filedialog.askopenfilename(title="Select Input Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if input_path:
        output_directory = filedialog.askdirectory(title="Select Output Directory")
        if output_directory:
            image = Image.open(input_path).convert("RGB")
            output_file = os.path.join(output_directory, "compressed_image.jpg")
            image.save(output_file, optimize=True, quality=80)
            status_label.config(text="Image compressed successfully.", fg="green")
        else:
            status_label.config(text="Output directory not selected.", fg="red")
    else:
        status_label.config(text="Input image not selected.", fg="red")

# Create Tkinter root window
root = tk.Tk()
root.title("Image Compressor")

# Create GUI elements
label = tk.Label(root, text="Click the button to compress an image")
label.pack(pady=10)

compress_button = tk.Button(root, text="Compress", command=compress_image)
compress_button.pack(pady=5)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

# Start the main event loop
root.mainloop()
