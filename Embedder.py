

class Embedder():
    """
    The main class handling text-embedding into the image

    === Attributes ===
    text: The text to be embedded into the image
    length: The length of the text
    image: The path to the image
    """

    def __int__(self, text: str, image: str) -> None:
        self.text = text
        self.length = len(text)
        self.image = image

    def enough_pixels(self) -> bool:
        """
        Returns a Boolean of whether there are enough pixels in the image to
        successfully embed the text
        """
        return len(self.text) <= ... #image pixels / 4, since last 2 bits are
        # holding the text bits, so 4 pixels are needed since 2 * 4 = 8
# def a2b(char: str) -> str:
#         """
#         Return the binary representation of an ASCII character
#         """
#         # string.encode() function turns the specified string into an array of bytes
#         byte_array = char.encode()
#         # Convert the byte_array into a binary integer
#         binary_int = int.from_bytes(byte_array, "big")
#         # Convert binary_int to a string of binary characters
#         binary_string = bin(binary_int)
#         return binary_string[0] + binary_string[2:]
# def b2a(char: str):
#         """
#         Return the ASCII representation of a binary string
#         """
#         input_string = int(char, 2)
#         # Obtain the total number of bytes
#         Total_bytes = (input_string.bit_length() + 7) // 8
#         # Convert these bits to bytes
#         input_array = input_string.to_bytes(Total_bytes, "big")
#         # Convert the bytes to an ASCII value and display it on the output screen
#         ASCII_value = input_array.decode()
#         return ASCII_value
def a2b(text: str) -> str:
    """
    Return the binary representation of the ASCII string
    """
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
    Return the ASCII representation of the binary string
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
