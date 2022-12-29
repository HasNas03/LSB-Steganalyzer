
def a2b(char: str) -> str:
    """
    A function that returns the binary representation of an ASCII character
    :param char:
    :return the binary representation of an ASCII character (8 digits long):
    """
    # string.encode() function turns the specified string into an array of bytes
    byte_array = char.encode()
    # Convert the byte_array into a binary integer
    binary_int = int.from_bytes(byte_array, "big")
    # Convert binary_int to a string of binary characters
    binary_string = bin(binary_int)
    return binary_string[0] + binary_string[2:]
