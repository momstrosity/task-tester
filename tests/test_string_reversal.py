import pytest
from src.string_reversal import reverse_string

def test_reverse_standard_string():
    """Test reversing a standard string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_reverse_palindrome():
    """Test reversing a palindrome."""
    assert reverse_string("racecar") == "racecar"

def test_reverse_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_reverse_mixed_characters():
    """Test reversing a string with mixed character types."""
    assert reverse_string("Hello, World! 123") == "321 !dlroW ,olleH"

def test_reverse_raises_type_error():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])