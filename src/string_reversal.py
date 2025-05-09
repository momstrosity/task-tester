def reverse_string(input_string):
    """
    Reverse the given input string manually.

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
    
    # Handle empty string case
    if len(input_string) == 0:
        return ""
    
    # Manually reverse the string using a list and two-pointer technique
    # Convert string to list to allow manipulation
    chars = list(input_string)
    
    # Two-pointer technique to reverse in-place
    left = 0
    right = len(chars) - 1
    
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    # Convert list back to string and return
    return ''.join(chars)