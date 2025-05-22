import pytest
from src.string_reversal import reverse_string

def test_reverse_simple_string():
    """Test reversing a simple string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_characters():
    """Test reversing a string with special characters."""
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_unicode_string():
    """Test reversing a string with Unicode characters."""
    assert reverse_string("café") == "éfac"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)

def test_numeric_string():
    """Test reversing a string of numbers."""
    assert reverse_string("12345") == "54321"