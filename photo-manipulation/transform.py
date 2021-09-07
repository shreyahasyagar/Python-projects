
from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, i.e by how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
     #make an empty image so we dont modify the original one
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values 

    # # this is the non vectorized version i.e we need to change all the values
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_im.array[x, y, c] = image.array[x, y, c] * factor

    # faster version that leverages numpy
    new_im.array = image.array * factor# add the constant value to the array

    return new_im

def adjust_contrast(image, factor, mid):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values 
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

    return new_im
    # vectorized
    # new_im.array=(image.array-mid) * factor +mid

def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (i.e kernel_size = 3  means that neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values 
    neighbor_range = kernel_size // 2  # this is a variable that tells us how many neighbors we actually look at (i.e for a kernel of 3, this value should be 1)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                # use the easy implementation of iterating through each neighbor and summing
                
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):
                    for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        total += image.array[x_i, y_i, c]
                new_im.array[x, y, c] = total / (kernel_size ** 2)
    return new_im
    #the faster way would be   
    # to incorporate some sort of, like memorization,  which means so for example, what we would do is we
    # would move like along the x axis, and every single  time instead of resetting every single neighbor,  
    #we just get rid of one column, and then we add  in the next column, and so on. And that would  
    # decrease the number of operations that we actually  need.

def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we are going to use
    # assume that the kernel is SQUARE
    # for example the sobel x kernel (detecting horizontal edges) is as follows:
    # [1 0 -1]
    # [2 0 -2]
    # [1 0 -1]
    x_pixels, y_pixels, num_channels = image.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values 
    neighbor_range = kernel.shape[0] // 2  # this is a variable that tells us how many neighbors we actually look at (i.e for a 3x3 kernel, this value should be 1)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                for x_i in range(max(0,x-neighbor_range), min(new_im.x_pixels-1, x+neighbor_range)+1):# find which value of kernel this corresponds to
                    for y_i in range(max(0,y-neighbor_range), min(new_im.y_pixels-1, y+neighbor_range)+1):
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_im.array[x, y, c] = total
    return new_im

def combine_images(image1, image2):
    # combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    x_pixels, y_pixels, num_channels = image1.array.shape  # represents x, y pixels of image, # channels (R, G, B)
    new_im = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)  # making a new array to copy values to!
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_im.array[x, y, c] = (image1.array[x, y, c]**2 + image2.array[x, y, c]**2)**0.5 # sq.root of sum
    return new_im
    
if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')

    # brightening

    #brightened_im=adjust_brightness(lake,1.7)
    #brightened_im.write_image('brightened.png')

    brightened_im = brighten(lake, 1.7)
    brightened_im.write_image('brightened.png')

    # darkening

    #darkened_im=adjust_brightness(lake,0.3)
    #darkened_im.write_image('darkened.png')
    darkened_im = brighten(lake, 0.3)
    darkened_im.write_image('darkened.png')

    # increase contrast
    incr_contrast = adjust_contrast(lake, 2, 0.5) # scale is 0 to 1... mid point os 0.5
    incr_contrast.write_image('increased_contrast.png')

    # decrease contrast
    decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    decr_contrast.write_image('decreased_contrast.png')

    # blur using kernel 3
    blur_3 = blur(city, 3)
    blur_3.write_image('blur_k3.png')

    # blur using kernel size of 15
    blur_15 = blur(city, 15)
    blur_15.write_image('blur_k15.png')

    # apply a sobel edge detection kernel on the x and y axis

     # sobel_x_kernel=np.array([
    # [1, 2, 1], 
    # [0, 0, 0], 
    # [-1, -2, -1]
    # ])
    # sobel_y_kernel=np.array([
    # [1, 0, -1], 
    # [2, 0, -2],
    # [1, 0, -1]])

    sobel_x = apply_kernel(city, np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]))
    sobel_x.write_image('edge_x.png')
    sobel_y = apply_kernel(city, np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]]))
    sobel_y.write_image('edge_y.png')

    # combine these and make an edge detector!
    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image('edge_xy.png')

