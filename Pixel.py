from Embedder import a2b, b2a


class Pixel():

    def __init__(self, redval, greenval, blueval):
        """

        """
        self.lowest_rgb_value = None
        self.lowest_rgb_binary = None
        self.lowest_rgb_index = None
        self.rgb_list = [redval, greenval, blueval]

    def fun1(self) -> None:
        """ #lowest_rgb2binary
        Return a 2-tuple (x,y), where:
        x: the value of the lowest rgb value (in ASCII)
        y: the index of that lowest value in self.rgb_list, meaning a 0, 1, or
        2 means the lowest rgb value belongs to red, green, or blue respectively
        """
        self.lowest_rgb_value = min(self.rgb_list)
        self.lowest_rgb_index = self.rgb_list.index(self.lowest_rgb_value)
        self.lowest_rgb_binary = a2b(str(self.lowest_rgb_value))

    def fun2(self, bits: str) -> str:
        """#least_color2binary

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
        self.fun1()
        new_pixel_rgb = self.rgb_list[:]
        new_pixel_rgb[self.lowest_rgb_index] = self.fun2(new_bits)
        return str(new_pixel_rgb[0]) + str(new_pixel_rgb[1]) + str(new_pixel_rgb[2])


p = Pixel(200, 100, 250)
print(p.embed("11"))
# should get Pixel(200, 103, 250)

