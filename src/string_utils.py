def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string manually, preserving all characters.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use a manual reversal approach with a list
    reversed_chars = []
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    return ''.join(reversed_chars)