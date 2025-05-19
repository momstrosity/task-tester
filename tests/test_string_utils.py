import pytest
from src.string_utils import reverse_string

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
    """Test reversal of string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversal of string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_string_unicode():
    """Test reversal of unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_string_invalid_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(None)
    
    with pytest.raises(TypeError):
        reverse_string(["hello"])