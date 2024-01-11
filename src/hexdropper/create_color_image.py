def create_color_image(hex_code, image_size=(200, 200)):
    """
    Create an image with a specific background color and display the hex code.

    Parameters
    ----------
    hex_code : str
        A hexadecimal color code string (e.g., 'FF5733'), without the '#' symbol.
    image_size : tuple of int, optional
        The size of the image as a (width, height) tuple. Default is (200, 200).

    Returns
    -------
    None
        The function saves the created image as a PNG file with the name based on
        the hex code (e.g., 'FF5733.png').

    Examples
    --------
    >>> create_color_image('FF5733')
    # This will create an image with a red background and 'FF5733' text in the center.

    >>> create_color_image('00FF00', (100, 100))
    # This will create a 100x100 green background image with '00FF00' text in the center.
    """
