import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageCompressionWindow(tk.Toplevel):
    def __init__(self, original_image, compressed_image):
        super().__init__()
        self.original_image = original_image
        self.compressed_image = compressed_image
        self.save_option = tk.BooleanVar()

        self.setup_ui()

    def setup_ui(self):
        self.title("Image Compression")
        self.protocol("WM_DELETE_WINDOW", self.on_window_close)

        original_pil_image = Image.fromarray(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB))
        compressed_pil_image = Image.fromarray(cv2.cvtColor(self.compressed_image, cv2.COLOR_BGR2RGB))

        original_resized = original_pil_image.resize((400, 400))
        compressed_resized = compressed_pil_image.resize((400, 400))

        original_photo = ImageTk.PhotoImage(original_resized)
        compressed_photo = ImageTk.PhotoImage(compressed_resized)

        original_label = tk.Label(self, image=original_photo)
        original_label.pack(side=tk.LEFT, padx=10, pady=10)

        compressed_label = tk.Label(self, image=compressed_photo)
        compressed_label.pack(side=tk.LEFT, padx=10, pady=10)

        original_label.image = original_photo
        compressed_label.image = compressed_photo

        original_size = f"Original image size: {self.get_file_size(self.original_image)} KB"
        compressed_size = f"Compressed image size: {self.get_file_size(self.compressed_image)} KB"
        size_label = tk.Label(self, text=f"{original_size}\n{compressed_size}")
        size_label.pack()

        save_checkbox = tk.Checkbutton(self, text="Save compressed image", variable=self.save_option)
        save_checkbox.pack()

    def on_window_close(self):
        if self.save_option.get():
            compressed_file_path = filedialog.asksaveasfilename(
                title="Save the compressed image", defaultextension=".jpg",
                filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
            )
            self.save_compressed_image(compressed_file_path)

        self.destroy()

    def save_compressed_image(self, file_path):
        cv2.imwrite(file_path, self.compressed_image)
        print("Compressed image saved.")

    @staticmethod
    def get_file_size(image):
        # Convert bytes to kilobytes
        size_in_kb = round(image.nbytes / 1024, 2)
        return size_in_kb


def compress_image(image, quality=50):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    Q, R = np.linalg.qr(gray_image)
    quantized_R = np.round(R / quality) * quality
    compressed_image = np.dot(Q, quantized_R)
    return np.uint8(compressed_image)


def select_and_compress():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
    )

    image = cv2.imread(file_path)

    if image is not None:
        compressed_image = compress_image(image, quality=50)
        window = ImageCompressionWindow(image, compressed_image)
        window.mainloop()
    else:
        print("Failed to load the image.")


select_and_compress()