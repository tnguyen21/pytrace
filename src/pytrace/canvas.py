# import sys
# import os
# sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src/pytrace")

# # hack to get relative imports working in script
# # pylint: disable=wrong-import-position
# # pylint: disable=import-error
# from tuple import Color

from .tuple import Color

class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pixels = [[Color(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def write_pixel(self, x: int, y: int, color: Color) -> None:
        self.pixels[y][x] = color

    def to_ppm(self) -> str:
        """
        * use [:-1] at end of strings to exlude extra " " whitespace
        """
        header = f"P3\n{self.width} {self.height}\n255\n"

        img = ""
        for pixel_row in self.pixels:
            ppm_row = ""
            for pixel in pixel_row:
                r, g, b = pixel.scale_255()
                r, g, b = str(r), str(g), str(b)
                if len(ppm_row) + len(r) > 70:
                    img += ppm_row[:-1] + "\n"
                    ppm_row = ""
                ppm_row += r + " "

                if len(ppm_row) + len(g) > 70:
                    img += ppm_row[:-1] + "\n"
                    ppm_row = ""
                ppm_row += g + " "

                if len(ppm_row) + len(b) > 70:
                    img += ppm_row[:-1] + "\n"
                    ppm_row = ""
                ppm_row += b + " "

            img += ppm_row[:-1]
            img +="\n"

        return header + img
