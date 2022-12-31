import binascii



def a2b(char: str) -> str:
    """
    Return the binary representation of an ASCII character
    """
    # string.encode() function turns the specified string into an array of bytes
    byte_array = char.encode()
    # Convert the byte_array into a binary integer
    binary_int = int.from_bytes(byte_array, "big")
    # Convert binary_int to a string of binary characters
    binary_string = bin(binary_int)
    return binary_string[0] + binary_string[2:]
def b2a(char: str):
    """
        Return the ASCII representation of a binary string
        """
    input_string = int(char, 2)
    # Obtain the total number of bytes
    Total_bytes = (input_string.bit_length() + 7) // 8

    # Convert these bits to bytes
    input_array = input_string.to_bytes(Total_bytes, "big")

    # Convert the bytes to an ASCII value and display it on the output screen
    ASCII_value = input_array.decode()
    return ASCII_value

class Pixel():

    def __init__(self, redval, greenval, blueval):
        """

        """
        self.red = redval
        self.green = greenval
        self.blue = blueval
        self.lowest_rgb_binary = None
        self.lowest_rgb_index = None
        self.rgb_list = [self.red, self.green, self.blue]

    def lowest_rgb2binary(self) -> None:
        """
        Return a 2-tuple (x,y), where:
        x: the value of the lowest rgb value (in ASCII)
        y: the index of that lowest value in self.rgb_list, meaning a 0, 1, or
        2 means the lowest rgb value belongs to red, green, or blue respectively
        """
        self.lowest_rgb_value = min(self.rgb_list)
        self.lowest_rgb_index = self.rgb_list.index(self.lowest_rgb_value)
        self.lowest_rgb_binary = a2b(str(self.lowest_rgb_value))

    def least_color2binary(self, bits: str) -> str:
        """

        :param bits:
        :return:
        """
        embedded_value = str(self.lowest_rgb_binary[:-2] + bits)
        new_rgb_val = b2a(embedded_value)
        return new_rgb_val

    def embed(self, new_bits: str):
        """

        :param new_bits:
        :return:
        """
        self.lowest_rgb2binary()
        new_pixel_rgb = self.rgb_list[:]
        new_pixel_rgb[self.lowest_rgb_index] = self.least_color2binary(new_bits)
        return str(new_pixel_rgb[0]) + str(new_pixel_rgb[1]) + str(new_pixel_rgb[2])


p = Pixel(200, 100, 250)
print(p.embed("11"))


# should get Pixel(200, 103, 250)
