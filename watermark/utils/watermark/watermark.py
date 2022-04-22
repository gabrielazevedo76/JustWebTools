import os, sys
from PIL import Image, ImageEnhance

class Watermark():
    def __init__(self, _img: str, _logo: str) -> None:
        self.img = _img
        self.logo = _logo
        self.widthImg, self.heightImg = Image.open(self.img).size[0], Image.open(self.img).size[1]

    # Resize logo (default value = (125, 125))
    def resize(self, opacity: float) -> Image:

        try:
            with Image.open(self.logo) as im:
                if im.mode != "RGBA":
                    im = im.convert("RGBA")
                else:
                    im = im.copy()

                im = im.resize((125, 125))

                # Apply opacity in the image
                alpha = im.split()[3]
                alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
                im.putalpha(alpha)
                self.logo = im

                return im

        except OSError:
            print("cannot resize", self.logo)

    # Merge image choosed with the resized logo
    def merge(self, widthUser, heightUser) -> Image:
        if(widthUser > (self.widthImg - 125) or heightUser > self.heightImg):
            raise Exception("Width and Height have to be between the range given!")

        try:
            with Image.open(self.img) as im, self.logo as logo:
                im.paste(logo, box=(widthUser, heightUser), mask=logo)

                return im
        except:
            print(f"cannot merge {self.img} with {self.logo}")