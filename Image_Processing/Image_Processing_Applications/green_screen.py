"""
File: green_screen.py
Name:Yu-Ju Fang
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, input the background image
    :param figure_img: SimpleImage, input the figure image
    :return: SimpleImage, the combined image of background image and figure image
    """
    result_img = SimpleImage.blank(figure_img.width, figure_img.height)
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            result_pixel = result_img.get_pixel(x, y)
            background_pixel = background_img.get_pixel(x, y)

            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > 2 * bigger:  # check whether the pixel is green
                result_pixel.red = background_pixel.red
                result_pixel.green = background_pixel.green
                result_pixel.blue = background_pixel.blue
            else:
                result_pixel.red = figure_pixel.red
                result_pixel.green = figure_pixel.green
                result_pixel.blue = figure_pixel.blue

    return result_img


def main():
    """
    Extract the the figure in ReyGreenScreen.png and the combine it with MillenniumFalcon.png and
    show the result image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()

    
if __name__ == '__main__':
    main()
