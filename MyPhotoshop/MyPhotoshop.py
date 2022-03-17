"""
File: Myphotoshop.py
Name: Yu-Ju Fang
----------------------------------------------
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

Input a list of images and try to use color distance algorithm to generate a picture with no people in the image
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    # formula of color distance
    color_distance = ((red - pixel.red)**2 + (blue - pixel.blue)**2 + (green - pixel.green)**2 )**(1/2)

    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0  # the sum of every pixel.red
    total_green = 0  # the sum of every pixel.green
    total_blue = 0  # the sum of every pixel.blue

    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue

    return [total_red // len(pixels), total_green // len(pixels), total_blue // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels(the best pixel)

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    min_color_distance = float("inf")

    pixel_avg = get_average(pixels)

    for pixel in pixels:
        if get_pixel_dist(pixel, pixel_avg[0], pixel_avg[1], pixel_avg[2]) < min_color_distance:
            min_color_distance = get_pixel_dist(pixel, pixel_avg[0], pixel_avg[1], pixel_avg[2])
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)


    pixel_list = []  # add the pixel in same position in all images in the list

    for x in range(width):
        for y in range(height):
            for image in images:
                pixel_list.append(image.get_pixel(x, y))
            best1 = get_best_pixel(pixel_list)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best1.red
            result_pixel.green = best1.green
            result_pixel.blue = best1.blue
            pixel_list = []

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
