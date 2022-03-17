"""
File: shrink.py
Name:Yu-Ju Fang      
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,s
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, input the filename of the image
    :return img: SimpleImage, return the shrink image
    the pixels colors in out image can be found by multiply two times x and y coordinate in out image
    and use the multiplied coordinate to get pixel color in original image
    """
    img = SimpleImage(filename)
    out = SimpleImage.blank(img.width // 2, img.height // 2)  # create a blank
    for x in range(out.width):
        for y in range(out.height):
            pixel = img.get_pixel(x * 2, y * 2)
            new_pixel = out.get_pixel(x, y)

            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue

    return out


def main():
    """
    First, output a original image and then input the original image into shrink function and output the
    result shrink image
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
