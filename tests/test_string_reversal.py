import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversal of a single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversal of a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversal of a string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_string_with_unicode():
    """Test reversal of a string with unicode characters."""
    assert reverse_string("café") == "éfac"

def test_reverse_string_none_input():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot be None"):
        reverse_string(None)

def test_reverse_string_non_string_input():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"]))