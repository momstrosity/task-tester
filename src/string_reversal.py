def reverse_string(input_string: str) -> str:
    """
    Reverse the characters of a given string.

    This function manually reverses a string character by character,
    preserving all original characters including spaces and special characters.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The input string with characters in reverse order.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # For empty string, return empty string
    if len(input_string) == 0:
        return ""
    
    # Convert string to list of characters for manual reversal
    chars = list(input_string)
    
    # Manually reverse the list of characters
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move towards the center
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)