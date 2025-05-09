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
    assert reverse_string("a!b@c#") == "#c@b!a"

def test_reverse_string_unicode():
    """Test reversal of unicode strings."""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_string_with_spaces():
    """Test reversal of strings with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["hello"])