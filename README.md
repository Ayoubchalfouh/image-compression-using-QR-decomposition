
## Image Compression using QR Decomposition

This Python code provides a simple image compression application that utilizes QR decomposition for the compression process. The code allows users to select an image file, apply the QR decomposition technique to compress the image, and display the original and compressed images side by side in a graphical window. Additionally, it shows the sizes of the original and compressed images in kilobytes (KB).

### Features

- Image compression using QR decomposition
- Graphical user interface (GUI) for image selection and display
- Side-by-side comparison of original and compressed images
- Display of image sizes in kilobytes (KB)
- Option to save the compressed image

### How it works

1. The user selects an image file (JPEG or PNG format).
2. The selected image is loaded and displayed in the GUI window.
3. The loaded image undergoes QR decomposition to compress it.
4. The compressed image is displayed alongside the original image in the GUI window.
5. The sizes of the original and compressed images are shown in kilobytes (KB).
6. The user has the option to save the compressed image to a file.

### Requirements

- Python 3.x
- OpenCV
- Tkinter
- Pillow

### Usage

1. Clone the repository or download the code files.
2. Install the required dependencies if not already installed (e.g., `pip install opencv-python`, `pip install pillow`).
3. Run the script: `python image_compression_qr.py`.
4. Select an image file when prompted and observe the GUI window displaying the original and compressed images.
5. Optionally, check the "Save compressed image" checkbox in the GUI to save the compressed image to a file.

Feel free to customize the description according to your preferences, and don't forget to mention any additional details or instructions that might be relevant to users.