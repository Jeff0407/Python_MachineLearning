"""
File: fire.py
Name:Yu-Ju Fang
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename str, the filename of the image
    :return: SimpleImage, the processed image
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.green+pixel.blue+pixel.red)//3  # calculate the average pixel value of red, green and blue
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg
    return img


def main():
    """
    First show the original fire.png image and then input the image to highlight_fires function
    ans show the result of fire highlight image
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
