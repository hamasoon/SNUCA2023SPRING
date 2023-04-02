"""
4190.308 Computer Architecture                                                          Spring 2023

Image blurring (float)

This module implements a function that blurs an image with a 3x3 filter (floating point version)

@author:
    Your Name <your@email.com>

@changes:
    2023/MM/DD Your Name Comment

"""

kernel_3by3 = [[1/9 for x in range(3)] for y in range(3)]
kernel_5by5 = [[1/25 for x in range(5)] for y in range(5)]
kernel_7by7 = [[1/49 for x in range(7)] for y in range(7)]

kernel_dict = {3: kernel_3by3, 5: kernel_5by5, 7: kernel_7by7}

def blur(image, height, width, channels, kernel_size=5):
    """
    Blurs an image with a kernel and returns the blurred image.

    Args:
        image:        image data (multi-level list)
        height:       image height
        width:        image width
        channels:     number of channels (BGR or BGRA)
        kernel_size:  size of blurring kernel

    Returns:
        A tuple containing the following elements:
        - blurred:    blurred image data
        - bheight:    blurred image height
        - bwidth:     blurred image width
        - bchannels:  blurred image channels

    """

    # TODO
    # Your work goes here

    # For now, we simply copy the input parameters into the output parameters.
    # Fix/adjust once you have implemented your solution.
    bheight   = height - (kernel_size - 1)
    bwidth    = width - (kernel_size - 1)
    bchannels = channels
    blurred   = [[[0 for c in range(bchannels)] for w in range(bwidth)] for h in range(bheight)]
    kernel = kernel_dict[kernel_size]

    if kernel_size != 3 & kernel_size != 5 & kernel_size != 7:
        raise ValueError('Kernel must be 3, 5, or 7')

    for h in range(bheight):
        for w in range(bwidth):
            for c in range(bchannels):
                blurred[h][w][c] = 0
                for k_x in range(kernel_size):
                    for k_y in range(kernel_size):
                        blurred[h][w][c] += image[h+k_x][w+k_y][c] * kernel[k_x][k_y]
				
                blurred[h][w][c] = int(blurred[h][w][c])


    return blurred, bheight, bwidth, bchannels



