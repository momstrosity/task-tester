def reverse_string(input_string: str) -> str:
    """
    Reverse the given input string using manual character manipulation.

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
    
    # Convert string to list for manipulation
    chars = list(input_string)
    
    # Use two-pointer technique to swap characters
    left, right = 0, len(chars) - 1
    
    while left < right:
        # Swap characters from both ends
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers towards the center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)