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
    """Test reversal with special characters and spaces."""
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"
    assert reverse_string("  trim  ") == "  mirt  "

def test_reverse_string_unicode():
    """Test reversal with Unicode characters."""
    assert reverse_string("こんにちは") == "はちにんこ"
    assert reverse_string("🌈🦄") == "🦄🌈"

def test_reverse_string_invalid_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])