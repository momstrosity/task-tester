def reverse_string(input_str):
    """
    Reverse a given string manually without using built-in reversal methods.

    Args:
        input_str (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Convert string to list of characters for manipulation
    chars = list(input_str)
    
    # Manual reversal using two-pointer technique
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string
    return ''.join(chars)