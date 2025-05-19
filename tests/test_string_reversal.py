import pytest
from src.string_reversal import reverse_string

def test_reverse_normal_string():
    """Test reversing a standard string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_char_string():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("hello!@#") == "#@!olleh"

def test_reverse_unicode_string():
    """Test reversing a Unicode string."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)