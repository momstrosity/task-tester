import pytest
from src.string_reversal import reverse_string

def test_reverse_normal_string():
    """Test reversing a standard string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_char_string():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("!@#$%") == "%$#@!"

def test_reverse_unicode_string():
    """Test reversing a string with unicode characters."""
    assert reverse_string("áéíóú") == "úóíéá"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])