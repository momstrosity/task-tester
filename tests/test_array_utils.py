import pytest
from src.array_utils import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simple nested array."""
    input_array = [1, [2, 3], 4]
    assert flatten_array(input_array) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    input_array = [1, [2, [3, 4]], [5, [6, 7]]]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_non_nested_array():
    """Test flattening an array without nesting."""
    input_array = [1, 2, 3, 4, 5]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types_array():
    """Test flattening an array with mixed types and nesting."""
    input_array = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    assert flatten_array(input_array) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_single_item_array():
    """Test flattening an array with a single nested item."""
    input_array = [1, [2]]
    assert flatten_array(input_array) == [1, 2]

def test_flatten_non_list_input():
    """Test flattening a non-list input."""
    assert flatten_array(5) == [5]
    assert flatten_array('string') == ['string']

def test_flatten_complex_nested_array():
    """Test flattening a complex deeply nested array."""
    input_array = [1, [2, [3, [4, [5]]]], 6]
    assert flatten_array(input_array) == [1, 2, 3, 4, 5, 6]