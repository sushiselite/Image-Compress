# Image Compressor

The Image Compressor is a Python-based application that allows you to compress images using lossy compression. It provides a graphical user interface (GUI) that enables users to select an input image file, choose an output directory, and compress the image with the specified settings.

## Features

- Supports lossy compression of JPEG and PNG images.
- Provides a user-friendly GUI for easy interaction.
- Allows users to select the input image file using a file explorer.
- Supports selecting the output directory using a file explorer.
- Displays a progress bar to track the compression process.
- Shows status messages indicating the success or failure of the compression.
- Generates a compressed image file in JPEG format.

## Usage

1. Run the `image_compressor_gui.exe` executable.
2. Click the "Import" button to select the input image file.
3. Click the "Output" button to choose the output directory.
4. Click the "Compress" button to start the image compression process.
5. Monitor the progress bar to track the compression progress.
6. Once the compression is complete, a success message will be displayed.
7. The compressed image will be saved in the specified output directory.

## Requirements

- Windows operating system.
- No additional software or dependencies are required.

## Building the Executable

If you want to build the executable from the source code, follow these steps:

1. Clone the repository or download the source code files.
2. Install the required dependencies.
3. 3. Run the PyInstaller command to generate the executable:

```shell
pyinstaller --onefile --distpath=build --icon=my_icon.ico image_compressor_gui.py
```
Replace `my_ico.ico` with the path to your custom icon file.
4. The executable will be generated in the "build" directory.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to explore, modify, and use the code according to the terms of the license.
