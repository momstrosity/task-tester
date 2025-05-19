def reverse_string(input_string):
    """
    Reverses the given input string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Strict type checking using exact type comparison
    if type(input_string) is not str:
        raise TypeError("Input must be a string")
    
    # Reverse the string using slice notation
    return input_string[::-1]