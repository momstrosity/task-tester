import pytest
from src.string_reversal import reverse_string

def test_reverse_normal_string():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_single_character():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_special_characters():
    """Test reversing string with special characters."""
    assert reverse_string("hello!") == "!olleh"
    assert reverse_string("@#$%^") == "^%$#@"

def test_reverse_unicode_string():
    """Test reversing a string with Unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("Привет") == "тевирП"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])