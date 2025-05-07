def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string using a manual character-by-character reversal method.

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
    
    # Use a list to manually reverse the string
    reversed_chars = []
    
    # Iterate through the string from last to first character
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Convert the list of characters back to a string
    return ''.join(reversed_chars)