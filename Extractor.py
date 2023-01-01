from Pixel import Pixel
from Embedder import a2b, b2a


class Extractor:
    """
    this class will handle extracting text over pixels
    it will go over every 4-pixel group and extract the character from their
    last 2 bits, making 8 bits, or 1 character. It will do this until there are
    3 ^ symbols in a row(via accumulator), meaning the iteration over pixels
    will stop and the message will be returned. (So we won't need to go over
    every single pixel wastefully)


    Instructions:

    1. Make a method that takes in a pixel and converts the lowest rgb-value to
    binary.
    2. Extract the last 2 bits.
    3. Do this 4 times for 1 4-pixel group, and combine the 8 bits in 1 string
    and apply b2a
    4. Add the result to a string S and repeat until '^^^' is in S, then
    terminate the process
    """

    def __init__(self):
        self.pixel_array = ...
        self.flattened_array = []


    def pixel_array_flattener(self) -> list:
        """
        :return: The 1-dimensional representation of the 2-dimensional array
        holding the image's pixels, for easier 4-item iteration
        """
        for row in self.pixel_array:
            self.flattened_array.extend(row)
        return self.flattened_array


    def bits_extractor(self, pixel: Pixel) -> chr:
        """
        :param pixel: The Pixel object who's rgb will be analyzed to extract
        the 2 bits
        :return: The 2 bits which will make up a quarter of the character
        embedded into 4 pixels
        """
        return pixel.lowest_rgb_binary[-2:]

    def bits_combiner_to_byte(self, b1: str, b2: str, b3: str, b4: str):
        """
        :param b1, b2, b3, b4: the 4 bit pairs, each from their own Pixel
        :return: The byte achieved when combining all 4 bit pairs
        """
        if len(b1) == 2 and len(b2) == 2 and len(b3) == 2 and len(b4) == 2:
            char_byte = b1 + b2 + b3 + b4
            char = b2a(char_byte)
            if type(char) == chr:
                return char
            return ("char is not of type 'chr'!!!!")
        return ("Some bit pairs may not be of length 2!!!!")



