import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """Test reversing a single character."""
    assert reverse_string("a") == "a"

def test_reverse_string_with_spaces():
    """Test reversing a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_with_special_chars():
    """Test reversing a string with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)

def test_reverse_string_unicode():
    """Test reversing a string with Unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("🌈rainbow") == "wobniar🌈"