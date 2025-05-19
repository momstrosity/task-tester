def reverse_string(input_str: str) -> str:
    """
    Reverse the given string manually, character by character.

    Args:
        input_str (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Manual string reversal using list manipulation
    reversed_chars = []
    for char in input_str:
        reversed_chars.insert(0, char)
    
    return ''.join(reversed_chars)