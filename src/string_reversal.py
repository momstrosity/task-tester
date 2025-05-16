def reverse_string(input_string: str) -> str:
    """
    Reverses the given input string using a manual character-by-character reversal method.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is None.
    """
    # Validate input
    if input_string is None:
        raise ValueError("Input cannot be None")
    
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using a list of characters
    reversed_chars = []
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    return ''.join(reversed_chars)