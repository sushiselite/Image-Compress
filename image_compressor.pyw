import os
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from PIL import Image

def import_image():
    input_path = filedialog.askopenfilename(title="Select Input Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if input_path:
        input_path_entry.delete(0, tk.END)
        input_path_entry.insert(0, input_path)

def select_output_directory():
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    if output_directory:
        output_path_entry.delete(0, tk.END)
        output_path_entry.insert(0, output_directory)

def compress_image():
    input_path = input_path_entry.get()
    output_directory = output_path_entry.get()

    if input_path and output_directory:
        image = Image.open(input_path).convert("RGB")
        output_file = os.path.join(output_directory, "compressed_image.jpg")

        progress_bar.config(value=0)
        progress_bar.update()

        image.save(output_file, optimize=True, quality=80)

        progress_bar.config(value=100)
        progress_bar.update()

        status_label.config(text="Image compressed successfully.", fg="green")
    else:
        status_label.config(text="Input image or output directory not selected.", fg="red")

# Create Tkinter root window
root = tk.Tk()
root.title("Image Compressor")

# Set window background color
root.configure(bg="#F8F8F8")

# Create GUI elements
welcome_label = tk.Label(root, text="Welcome to Image Compressor", font=("Arial", 16, "bold"), bg="#F8F8F8")
welcome_label.pack(pady=10)

input_label = tk.Label(root, text="Input Image Path:", font=("Arial", 12), bg="#F8F8F8")
input_label.pack(pady=5)

input_path_entry = tk.Entry(root, width=50)
input_path_entry.pack(pady=5)

import_button = tk.Button(root, text="Import", command=import_image)
import_button.pack(pady=5)

output_label = tk.Label(root, text="Output Directory:", font=("Arial", 12), bg="#F8F8F8")
output_label.pack(pady=5)

output_path_entry = tk.Entry(root, width=50)
output_path_entry.pack(pady=5)

output_button = tk.Button(root, text="Output", command=select_output_directory)
output_button.pack(pady=5)

compress_button = tk.Button(root, text="Compress", command=compress_image, font=("Arial", 12))
compress_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="green", bg="#F8F8F8")
status_label.pack(pady=10)

progress_label = tk.Label(root, text="Progress:", font=("Arial", 12), bg="#F8F8F8")
progress_label.pack(pady=5)

progress_bar = Progressbar(root, length=200, mode="determinate")
progress_bar.pack(pady=5)

# Start the main event loop
root.mainloop()
