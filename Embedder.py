import os
from PIL import Image

class Embedder:
    """
    The main class handling text-embedding into the image

    === Attributes ===
    text: The text to be embedded into the image
    length: The length of the text
    image: The path to the image
    """

    def __int__(self, text: str, image_path: str) -> None:
        self.text = text
        self.length = len(text)
        self.image = image_path
        self.key = "" # 1 char = 4 pixels/indexes, len(text) = len(text) * 4 pixels indexes
        self.pixel_array = self.pixel_extractor(image_path)

    def pixel_extractor(self, image_path: str) -> list:
        with Image.open(image_path) as image:
            # Get the pixel data as a 2D list of tuples
            pixels = list(image.getdata())
            # Convert each tuple to a list and return the 2D list of pixels
            return [[pixel for pixel in t[0:3]] for t in pixels]

    def enough_pixels(self) -> bool:
        """
        :return: Whether there are enough pixels to hold the text as well as the
        key which holds the indexes of each pixel needed to access the least rgb
        """
        if not os.path.exists(self.image):
            raise FileNotFoundError(
                f"Image file not found at {self.image}")
            # Open the image file in binary mode
        with open(self.image, "rb") as file:
            # Read the file header to get the width and height of the image
            header = file.read(24)
            width = int.from_bytes(header[16:18], byteorder="little")
            height = int.from_bytes(header[18:20], byteorder="little")
            pixel_count = width * height
        return 2 * (4 * (len(self.text))) <= pixel_count

    def embed(self):
        if self.enough_pixels:
            flat_pixel_array = [item for subarray in self.pixel_array for item in subarray]
            text_index = 0
            while text_index < len(self.text):



                text_index += 1

        return "Not enough pixels in image to handle your text and the index key"



def a2b(text: str) -> str:
    """
    :param text: a string of text to be converted
    :return: The binary representation of the ASCII string
    """
    if text.isnumeric():
        return bin(int(text))
    binary_val = []
    # Iterate through each character in the text
    for char in text:
        # Convert the character to its ASCII representation and then to binary
        binary = bin(ord(char))[2:]
        # Pad the binary representation with leading zeros to make it 8 digits long
        binary = '0' * (8 - len(binary)) + binary
        # Add the binary representation to the list
        binary_val.append(binary)
    # Join the binary representations into a single string and return it
    return ''.join(binary_val)


def b2a(binary: str) -> str:
    """
    :param binary: a string of a binary number
    :return: The ASCII representation of the binary string
    """
    binary_list = []
    # Split the binary string into a list of 8-digit binary strings
    for i in range(0, len(binary), 8):
        binary_list.append(binary[i:i+8])
    # Initialize an empty string to store the decoded text
    text_val = ''
    # Iterate through each 8-digit binary string
    for b in binary_list:
        # Convert the binary string to an integer and then to its ASCII representation
        char = chr(int(b, 2))
        # Add the character to the decoded text
        text_val += char
    # Return the decoded text
    return text_val
