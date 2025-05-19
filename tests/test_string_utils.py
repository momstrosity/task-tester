import pytest
from src.string_utils import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test string reversal with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test string reversal with special characters."""
    assert reverse_string("a!b@c#") == "#c@b!a"

def test_reverse_string_with_unicode():
    """Test string reversal with unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_string_none_input():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot be None"):
        reverse_string(None)

def test_reverse_string_non_string_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(['a', 'b', 'c'])
    
    with pytest.raises(TypeError):
        reverse_string({"key": "value"})