def reverse_string(input_string: str) -> str:
    """
    Reverses the given input string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is None.
    """
    # Check for invalid inputs
    if input_string is None:
        raise ValueError("Input cannot be None")
    
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Reverse the string using slice notation
    return input_string[::-1]