import Image

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
        pixels_needed = self.length * 8

