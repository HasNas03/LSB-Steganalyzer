from Embedder import a2b, b2a


class Pixel:
    def __init__(self, redval, greenval, blueval):
        """
        :param redval: The red value of the pixel
        :param greenval: The green value of the pixel
        :param blueval: The blue value of the pixel
        """
        self.rgb_list = [redval, greenval, blueval]
        self.lowest_rgb_value = min(self.rgb_list)
        self.lowest_rgb_binary = a2b(str(self.lowest_rgb_value))
        self.lowest_rgb_index = self.rgb_list.index(self.lowest_rgb_value)

    def embed_char(self, bits: str) -> str:
        """
        :param bits:
        :return:
        """
        embedded_value = str(self.lowest_rgb_binary[:-2] + bits)
        new_rgb_val = b2a(embedded_value)
        return new_rgb_val

    def execute(self, new_bits: str):
        """
        :param new_bits:
        :return:
        """
        new_pixel_rgb = self.rgb_list[:]
        new_pixel_rgb[self.lowest_rgb_index] = self.embed_char(new_bits)
        return str(new_pixel_rgb[0]) + str(new_pixel_rgb[1]) + str(
            new_pixel_rgb[2])
        # change return statement to return a proper format/Pixel object


p = Pixel(200, 100, 250)
print(p.execute("11"))
# should get Pixel(200, 103, 250)
