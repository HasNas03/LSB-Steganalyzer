

class Pixel:
    def __init__(self, redval, greenval, blueval):
        """
        :param redval: The red value of the pixel
        :param greenval: The green value of the pixel
        :param blueval: The blue value of the pixel
        """
        self.rgb_list = [redval, greenval, blueval]
        self.lowest_rgb_value = min(self.rgb_list)
        self.lowest_rgb_binary = bin(int(str(self.lowest_rgb_value)))
        self.lowest_rgb_index = self.rgb_list.index(self.lowest_rgb_value)

    def embed_char(self, bits: str) -> str:
        """
        :param bits:
        :return:
        """
        embedded_value = str(self.lowest_rgb_binary[:-2] + bits)
        new_rgb_val = str(int(embedded_value, 2))
        return new_rgb_val

    def execute(self, new_bits: str):
        """
        :param new_bits:
        :return:
        """
        new_pixel_rgb = self.rgb_list[:]
        new_pixel_rgb[self.lowest_rgb_index] = self.embed_char(new_bits)
        t = (new_pixel_rgb[0], new_pixel_rgb[1], int(new_pixel_rgb[2]), 255)
        return t
        # change return statement to return a proper format/Pixel object

    def minimum_rgb(self):
        return self.rgb_list.index(self.lowest_rgb_value)


# def a2b(text: str) -> str:
#     """
#     :param text: a string of text to be converted
#     :return: The binary representation of the ASCII string
#     """
#     if text.isnumeric():
#         return bin(int(text))
#     binary_val = []
#     # Iterate through each character in the text
#     for char in text:
#         # Convert the character to its ASCII representation and then to binary
#         binary = bin(ord(char))[2:]
#         # Pad the binary representation with leading zeros to make it 8 digits long
#         binary = '0' * (8 - len(binary)) + binary
#         # Add the binary representation to the list
#         binary_val.append(binary)
#     # Join the binary representations into a single string and return it
#     return ''.join(binary_val)


# def b2a(binary: str) -> str:
#     """
#     :param binary: a string of a binary number
#     :return: The ASCII representation of the binary string
#     """
#     return str(int(binary, 2))
#     # binary_list = []
#     # # Split the binary string into a list of 8-digit binary strings
#     # for i in range(0, len(binary), 8):
#     #     binary_list.append(binary[i:i+8])
#     # # Initialize an empty string to store the decoded text
#     # text_val = ''
#     # # Iterate through each 8-digit binary string
#     # for b in binary_list:
#     #     # Convert the binary string to an integer and then to its ASCII representation
#     #     char = chr(int(b, 2))
#     #     # Add the character to the decoded text
#     #     text_val += char
#     # # Return the decoded text
#     # return text_val
