def reverse_string(input_string):
    """
    Reverse the characters in a given string using manual character iteration.

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
    
    # Convert string to list of characters for manual reversal
    chars = list(input_string)
    
    # Swap characters from start to end
    left = 0
    right = len(chars) - 1
    
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move towards the center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)