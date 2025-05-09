def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string using a manual character-by-character approach.

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
    
    # Create a list to store reversed characters
    reversed_chars = []
    
    # Iterate through the string from end to beginning
    for i in range(len(input_string) - 1, -1, -1):
        reversed_chars.append(input_string[i])
    
    # Join the characters back into a string
    return ''.join(reversed_chars)