"""
File: histogram_equalization
Name: Yu-Ju Fang
------------------------------------------------------------
Histogram equalization is a common image enhancement technique.
The objective of this file is to transform the image so that the
output histogram is uniform over the full range of gray values.

Histogram Equalization is effective to deal with image which is
too dark or overexposure.However, it may lose some details in
the image.

"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm

gray = cm.get_cmap('gray', 256)


def equalize(x):
    """
    :param x: Numpy array of image data
    :return: histogram equalized numpy array image datq
    """
    height, width = x.shape
    list_histogram = []
    sum_histogram = 0

    # Calculate how many pixels have the same value for 1 to 255
    for xs in range(256):
        for i in range(height):
            for j in range(width):
                if x[i][j] == xs:
                    sum_histogram += 1
        list_histogram.append(sum_histogram)
        sum_histogram = 0

    # Calculate the cumulative distribution of the list_histogram
    for i in range(len(list_histogram)):
        if i == 0:
            pass
        else:
            list_histogram[i] = list_histogram[i] + list_histogram[i - 1]

    for i in range(len(list_histogram)):
        list_histogram[i] /= (width*height)

    # Normalize
    y_max = max(list_histogram)
    y_min = min(list_histogram)

    for i in range(len(list_histogram)):
        list_histogram[i] = ((list_histogram[i] - y_min) / (y_max - y_min)) * 255

    # Transform all the value of each pixel to integer
    for i in range(height):
        for j in range(width):
            x[i][j] = int(list_histogram[x[i][j]])

    return x


def main():
    im = Image.open('kids.tif')
    x = np.array(im)
    x = equalize(x)
    plt.imshow(x, cmap=gray)
    plt.show()


if __name__ == '__main__':
    main()