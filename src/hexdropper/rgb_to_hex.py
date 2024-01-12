def rgb_to_hex(r, g, b):
    """
    Convert RGB color to hexadecimal format.

    Parameters
    ----------
    r : int
        Red component of the color, range 0-255.
    g : int
        Green component of the color, range 0-255.
    b : int
        Blue component of the color, range 0-255.

    Returns
    -------
    str
        The hexadecimal color code is a string. The format of the returned string is 'RRGGBB',
        where RR is the hex representation of the red component, GG of the green, and BB of the blue.

    Examples
    --------
    >>> rgb_to_hex(255, 0, 0)
    'FF0000'  # Red color

    >>> rgb_to_hex(0, 255, 0)
    '00FF00'  # Green color

    >>> rgb_to_hex(0, 0, 255)
    '0000FF'  # Blue color
    """
    return None
