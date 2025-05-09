def reverse_string(input_string):
    """
    Reverse a given string using a manual character-by-character approach.

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
    
    # Use a list to build the reversed string
    reversed_chars = []
    
    # Iterate through the string from end to beginning
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Convert list of characters back to string
    return ''.join(reversed_chars)