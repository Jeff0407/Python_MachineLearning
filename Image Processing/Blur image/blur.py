"""
File: blur.py
Name:Jeff
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the input image
    :return: the processed image which is blurred

    the function calculate the every position and its neighbors' pixel color and then average then
    set it as the new pixel's RGB
    """
    sum_red = 0
    sum_blue = 0
    sum_green = 0
    neighbors = 0
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_pixel = new_img.get_pixel(x, y)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if x + i >= 0 and x+i <= img.width -1 and y + j >= 0 and y + j <= img.height -1:
                        sum_red += img.get_pixel(x + i, y + j).red
                        sum_blue += img.get_pixel(x + i, y + j).blue
                        sum_green += img.get_pixel(x + i, y + j).green
                        neighbors += 1
            new_pixel.red = sum_red // neighbors
            new_pixel.blue = sum_blue // neighbors
            new_pixel.green = sum_green // neighbors

            neighbors = 0
            sum_red = 0
            sum_blue = 0
            sum_green = 0

    return new_img


def main():
    """
    First show the original image and then input the image into the blur function and output the processed
    image that is blurred
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
