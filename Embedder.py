
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

    def enough_pixels(self) -> int:
        """

        :return:
        """
        return self.length * 8
