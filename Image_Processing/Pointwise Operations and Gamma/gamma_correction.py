"""
File: gamma_correction
Name: Yu-Ju Fang
------------------------------------------------------------
gamma correction is used to compensate for the nonlinear behavior of a display device.
Most often images are already encoded in gamma corrected form, and will appear fine when displayed
on most video monitors. However, if an image is stored with a linear scaling it becomes necessary
to correct the image. If the value of gamma for your monitor is known, then the correction process
consists of applying the inverse of equation.

"""


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import cm

Gamma = 3
gray = cm.get_cmap('gray', 256)


def main():
    im = Image.open('gamma15.tif')
    x = np.array(im)
    height, width = x.shape

    for i in range(height):
        for j in range(width):
            if x[i][j] == 0:
                pass
            else:
                x[i][j] = 255 * ((x[i][j] / 255) ** (1 / Gamma))
    plt.imshow(x, cmap=gray)
    plt.show()


if __name__ == '__main__':
    main()