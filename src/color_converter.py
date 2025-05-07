def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """
    Convert RGB color values to a hexadecimal color code.

    Args:
        red (int): Red color value (0-255)
        green (int): Green color value (0-255)
        blue (int): Blue color value (0-255)

    Returns:
        str: Hexadecimal color code (6 characters)

    Raises:
        ValueError: If any color value is outside the range 0-255
    """
    # Validate input values
    for color, color_name in [(red, 'Red'), (green, 'Green'), (blue, 'Blue')]:
        if not isinstance(color, int):
            raise TypeError(f"{color_name} must be an integer")
        if color < 0 or color > 255:
            raise ValueError(f"{color_name} must be between 0 and 255")
    
    # Convert RGB to hex
    return f"{red:02x}{green:02x}{blue:02x}"