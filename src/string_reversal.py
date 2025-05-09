def reverse_string(input_string):
    """
    Reverse a given string using manual character iteration.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If string is empty, return empty string
    if len(input_string) == 0:
        return ""
    
    # Manually reverse the string using a new list of characters
    reversed_chars = []
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Convert list of characters back to string
    return ''.join(reversed_chars)