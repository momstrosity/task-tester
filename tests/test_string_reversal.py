import pytest
from src.string_reversal import reverse_string

def test_reverse_string_basic():
    """Test basic string reversal"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Test reversal of an empty string"""
    assert reverse_string("") == ""

def test_reverse_string_palindrome():
    """Test reversal of a palindrome"""
    assert reverse_string("racecar") == "racecar"

def test_reverse_string_special_chars():
    """Test reversal with special characters"""
    assert reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_reverse_string_unicode():
    """Test reversal of Unicode strings"""
    assert reverse_string("こんにちは") == "はちにんこ"

def test_reverse_string_invalid_input():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError):
        reverse_string(12345)
    with pytest.raises(TypeError):
        reverse_string(None)
    with pytest.raises(TypeError):
        reverse_string(["list"])