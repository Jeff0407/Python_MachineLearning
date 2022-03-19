"""
File: Image_ Restoration
Name: Yu-Ju Fang

Finding the minimum error by using least squares estimation and  contsruct the
optimal filter. By applying the optimal filter to the blurred image and two
noisy image. We can restore them.
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import cm

gray = cm.get_cmap('gray', 256)


def smaple(image_c, image_o):
    """
    Use the original img14g.tif for Y and use img14bl.tif for X.
    Only sample the pairs (zs,ys) at (1/400)th of the pixel locations
    in the image by taking a sample at every 20th column and every 20th row
    :param image_c: input, corrupted image
    :param image_o: input, desired image
    :return: the surrounding pixels of each pixel and the sampled pixels from the desired image
    """
    height, width = image_o.shape
    total_pixels = 0  # Calculate how many pixels has been sampled
    Z = []
    Y = []
    surround_x = []

    for i in range(3, height):
        for j in range(3, width):
            if i % 20 == 0 and j % 20 == 0:
                total_pixels += 1
                for a in range(-3, 4):
                    for b in range(-3, 4):
                        surround_x.append(image_c[i + a][j + b])

                # surround_x = np.array(surround_x)
                Z.append(surround_x)
                surround_x = []

                # Find each ys
                Y.append(image_o[i][j])

    Z = np.array(Z)
    Y = np.array(Y)
    Y = Y.reshape(Y.shape[0], 1)
    return Z, Y, total_pixels


def restoration(image_c, theta):
    """
    By Multiplying the surrounding pixels of a pixel with corresponding filter coefficients, we can get the estimated
    pixel value for each pixel
    :param image_c: input, the corrupted image with numpy array format
    :param theta: the filter coefficient
    :return: the restored image
    """

    height, width = image_c.shape
    new_image = np.zeros((height, width))  # Record the the estimated ys_hat
    surround_x = []

    for i in range(0, height):
        for j in range(0, width):
            if (i - 3 >= 0 and j - 3 >= 0) and (j + 3 <= width - 1 and i + 3 <= height - 1):
                for a in range(-3, 4):
                    for b in range(-3, 4):
                        surround_x.append(image_c[i + a][j + b])
                zs = np.array(surround_x)
                surround_x = []
                ys_hat = np.dot(zs, theta)
                new_image[i][j] = ys_hat
            else:
                new_image[i][j] = image_c[i][j]
    return new_image


def dot(M_T, M, N):
    new_M = np.zeros((49, M.shape[1]))
    sum = 0
    for i in range(49):
        for j in range(M.shape[1]):
            for t in range(N):
                sum += int(M_T[i][t]) * int(M[t][j])
            new_M[i][j] = sum
            sum = 0
    return new_M


def main():
    Y = Image.open('img14g.tif')
    X = Image.open('img14sp.tif')
    y = np.array(Y)  # original image
    x = np.array(X)  # corrupted image

    # Sample the original and corrupted image
    Z, Y, N = smaple(x, y)

    # Compute estimates of the covariance matrix Rzz and the cross correlation rzy
    Rzz = dot(Z.T, Z, N) / N
    rzy = dot(Z.T, Y, N) / N

    # Calculate the corresponding filter coefficients θ
    theta = np.dot(np.linalg.inv(Rzz), rzy)
    # reshape_theta = theta.reshape((7, 7))

    # Restore the image
    new_image = restoration(x, theta)

    plt.imshow(new_image, cmap=gray)
    plt.show()


if __name__ == '__main__':
    main()