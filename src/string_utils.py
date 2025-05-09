def reverse_string(input_string: str) -> str:
    """
    Reverse the given string using a manual iteration approach.

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
    
    # Convert string to list of characters and reverse manually
    reversed_chars = []
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Join the reversed characters back into a string
    return ''.join(reversed_chars)