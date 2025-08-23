import colorgram

class Color_Extractor:

    def __init__(self, image, num):
        self.image = image
        self.number_of_colors = num

    def extract(self):
        # Extracting the colours from image.jpeg
        rgb_colors = []
        color = colorgram.extract(self.image, self.number_of_colors)
        for items in color:
            r = items.rgb.r
            g = items.rgb.g
            b = items.rgb.b
            new_color = (r, g, b)
            rgb_colors.append(new_color)
        return rgb_colors
