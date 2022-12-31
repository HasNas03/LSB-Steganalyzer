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
# listy = [50, 100, 50]
# colorval = min(listy)
# print(colorval, listy.index(colorval))
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


print(a2b("100"))
print(b2a("01100010011000000110011"))

l = "01100010011000000110000"
print(l[:-2])
