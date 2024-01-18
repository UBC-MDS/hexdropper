import numpy as np

def most_common_rgb(input_array):
    """Determine the most common RGB values based on an image-derived array.

    The input

    Parameters
    ----------
    input_array : ndarray(dtype=float, ndim=3)
        Array containing data from a cropped image

    Returns
    -------
    tuple
        Most common RGB values.

    Examples
    --------
    >>> most_common_rgb(img_arr)
    """
    # check that the input range is between 0 and 255
    
    # check that the input are integers (i.e., whole numbers) with no decimal values
    
    # check that the input has the correct dimension i.e., [:, :, 3] 

    # reshape array to create a tuple with the rgb values, i.e., (r, g, b)
    width, height = input_array.shape[0], input_array.shape[1]
    reshaped_array = input_array.reshape(width * height, 3)
    rgb_array = list(map(tuple, reshaped_array))

    # count the RGB values of each pixel and return the most frequent colour
    rgb_dict = {}
    for i in rgb_array: 
        if i not in rgb_dict:
            rgb_dict[i] = 0
        rgb_dict[i] += 1
          
    most_frequent_colour = max(rgb_dict, key=rgb_dict.get)
    most_frequent_colour = list(most_frequent_colour)
    return most_frequent_colour

