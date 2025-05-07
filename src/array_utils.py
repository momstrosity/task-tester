from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested array into a single-level array.

    This function takes a potentially nested array and returns a flattened 
    version where all nested lists are converted to a single level, 
    maintaining the original order of elements.

    Args:
        arr (List[Union[Any, List]]): The input array that may contain nested lists.

    Returns:
        List[Any]: A flattened version of the input array.

    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    # Base case: if input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # If the list is empty, return an empty list
    if not arr:
        return []
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            flattened.append(item)
    
    return flattened