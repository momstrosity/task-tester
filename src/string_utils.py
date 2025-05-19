def reverse_string(input_string):
    """
    Reverse a given string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is None.
    """
    # Check for None input
    if input_string is None:
        raise ValueError("Input cannot be None")
    
    # Check for non-string input
    if not isinstance(input_string, str):
        raise TypeError(f"Input must be a string, not {type(input_string).__name__}")
    
    # Reverse the string
    return input_string[::-1]