import pytest
from src.string_reversal import reverse_string

def test_basic_string_reversal():
    """Test standard string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_empty_string():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_single_character():
    """Test reversal of a single character string."""
    assert reverse_string("a") == "a"

def test_palindrome():
    """Test reversal of a palindrome."""
    assert reverse_string("racecar") == "racecar"

def test_string_with_spaces():
    """Test reversal of a string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_string_with_special_characters():
    """Test reversal of a string with special characters."""
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_unicode_string():
    """Test reversal of a string with unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(12345)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])