def reverse_string(input_string: str) -> str:
    """
    Reverse a given string using a manual character-by-character reversal approach.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check for invalid input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Convert string to list of characters and reverse manually
    char_list = list(input_string)
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap characters
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(char_list)