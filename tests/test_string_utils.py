import pytest
from src.string_utils import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_special_chars():
    """Test reversal of strings with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_string_unicode():
    """Test reversal of Unicode strings."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("🌍🌎🌏") == "🌏🌎🌍"

def test_reverse_string_single_char():
    """Test reversal of a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_string_invalid_input():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(123)
    
    with pytest.raises(TypeError):
        reverse_string(None)
    
    with pytest.raises(TypeError):
        reverse_string(["hello"])