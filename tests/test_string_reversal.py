import pytest
from src.string_reversal import reverse_string

def test_reverse_standard_string():
    """Test reversing a standard ASCII string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_special_characters():
    """Test reversing strings with special characters."""
    assert reverse_string("a1b2c3") == "3c2b1a"
    assert reverse_string("!@#$%^") == "^%$#@!"

def test_reverse_unicode_string():
    """Test reversing Unicode strings."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("🌈🚀") == "🚀🌈"

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["not", "a", "string"])