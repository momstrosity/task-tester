import pytest
from src.string_reversal import reverse_string

def test_reverse_standard_string():
    """Test reversing a standard string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_palindrome():
    """Test reversing a palindrome string."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("h3llo!") == "!oll3h"

def test_reverse_with_mixed_characters():
    """Test reversing a string with mixed characters."""
    assert reverse_string("A1b2C3!@") == "@!3C2b1A"

def test_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
        reverse_string(None)
        reverse_string(["hello"])