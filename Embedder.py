import os
from PIL import Image
from Pixel import Pixel

num_status = False
gv = 0
class Embedder:
    """
    The main class handling text-embedding into the image

    === Attributes ===
    text: The text to be embedded into the image
    length: The length of the text
    image: The path to the image
    """

    def __init__(self, text: str, image: str) -> None:
        self.text = text
        self.length = len(text)
        self.image = image
        self.key = "" # 1 char = 4 pixels/indexes, len(text) = len(text) * 4 pixels indexes
        self.pixel_array = []

    def pixel_extraction(self) -> bool:
        # Check if the file exists
        if not os.path.exists(self.image):
            raise ValueError("File does not exist")
        # Open the image and get the size
        image = Image.open(self.image)
        width, height = image.size
        # Get the pixel data as a list of tuples
        pixels = list(image.getdata())
        # Convert the list of tuples to a 2D list
        result = []
        for i in range(0, len(pixels), width):
            result.append(pixels[i:i + width])
        self.pixel_array = result
        # Return the number of pixels and the 2D list of pixels
        pixel_count = 0
        for i in result:
            pixel_count += len(i)
        if width * height == pixel_count:
            return 2 * (4 * (len(self.text))) <= pixel_count

    def embed(self):
        global gv
        if self.pixel_extraction():
            flat_pixel_array = [item for subarray in self.pixel_array for item in subarray]
            text_index = 0
            #start_index, end_index = 0, 4
            #print(flat_pixel_array)
            while text_index < len(self.text):
                charval = self.text[text_index]
                charbin = a2b(charval)

                charbin = list(map(''.join, zip(*[iter(charbin)] * 2)))
                target_p = list(flat_pixel_array[gv:gv+4]) # error is here

                for i in range(len(target_p)):
                    pval = target_p[i]
                    charval = charbin[i]
                    p = Pixel(pval[0], pval[1], pval[2])
                    new_rgb = p.execute(charval)

                    flat_pixel_array[gv] = new_rgb
                    self.key += str(p.minimum_rgb())
                    gv+=1
                text_index += 1
                # start_index += 4
                # end_index += 4
            gv = 0
            self.key_embed(flat_pixel_array)
            return flat_pixel_array

        return "Not enough pixels in image to handle your text and the index key"

    def key_embed(self, one_d_array: list):
        global gv
        pixels_needed = len(self.key) * 4
        pixel_work = one_d_array[pixels_needed:]
        old = pixel_work[:]
        text_index = 0
        while text_index < len(self.key):
            charval = self.key[text_index]
            charbin = a2b(charval)
            charbin = list(map(''.join, zip(*[iter(charbin)] * 2)))
            target_p = list(pixel_work[gv:gv + 4])
            for i in range(len(target_p)):
                pval = target_p[i]
                charval = charbin[i]
                p = Pixel(pval[0], pval[1], pval[2])
                new_rgb = p.execute(charval)
                pixel_work[gv] = new_rgb
                gv += 1
            text_index += 1
        t = (old, pixel_work)
        return t





def a2b(text: str) -> str:
    """
    :param text: a string of text to be converted
    :return: The binary representation of the ASCII string
    """
    if text.isnumeric():
        global num_status
        num_status = True
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
    global num_status
    if num_status == True:
        return str(int(binary, 2))
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



