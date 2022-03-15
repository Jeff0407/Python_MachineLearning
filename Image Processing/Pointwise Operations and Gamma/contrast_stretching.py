"""
File: contrast_strecthing
Name: Yu-Ju Fang
------------------------------------------------------------
This particular transformation maps the “darker” pixels in the range [0,T1]
to a level of zero (black), and similarly maps the “lighter” pixels in [T2, 255]
to white. Then the pixels in the range [T1, T2] are “stretched out” to use the full scale of [0, 255].
This can have the effect of increasing the contrast in an image.

"""


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm

gray = cm.get_cmap('gray', 256)


def strech(input, T1, T2):
    """
    :param input: Numpy array of the image
    :param T1: int, pixel value smaller than T1 will be assign value 0
    :param T2: int, pixel value larger than T2 will be assign value 255
    :return: the Contrast Stretching Transformation numpy array of image
    """

    height, width = input.shape
    for i in range(height):
        for j in range(width):
            if input[i][j] <= T1:
                input[i][j] = 0
            elif input[i][j] > T2:
                input[i][j] = 255
            else:
                input[i][j] = int(input[i][j] * (255 / (T2 - T1)) - ((255 * T1) / (T2 - T1)))

    return input


def main():
    im = Image.open('kids.tif')
    x = np.array(im)  # Import Image Data into Numpy array.
    output = strech(x, 70, 165)
    plt.imshow(x, cmap=gray)
    plt.show()


if __name__ == '__main__':
    main()