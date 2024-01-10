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
    