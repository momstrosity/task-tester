import pytest
from src.string_reversal import reverse_string

def test_reverse_normal_string():
    """Test reversing a normal string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_empty_string():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_special_characters_and_spaces():
    """Test reversing a string with special characters and spaces."""
    assert reverse_string("a1b2c3 !@#") == "#@! 3c2b1a"
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_unicode_string():
    """Test reversing a string with unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_single_character():
    """Test reversing a single character string."""
    assert reverse_string("a") == "a"

def test_reverse_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list", "of", "strings"])