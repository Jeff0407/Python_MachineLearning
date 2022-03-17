"""
File: mirror_lake.py
Name:Yu-Ju Fang
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, filename of the original image
    :return: SimpleImage, the processed reflected image
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height*2) # create a new blank with same width and 2 times bigger height
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            new_pixel_1 = new_img.get_pixel(x, y)  # get position of the new blank to reflect the color
            new_pixel_2 = new_img.get_pixel(x, new_img.height-1-y)  # get position of the new blank to reflect the color

            new_pixel_1.red = pixel.red
            new_pixel_1.green = pixel.green
            new_pixel_1.blue = pixel.blue

            new_pixel_2.red = pixel.red
            new_pixel_2.green = pixel.green
            new_pixel_2.blue = pixel.blue

    return new_img


def main():
    """
    First, show the original image and then input the original image into reflect function ans output the
    reflected image and show the reflected image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
